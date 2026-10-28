
import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("TCP server started on port", PORT)
print("Waiting for Android client...")

try:
    while True:
        conn, addr = server.accept()
        print("Android connected:", addr)

        with conn:
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode("utf-8")
                print("Phone:", message)

                reply = "Laptop received: " + message
                conn.sendall(reply.encode("utf-8"))
                print("Sent:", reply)

except KeyboardInterrupt:
    print("Server stopped")
finally:
    server.close()
