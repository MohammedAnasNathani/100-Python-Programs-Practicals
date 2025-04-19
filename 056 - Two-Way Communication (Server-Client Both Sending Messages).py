import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for a connection...")
client_socket, client_address = server_socket.accept()

# Send message to client
message = "Hello from server!"
client_socket.send(message.encode())

# Receive message from client
client_message = client_socket.recv(1024).decode()
print(f"Client says: {client_message}")

client_socket.close()
server_socket.close()
