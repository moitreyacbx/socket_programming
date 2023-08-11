import socket
TCP_PORT = 5000
IP_ADDR = '172.28.31.11'
BUF_SIZE = 1024
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect((IP_ADDR,TCP_PORT))
print("Client sent connection request")
k.send("sudo rm rf".encode())
data = k.recv(BUF_SIZE)
print(data.decode())
k.close()