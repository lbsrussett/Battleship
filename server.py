import socket
import sys
from pprint import pprint

BUFFER_SIZE = 1024
#retrieve port and board inputs from command line
port = sys.argv[1]
own_board = sys.argv[2]

#initialize sockets for servers
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#stopgap to allow server to run on 'any available resource' - need to figure out IP address
HOST = '127.0.0.1'   
PORT = int(port)

with open(own_board) as f:
    data = f.readlines()

# for d in data:
# 	list(d)
# 	print d + '\r\n'
#bind first server to socket
s1.bind((HOST, PORT))
# print 'Successfully connected to: ' + str(PORT)

s1.listen(10)

#create listening connection to receive data from client
conn, addr = s1.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
data = conn.recv(BUFFER_SIZE)
if data:
	print data
else:
	print 'no data'

reply = 'Successfully sent from server'
conn.send(reply)
# conn.close()

#need logic to take data from client side to interact with battleship game
#need to update own_board based on game logic

