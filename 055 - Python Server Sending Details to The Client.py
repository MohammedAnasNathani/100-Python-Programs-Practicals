import socket

# Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

message = "Hello, client! I am the server."
client_socket.send(message.encode())
client_socket.close()
server_socket.close()
