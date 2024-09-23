import socket
import threading

HOST = "127.0.0.1"
PORT = 12345


def receive_message(connection: socket.socket) -> None:
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break


def send_message(connection: socket.socket, username: str) -> None:
    while True:
        message = input()
        if message == "/exit":
            break
        full_message = f"{username}: {message}"
        connection.sendall(full_message.encode())
    connection.close()


username = input("Enter your name: ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=receive_message, args=(s,), daemon=True).start()
    send_message(s, username)
