import tkinter as tk
import socket

import settings
from tkinter_utils.scrollable_text_box import ScrollableTextBox
from utils import send_request


class RemoteCLI(tk.Frame):
    def __init__(self, client_socket: socket.socket) -> None:
        super().__init__()
        self.client_socket = client_socket

        self.title_variable = tk.StringVar(value="Remote CMD")
        self.title_label = tk.Label(textvariable=self.title_variable, fg="#FFFFFF", bg="#2E2E2E", relief=tk.RAISED,
                                    borderwidth=20, font=('Helvetica', '30'))
        self.command_area = ScrollableTextBox(self)
        self.command_insert = tk.Entry(self)
        self.insert_button = tk.Button(self, text="Send", command=self.run_command)


    def run_command(self) -> None:
        command = self.command_insert.get()
        if command:
            data = send_request(client_socket=self.client_socket, request=command)
            self.command_area.text_box.insert(tk.END, f"{command}\n{data}\n")


    def pack(self) -> None:
        self.place(x=settings.WINDOW_WIDTH//4, y=settings.WINDOW_HEIGHT//8, width=425, height=423)
        self.title_label.pack()
        self.command_area.pack()
        self.command_insert.pack()
        self.insert_button.pack()
