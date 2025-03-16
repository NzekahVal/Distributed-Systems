import socket

# Server setup
host = '127.0.0.1'  # Localhost
port = 12345  # Port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)  # Allow 1 client

print(f"Server started on {host}:{port}. Waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    message = conn.recv(1024).decode()
    if message.lower() == "exit":
        print("Client disconnected.")
        break
    print(f"Client: {message}")
    response = input("Server: ")
    conn.send(response.encode())

conn.close()
server_socket.close()
