import socket
import subprocess
from sys import stdout

import settings
from db import check_username_password


def process_command(command: str) -> str:
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.stdout == "":
        if result.stderr == "":
            return "Invalid command"
        return result.stderr
    return result.stdout


def handle_client(client_socket: socket.socket) -> None:
    authorized = False
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            if authorized:
                result = process_command(request)
            else:
                username, password = request.split(":", 1)
                authorized = check_username_password(username, password)
                if authorized:
                    result = settings.SUCCESSFUL_LOGIN_CODE
                else:
                    result = settings.INVALID_LOGIN_CODE
            client_socket.send(result.encode("utf-8"))
        except (socket.error, IOError) as e:
            print(f"Socket error: {e}")
            break

def main() -> None:
    with socket.socket() as server_socket:
        server_socket.bind(("0.0.0.0", settings.CONNECTION_PORT))
        server_socket.listen(5)
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket)

if __name__ == "__main__":
    main()