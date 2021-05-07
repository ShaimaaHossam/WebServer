import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 12345
filename ="/HelloWorld.html"
header=f"GET {filename} HTTP/1.1\r\nHost: localhost:12345\r\n"
clientSocket.connect((host, port))
clientSocket.send(header.encode())
rec = clientSocket.recv(2048).decode()

# display the response
print(rec)
data = []
message = clientSocket.recv(2048).decode()
if message:
    data.append(message)

for d in data:
    print(d)
