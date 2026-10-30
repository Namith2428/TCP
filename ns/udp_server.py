import socket

SERVER_HOST = ""        # "" = accept messages from any device on the network
SERVER_PORT = 12000     # The port your phone will send to

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"[SERVER] Listening on UDP port {SERVER_PORT}...")

while True:
    data, client_address = server_socket.recvfrom(2048)
    message = data.decode()
    print(f"[SERVER] Received from {client_address}: {message}")

    reply = message.upper()
    server_socket.sendto(reply.encode(), client_address)
    print(f"[SERVER] Sent back: {reply}")