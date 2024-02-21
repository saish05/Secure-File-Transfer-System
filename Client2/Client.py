import socket
import threading

host = "127.0.0.1"
port = 12345

size = 1024


def split_frame(frame):
    chunks = []
    offset = 0
    while offset < len(frame):
        
        chunk_length = int.from_bytes(frame[offset : offset + 4], "big")
        offset += 4
        chunk = frame[offset : offset + chunk_length]
        offset += chunk_length
        chunks.append(chunk)

    return chunks

def receive_messages(client_socket):
    while True:
        while True:
            frame = client_socket.recv(size + 8)
            if not frame:
                break
            header, data = split_frame(frame)
            to_username, file_name = header.decode().split(":")
            name, extension = file_name.split(".")
            file_name = f"{name}_{to_username}.{extension}"
            with open(file_name, "ab") as file:
                file.write(data)


def send_messages(client_socket):
    while True:
        header = input()
        to_username, file_name = header.split(":")
        header = header.encode()
        read_size = size - len(header)
        with open(file_name, "rb") as file:
            while True:
                data = file.read(read_size)
                if not data:
                    break
                frame1 = len(header).to_bytes(4, "big") + header
                frame2 = len(data).to_bytes(4, "big") + data
                frame = frame1 + frame2
                client_socket.send(frame)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Connected to the server.")


client_name = input("Enter user_name: ")
client_socket.send(client_name.encode())
print("Usage: <receiver_username>:<file_name>")


receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()


send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()

