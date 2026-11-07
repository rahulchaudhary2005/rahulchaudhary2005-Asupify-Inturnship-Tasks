import tkinter as tk
from tkinter import ttk
from services.calculator_service import CalculatorService, CalculatorError
from utils.validators import validate_expression

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCalc - Calculator")
        self.root.geometry("360x500")
        self.root.minsize(320, 440)
        self.root.configure(bg="#151923")
        self.service = CalculatorService()
        self.expression = tk.StringVar()
        self.status = tk.StringVar(value="Ready")
        self._build_ui()
        self.root.bind("<Key>", self._handle_key)

    def _build_ui(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Calc.TButton", font=("Segoe UI", 16, "bold"), padding=12,
                        background="#252c3b", foreground="#f5f7fb", borderwidth=0)
        style.map("Calc.TButton", background=[("active", "#39445a")])
        style.configure("Operator.TButton", font=("Segoe UI", 16, "bold"), padding=12,
                        background="#334d78", foreground="white")
        style.map("Operator.TButton", background=[("active", "#42669e")])
        style.configure("Equal.TButton", font=("Segoe UI", 18, "bold"), padding=12,
                        background="#18a572", foreground="white")
        style.map("Equal.TButton", background=[("active", "#129064")])

        header = tk.Frame(self.root, bg="#151923")
        header.pack(fill="x", padx=18, pady=(18, 8))
        tk.Label(header, text="PyCalc", bg="#151923", fg="#f5f7fb",
                 font=("Segoe UI", 20, "bold")).pack(side="left")
        tk.Label(header, text="PYTHON CALCULATOR", bg="#151923", fg="#8d9ab0",
                 font=("Segoe UI", 8, "bold")).pack(side="right", pady=9)

        display = tk.Frame(self.root, bg="#202737", padx=14, pady=14)
        display.pack(fill="x", padx=18, pady=(8, 12))
        self.entry = tk.Entry(display, textvariable=self.expression, justify="right",
                              font=("Segoe UI", 25), bg="#202737", fg="#ffffff",
                              insertbackground="white", relief="flat", bd=0)
        self.entry.pack(fill="x", ipady=12)
        self.entry.focus_set()
        tk.Label(display, textvariable=self.status, anchor="e", bg="#202737",
                 fg="#aab6c9", font=("Segoe UI", 9)).pack(fill="x", pady=(5, 0))

        keypad = tk.Frame(self.root, bg="#151923")
        keypad.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        buttons = [
            ("C", "clear", "operator"), ("⌫", "backspace", "operator"),
            ("(", "(", "operator"), (")", ")", "operator"),
            ("7", "7", "normal"), ("8", "8", "normal"), ("9", "9", "normal"), ("÷", "/", "operator"),
            ("4", "4", "normal"), ("5", "5", "normal"), ("6", "6", "normal"), ("×", "*", "operator"),
            ("1", "1", "normal"), ("2", "2", "normal"), ("3", "3", "normal"), ("−", "-", "operator"),
            ("0", "0", "normal"), (".", ".", "normal"), ("=", "equals", "equal"), ("+", "+", "operator"),
        ]
        for index, (label, value, kind) in enumerate(buttons):
            row, col = divmod(index, 4)
            style_name = {"normal": "Calc.TButton", "operator": "Operator.TButton",
                          "equal": "Equal.TButton"}[kind]
            ttk.Button(keypad, text=label, style=style_name,
                       command=lambda v=value: self._on_button(v)).grid(
                           row=row, column=col, sticky="nsew", padx=4, pady=4)
        for col in range(4):
            keypad.columnconfigure(col, weight=1, uniform="col")
        for row in range(5):
            keypad.rowconfigure(row, weight=1, uniform="row")

    def _on_button(self, value):
        if value == "clear":
            self.expression.set("")
            self.status.set("Cleared")
        elif value == "backspace":
            self.expression.set(self.expression.get()[:-1])
            self.status.set("Ready")
        elif value == "equals":
            self._calculate()
        else:
            current = self.expression.get()
            if self.status.get().startswith("Result:") and value not in "+-*/).":
                current = ""
            self.expression.set(current + value)
            self.status.set("Ready")

    def _calculate(self):
        raw = self.expression.get().strip()
        error = validate_expression(raw)
        if error:
            self.status.set(error)
            return
        try:
            result = self.service.calculate(raw)
            shown = self.service.format_result(result)
            self.expression.set(shown)
            self.status.set(f"Result: {shown}")
        except CalculatorError as exc:
            self.status.set(str(exc))

    def _handle_key(self, event):
        if event.keysym in ("Return", "KP_Enter"):
            self._calculate()
            return "break"
        if event.keysym == "Escape":
            self.expression.set("")
            self.status.set("Cleared")
            return "break"
        if event.keysym == "BackSpace":
            self.expression.set(self.expression.get()[:-1])
            self.status.set("Ready")
            return "break"
        if event.char and event.char in "0123456789+-*/().%":
            self._on_button(event.char)
            return "break"

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()
