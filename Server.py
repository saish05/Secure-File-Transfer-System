
import socket
import threading


host = "127.0.0.1"
port = 12345


size = 1024


def split_frame(frame):
    chunk_length = int.from_bytes(frame[0:4], "big")
    header = frame[4 : 4 + chunk_length]
    return header


def handle_client(client_socket, client_address, clients):
    while True:
        while True:
            frame = client_socket.recv(size + 8)
            if not frame:
                break
            header = split_frame(frame).decode()
            to_username, file_name = header.split(":")
            clients[to_username].send(frame)




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")


clients = {}

while True:
    
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_name = client_socket.recv(size).decode()
    clients[client_name] = client_socket
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address, clients)
    )
    client_thread.start()
