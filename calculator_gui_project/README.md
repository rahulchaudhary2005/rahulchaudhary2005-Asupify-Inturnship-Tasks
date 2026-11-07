# PyCalc – Python GUI Calculator

A desktop calculator built with Python and Tkinter.

## Features
- Addition, subtraction, multiplication, division, modulo, and powers
- Parentheses and decimal values
- Clear and backspace
- Dynamic expression/result display
- Keyboard support: Enter calculates, Esc clears, Backspace deletes
- Invalid-expression and division-by-zero handling
- Safe arithmetic parser using Python AST (does not use eval)
- Unit tests

## Project structure
```text
calculator_gui_project/
├── main.py
├── services/
│   └── calculator_service.py
├── utils/
│   └── validators.py
├── tests/
│   └── test_calculator_service.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9+
- Tkinter (usually included with Python)
- No third-party pip packages

## Run
Open a terminal in this folder and execute:
```bash
python main.py
```
Windows alternative:
```powershell
py main.py
```
macOS/Linux alternative:
```bash
python3 main.py
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Architecture
- `main.py`: Tkinter presentation layer and keyboard/button events
- `services/`: arithmetic evaluation and result formatting
- `utils/`: expression input validation
- `tests/`: automated unit tests

Tkinter opens a native desktop window, not a browser page. On Linux, if Tkinter is missing, install the OS package `python3-tk`.
