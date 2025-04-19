import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for a connection...")
client_socket, client_address = server_socket.accept()

with open('received_file.txt', 'wb') as f:
    print("Receiving file...")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully.")
client_socket.close()
server_socket.close()