import socket
import threading
import logging

HOST = "127.0.0.1"
PORT = 12345

clients = set()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%d.%m.%Y %H:%M:%S"
)


def handle_client(connection: socket.socket, address: tuple[str, int]) -> None:
    with connection:
        logging.info(f"New connection from {address}")
        clients.add(connection)
        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                logging.info(f"{address}: {data.decode()}")
                message_sender(data.decode(), connection)
        finally:
            clients.remove(connection)
            logging.info(f"Connection {address} closed")


def message_sender(message: str, sender_connection: socket.socket) -> None:
    for client in clients:
        if client != sender_connection:
            client.sendall(message.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    logging.info(f"Server started on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
