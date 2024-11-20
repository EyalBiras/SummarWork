import tkinter as tk
import socket
from ast import Param
from modulefinder import Module

import settings
from tkinter_utils.input_field import InputField
from utils import send_request

class Login(tk.Frame):
    def __init__(self, next_page: tk.Frame, client_socket: socket.socket) -> None:
        super().__init__()
        self.title_variable = tk.StringVar(value="Login")
        self.title_label = tk.Label(
            self,
            textvariable=self.title_variable,
            fg="#FFFFFF",
            bg="#4A4A4A",
            relief=tk.RAISED,
            borderwidth=22,
            font=('Helvetica', 24),
            padx=100
        )

        self.user_name = InputField(master=self, label_text="Username")
        self.password = InputField(master=self, label_text="Password")

        self.login_button = tk.Button(
            self,
            text="Login",
            command=self.login,
            bg="#007BFF",
            fg="white",
            font=('Helvetica', 10),
            padx=20,
            pady=5,
            relief=tk.RAISED,
            borderwidth=6
        )

        self.retry_label = tk.Label(
            self,
            text="Invalid credentials. Please try again.",
            fg="red",
            font=('Helvetica', 10),
            padx=10,
            pady=5
        )

        self.next_page = next_page

        self.client_socket = client_socket


    def login(self) -> None:
        username = self.user_name.value
        password = self.password.value
        result = send_request(client_socket=self.client_socket, request=f"{username}:{password}")
        if result == settings.SUCCESSFUL_LOGIN_CODE:
            self.destroy()
            self.next_page.pack()
        else:
            self.retry_label.pack()

    def pack(self) -> None:
        self.place(x=settings.WINDOW_WIDTH//4, y=0, width=400, height=400)
        self.title_label.pack()
        self.user_name.pack()
        self.password.pack()
        self.login_button.pack()




