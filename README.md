# Voice AI Agent - Backend Foundation

A clean, modular starter backend for the **Voice AI Agent** project built with **FastAPI** and **Uvicorn**.

---

## 📁 Project Structure

```text
Voice_AI_Agent/
│
├── .venv/               # Python virtual environment (ignored by Git)
├── .gitignore           # Git ignore rules for Python, virtual environments, and caches
├── requirements.txt     # Python dependencies (FastAPI, Uvicorn)
├── main.py              # FastAPI application entry point
└── README.md            # Project overview and setup documentation
```

---

## 📋 Prerequisites

- **Python**: Version 3.10, 3.11, 3.12, or 3.13 installed.
- **Operating System**: Windows (tested and optimized for Windows PowerShell / Command Prompt).
- **Code Editor**: Visual Studio Code (or any editor of your choice).

---

## 🚀 Quick Start Guide (Windows)

### 1. Open the Project Folder in VS Code
Open VS Code, press `File > Open Folder...`, and select the `Voice_AI_Agent` directory:
```text
C:\Users\Admin\.gemini\antigravity\scratch\Voice_AI_Agent
```

### 2. Activate the Virtual Environment

Open a PowerShell terminal in VS Code (`Ctrl + ` ` ` or `Terminal > New Terminal`) and run:

```powershell
.\.venv\Scripts\Activate.ps1
```

> **PowerShell Execution Policy Tip**: If you see a script execution error (`cannot be loaded because running scripts is disabled on this system`), run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> .\.venv\Scripts\Activate.ps1
> ```

*Alternatively, if you use standard Command Prompt (`cmd`):*
```cmd
.\.venv\Scripts\activate.bat
```

### 3. Install Dependencies

With the virtual environment active:
```powershell
pip install -r requirements.txt
```
*(Or run directly without activation: `.\.venv\Scripts\pip.exe install -r requirements.txt`)*

### 4. Start the Backend Server

You can start the server using either of the following commands:

**Option A (Recommended for development):**
```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Option B (Direct Python execution):**
```powershell
python main.py
```

The server will start at `http://127.0.0.1:8000`.

---

## 🌐 Available Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Welcoming message, service status, and link to docs |
| `GET` | `/health` | Health check endpoint returning status `healthy` |
| `GET` | `/docs` | Interactive Swagger UI API documentation |
| `GET` | `/redoc` | Alternative ReDoc API documentation |

---

## 🛠️ VS Code Integration Tips

1. **Select Python Interpreter**:
   - Press `Ctrl + Shift + P` in VS Code.
   - Type and select **`Python: Select Interpreter`**.
   - Choose the virtual environment: `.\.venv\Scripts\python.exe`.
2. **Automatic Activation**:
   - Once selected, any new integrated terminal opened in VS Code will automatically activate `.venv`.
