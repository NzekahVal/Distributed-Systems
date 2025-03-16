import socket

# Server details
host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Connected to the server. Type 'exit' to quit.")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

client_socket.close()
