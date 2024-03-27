import requests
from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from logger import get_logger
from os import getenv, path

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

logger = get_logger(__name__)
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root() -> str:
    return "Hello, Reliverse and Bleverse!"

@app.get("/favicon.ico")
async def favicon():
    file_name = "favicon.ico"
    file_path = path.join(app.root_path, "static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}

@app.get("/abc")
def abc_test():
    return{"hello":"abc"}

# Backend API health check
@app.get("/backend-health")
def check_backend_health():
    return JSONResponse(content={"status": "ok"}, status_code=200)

# Frontend API health check
@app.get("/frontend-health")
def check_frontend_health():
    frontend_url = "https://relifront.bleverse.com"
    try:
        response = requests.get(frontend_url)
        if response.status_code == 200:
            return JSONResponse(content={"status": "ok", "frontend_health": True}, status_code=200)
        else:
            return JSONResponse(content={"status": "ok", "frontend_health": False}, status_code=200)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error checking frontend health: {e}")
        return JSONResponse(content={"status": "ok", "frontend_health": False}, status_code=200)

def debug_setup():
    if getenv("DEV_MODE") == "true":
        import debugpy
        logger.debug("👨‍💻 Running in dev mode")
        debugpy.listen(("0.0.0.0", 5678))

def run_app():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

if __name__ == "__main__":
    # import needed here if you want debug main.py
    from dotenv import load_dotenv # type: ignore
    load_dotenv()
    debug_setup()
    run_app()
