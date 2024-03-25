# Relivator: The Docker Edition (Backend)

Frontend's Repo: <https://github.com/blefnk/relivator-docker-frontend>

## Getting Started

### Prerequisites

- **IDE** (VSCode recommended)
- [**Python**](https://python.org/downloads) (tested with 3.11.8 version)
- **Docker and Docker Compose** (for containerized development and deployment)
- **For Windows only:** [Powershell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)

### Installation

The paths below are an example, you can use any you like.

**1. Clone the repository:**

```bash
mkdir C:\B\S\reliverse && cd C:\B\S\reliverse # Windows
mkdir ~/Desktop/B/S/reliverse && cd ~/Desktop/B/S/reliverse # macOS/Linux
git clone https://github.com/blefnk/relivator-docker-backend.git
cd relivator-docker-backend
```

**2. Create and activate a virtual environment:**

**Windows:**

```bash
python -m venv C:\B\A\python\venv\main
```

**macOS/Linux:**

```bash
python -m venv ~/Desktop/B/A/python/venv/main
```

Then open project in VSCode > Ctrl+Shift+P > Terminal: Create New Terminal

**Windows:**

```bash
# Ctrl+Shift+P > Python: Select Interpreter > Enter interpreter path
# Find... > And choose python.exe in C:\B\A\python\venv\main\Scripts
C:\B\A\python\venv\main\Scripts\activate.ps1 # Or use .bat when CMD
```

**macOS/Linux:**

```bash
source ~/Desktop/B/A/python/venv/main/bin/activate
```

**3. Install dependencies:**

```bash
cd backend && pip install -r requirements.txt
```

### Development

**4. Start the development server:**

```bash
uvicorn main:app --reload
# http://localhost:8000
# http://localhost:8000/items/5?q=example
```

### Important notice

Remember to work on the activate virtual environment after each new terminal with:

```bash
C:\B\A\python\venv\main\Scripts\activate.ps1 #.bat
source ~/Desktop/B/A/python/venv/main/bin/activate
```

So you will see something like that:

- Windows `(main) PS C:\B\S\reliverse\relivator-docker-backend\backend >`
- macOS/Linux `(main) user@machine:~/Desktop/B/S/reliverse/relivator-docker-backend/backend$`

### Docker (Optional)

_Instructions for building and running the project using Docker and Docker Compose are forthcoming. Prerequisites:_

- [Docker](https://docs.docker.com/get-docker)
- [Docker Compose](https://docs.docker.com/compose/install)

## Contributing

Thank you for considering contributions to Reliverse, means to Relivator Universe!

1. Follow the installation steps above.
2. Make your changes.
3. Update `requirements.txt` if needed: `pip freeze > requirements.txt`
4. Submit a pull request.
