import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

with open('file_to_send.txt', 'rb') as f:
    print("Sending file...")
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.send(data)

print("File sent successfully.")
client_socket.close()
