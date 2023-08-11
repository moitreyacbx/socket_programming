import socket
TCP_PORT = 5050
IP_ADDR = '172.28.31.11'
BUF_SIZE = 1024
exp = input("Enter integer arithmetic expression:")
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect((IP_ADDR,TCP_PORT))
print("Client sent connection request")
k.send(exp.encode())
res = k.recv(BUF_SIZE)
print(res.decode())
k.close()