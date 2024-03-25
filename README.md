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

**3. Configure workspace:**

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

**4. Install dependencies:**

The project already has many pre-selected good packages, so you can easily get started, or remove unused packages whenever you want.

<details>
  <summary>💡 How to remove unused packages?</summary>

  <p>Here are the most common and effective ways to remove unused packages from the <code>requirements.txt</code> file:</p>
  <h3>1. Manual Review and Editing:</h3>
  <ul>
    <li><strong>Best for small projects:</strong> If you already have a relatively short <code>requirements.txt</code> file, you can often manually go through it and identify packages that are no longer actively used in your code.</li>
    <li><strong>Time-consuming for larger projects:</strong> This becomes less practical as your project and the list of dependencies grow.</li>
  </ul>
  <h3>2. Automated Tools:</h3>
  <p>These tools analyze your project's code to help determine unused dependencies. Here are some popular options:</p>
  <ul>
    <li><strong>pip-autoremove:</strong>
      <ul>
        <li><strong>Install:</strong> <code>pip install pip-autoremove</code></li>
        <li><strong>Usage:</strong> <code>pip-autoremove requirements.txt -o requirements.txt</code> (This overwrites your original file)</li>
      </ul>
    </li>
    <li><strong>pipdeptree (with reverse flag):</strong>
      <ul>
        <li><strong>Install:</strong> <code>pip install pipdeptree</code></li>
        <li><strong>Usage:</strong></li>
        <li><pre><code>pipdeptree -r &gt; possible_unused.txt  # Creates a list of possible unused packages
# Manually review possible_unused.txt and edit requirements.txt
</code></pre></li>
      </ul>
    </li>
    <li><strong>Other Tools:</strong>
      <ul>
        <li><code>pip-unused</code>: A simple command-line tool.</li>
        <li>There may be similar plugins for your IDE or code editor.</li>
      </ul>
    </li>
  </ul>
  <h3>Important Considerations:</h3>
  <ul>
    <li><strong>Caution:</strong> Automated tools can be helpful but they might not be 100% accurate. It's always best to double-check and test your project after removing packages from <code>requirements.txt</code>.</li>
    <li><strong>Version Conflicts:</strong> Sometimes packages might remain indirectly necessary due to dependencies of other required packages. Be mindful of complex dependencies when removing packages.</li>
  </ul>
  <h3>Workflow Example (Using pip-autoremove):</h3>
  <ol>
    <li><strong>Install pip-autoremove:</strong>
      <pre><code>pip install pip-autoremove
</code></pre></li>
    <li><strong>Create a backup (optional, but recommended):</strong>
      <pre><code>cp requirements.txt requirements.txt.bak
</code></pre></li>
    <li><strong>Remove unused packages:</strong>
      <pre><code>pip-autoremove requirements.txt -o requirements.txt
</code></pre></li>
    <li><strong>Review Changes:</strong> Check the updated <code>requirements.txt</code> to make sure the automated tool didn't remove anything essential.</li>
    <li><strong>Test Thoroughly:</strong> Run your project's tests or experiment with it manually to ensure everything still works as expected.</li>
  </ol>

</details>

```bash
cd backend && pip install -r requirements.txt
```

**5. Start the development server:**

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
