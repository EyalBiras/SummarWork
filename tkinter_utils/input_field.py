import tkinter as tk

class InputField(tk.Frame):
    def __init__(self, master, label_text: str) -> None:
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text=label_text, font=('Helvetica', 16))
        self.entry = tk.Entry(self, textvariable=tk.StringVar())


    def pack(self) -> None:
        self.label.pack()
        self.entry.pack()
        super().pack()

    @property
    def value(self) -> str:
        return self.entry.get()
