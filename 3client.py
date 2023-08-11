import socket
name = input("Enter student name")
d = name.encode()
serverAddrPort = ("127.0.0.1", 20001)
BUF_SIZE = 1024
k = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
k.sendto(d, serverAddrPort)
res = k.recvfrom(BUF_SIZE)
print(res.decode())