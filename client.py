import tkinter as tk
import socket
import settings
from login import Login
from remote_cli import RemoteCLI


class Client(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Application")
        self.geometry(f"{settings.WINDOW_WIDTH}x{settings.WINDOW_HEIGHT}")
        self.resizable(False, False)

        self.socket = socket.socket()
        self.socket.connect((settings.SERVER_IP, settings.CONNECTION_PORT))

        self.remote_cli_page = RemoteCLI(self.socket)
        self.login_page = Login(next_page=self.remote_cli_page, client_socket=self.socket)


        self.login_page.pack()
        self.mainloop()

if __name__ == '__main__':
    a = Client()

