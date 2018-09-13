import socket
import sys

port = sys.argv[1]
own_board = sys.argv[2]

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''   
PORT = int(port)

ip_address = socket.gethostbyname(HOST)
print HOST

s1.bind((HOST, PORT))
s1.listen(1)

conn.addr = s1.accept()
data = conn.recv(BUFFER_SIZE)
conn.send(data)
conn.close()
