# TaskFlow – To-Do List Application

A modular To-Do List application built with Python and Streamlit. Tasks are saved locally in a JSON file, so they remain available after the app is closed.

## Features

- Add tasks with a title and optional description
- View all tasks
- Mark tasks as completed or pending
- Delete unwanted tasks
- Persist task data in `data/tasks.json`
- Filter by All, Pending, or Completed
- Search task titles and descriptions
- Dashboard counters for total, pending, and completed tasks
- Input validation and unit tests

## Project structure

```text
todo_list_streamlit/
├── app.py                         # Streamlit user interface
├── models/
│   └── task.py                    # Task data model
├── services/
│   └── task_service.py             # Application/business logic
├── repositories/
│   └── json_task_repository.py     # JSON file persistence
├── utils/
│   └── validators.py               # Input validation
├── data/
│   └── tasks.json                  # Saved tasks
├── tests/
│   └── test_task_service.py        # Unit tests
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9 or newer
- pip

## Run locally

### 1. Open the project folder

```bash
cd todo_list_streamlit
```

### 2. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start Streamlit

```bash
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`. Open it in your browser.

## Run tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

## How the application is organized

- **Presentation layer (`app.py`)**: displays the interface and handles user interactions.
- **Service layer (`services/`)**: applies task-management rules.
- **Repository layer (`repositories/`)**: reads and writes JSON data.
- **Model layer (`models/`)**: defines the structure of a task.
- **Utility layer (`utils/`)**: validates user input.

This is a small full-stack-style application within Streamlit. It does not use a separate REST API or SQL database because the task specifically requires a local file for persistence.

## Data and privacy

Tasks are stored in `data/tasks.json` on the machine running the app. Do not put sensitive information in a publicly deployed instance. For multi-user or production use, replace the JSON repository with a database and add authentication and authorization.
