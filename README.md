# relivator-docker-backend

Relivator: The Docker Edition (Backend) | Frontend: <https://github.com/blefnk/relivator-docker-frontend>

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (latest version is recommended)
- Optional for Windows: [Powershell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)

### On Your System

First things first, run the following commands somewhere outside the repository, e.g. in Desktop:

```bash
cd ~/Desktop && python -m venv relipy
~\Desktop\relipy\Scripts\activate.ps1  # Activate on Windows, PowerShell
~\Desktop\relipy\Scripts\activate.bat  # Activate on Windows, CMD
source ~/Desktop/relipy/bin/activate  # Activate on macOS/Linux
```

After that, open the repo's folder and run the following:

```bash
cd backend && pip install -r requirements.txt
uvicorn main:app --reload
```

### Docker

```bash
-
```

## Contribute

Install as described above, make your changes, update the requirements as needed with `pip freeze > requirements.txt`, and send your fork as pull request.
