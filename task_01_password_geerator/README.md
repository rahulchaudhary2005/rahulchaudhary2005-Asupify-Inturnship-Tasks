# Secure Password Generator

A command-line password generator built with Python's standard library.

## Features
- Custom password length (8–128 characters)
- Letters, numbers, and symbols
- Choose which character groups to include
- At least one character from every selected group
- Generate 1–20 passwords in one batch
- Optional removal of ambiguous characters (I, l, 1, O, 0)
- Cryptographically secure randomness using Python's `secrets` module
- Input validation and graceful Ctrl+C exit

## Requirements
- Python 3.8 or newer
- No third-party packages required

## Run
Open a terminal in this folder and run:

```bash
python password_generator.py
```

Windows alternative:

```bash
py password_generator.py
```

macOS/Linux alternative:

```bash
python3 password_generator.py
```

## Security
Passwords are generated locally and are not sent over the internet. Use a unique password for every account and store it in a trusted password manager. Do not commit real passwords to GitHub.
