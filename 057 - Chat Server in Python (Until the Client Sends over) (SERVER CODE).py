import socket

# Set up the server to listen on localhost and port 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for a connection...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established!")

# Send an initial message to the client
client_socket.send("Welcome to the server!".encode())

# Keep receiving and responding to messages until 'over' is sent
while True:
    # Receive message from the client
    message = client_socket.recv(1024).decode()
    if message.lower() == 'over':
        print("Client has sent 'over'. Closing connection.")
        break

    print(f"Received from client: {message}")

    # Send a response to the client
    response = "Message received!"
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
