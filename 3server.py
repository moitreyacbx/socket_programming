import socket
 
IP_ADDR = "127.0.0.1"
UDP_Port = 20001
BUF_SIZE = 1024
 
k = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
k.bind((IP_ADDR, UDP_Port))
print("UDP server up and listening")
f = open("address.txt")
while True:
	name, addr1 = k.recvfrom(BUF_SIZE)
	name = name.decode()
	msg = ''
	flag=False
	for x in f:
		d=x.split(":")
		if d[0]==name:
			msg=x[1]
			flag=True
			
