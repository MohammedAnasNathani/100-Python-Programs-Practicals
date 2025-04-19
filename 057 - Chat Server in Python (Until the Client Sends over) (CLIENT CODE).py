import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Receive message from server
server_message = client_socket.recv(1024).decode()
print(f"Server says: {server_message}")

# Send message to server
message = "Hello from client!"
client_socket.send(message.encode())

client_socket.close()
