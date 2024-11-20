import socket


def send_request(client_socket: socket.socket, request: str) -> str:
    client_socket.send(request.encode("utf-8"))
    data = client_socket.recv(1024).decode("utf-8")
    return data
