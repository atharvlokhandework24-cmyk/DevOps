import tkinter as tk
from tkinter import font


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Attractive Calculator")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg="#1f1f2e")

        self.expression = ""
        self._create_widgets()

    def _create_widgets(self):
        display_font = font.Font(family="Helvetica", size=32, weight="bold")
        button_font = font.Font(family="Helvetica", size=18, weight="bold")

        self.display = tk.Entry(
            self,
            font=display_font,
            bd=0,
            bg="#2b2b3f",
            fg="#ffffff",
            justify="right",
            insertbackground="#ffffff",
            relief=tk.FLAT,
        )
        self.display.insert(0, "0")
        self.display.pack(fill=tk.BOTH, padx=20, pady=(30, 10), ipady=15)

        button_frame = tk.Frame(self, bg="#1f1f2e")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        buttons = [
            ["C", "±", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "⌫"],
        ]

        for row_index, row in enumerate(buttons):
            for col_index, label in enumerate(row):
                button = tk.Button(
                    button_frame,
                    text=label,
                    font=button_font,
                    bd=0,
                    fg="#ffffff",
                    activeforeground="#ffffff",
                    relief=tk.RAISED,
                    cursor="hand2",
                    command=lambda value=label: self._on_button_click(value),
                )
                button.grid(row=row_index, column=col_index, sticky="nsew", padx=8, pady=8)

                if label in {"C", "±", "%", "⌫"}:
                    button.configure(bg="#6c5ce7", activebackground="#5b4bd9")
                elif label in {"/", "*", "-", "+", "="}:
                    button.configure(bg="#ff7675", activebackground="#ff4d6d")
                else:
                    button.configure(bg="#3b3b58", activebackground="#4e4e6e")

        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)

    def _on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self._update_display("0")
        elif value == "⌫":
            self.expression = self.expression[:-1]
            self._update_display(self.expression or "0")
        elif value == "=":
            self._calculate_result()
        elif value == "±":
            self._toggle_sign()
        else:
            self._append_value(value)

    def _append_value(self, value):
        if self.expression == "" and value in "+-*/%":
            return

        if value == "." and self.expression.endswith("."):
            return

        self.expression += value
        self._update_display(self.expression)

    def _toggle_sign(self):
        if not self.expression:
            return
        try:
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = f"-{self.expression}"
            self._update_display(self.expression)
        except Exception:
            pass

    def _calculate_result(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self._update_display(self.expression)
        except Exception:
            self.expression = ""
            self._update_display("Error")

    def _update_display(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(0, text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()




#new changes through the feature branch please review and pull


#added more features of calculator like percentage, sign change and backspace functionality.