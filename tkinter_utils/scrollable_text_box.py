import tkinter as tk


class ScrollableTextBox(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.text_box = tk.Text(self, wrap=tk.WORD)

        self.vertical_scroll = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text_box.yview)

        self.horizontal_scroll = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.text_box.xview)

        self.text_box.config(yscrollcommand=self.vertical_scroll.set, xscrollcommand=self.horizontal_scroll.set)

    def pack(self) -> None:
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vertical_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.horizontal_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        super().pack()

