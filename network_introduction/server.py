import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

clients = set()
clients_lock = threading.Lock()


def handle_client(connection: socket.socket, address: tuple[str, int]) -> None:
    with connection:
        print(f'New connection from {address}')
        with clients_lock:
            clients.add(connection)
        try:    
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f'{address}: {data.decode()}')
                message_sender(data.decode(), connection)
        finally:
            with clients_lock:
                clients.remove(connection)
            print(f'Connection {address} closed')


def message_sender(message: str, sender_connection: socket.socket) -> None:
    with clients_lock:
        for client in clients:
            if client != sender_connection:
                client.sendall(message.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server started on {HOST}:{PORT}')
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
