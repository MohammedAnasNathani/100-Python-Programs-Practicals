import ssl
import socket

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Waiting for a secure connection...")
secure_socket = context.wrap_socket(server_socket, server_side=True)
client_socket, client_address = secure_socket.accept()
print(f"Secure connection established with {client_address}")

message = "Hello, secure client!"
client_socket.send(message.encode())
client_socket.close()
secure_socket.close()
