from datetime import datetime
import socket
now = datetime.now()
TCP_PORT = 5000
IP_ADDR = '172.28.31.11'
BUF_SIZE = 1024
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server has created a port")
k.bind((IP_ADDR,TCP_PORT))
print("Server bound successfully")
k.listen(1)
con, addr = k.accept()
print("Connection address is ", addr)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
msg = "date and time: %s"%(dt_string)
msg = msg.encode()
con.send(msg)
con.close()