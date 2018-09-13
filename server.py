import socket
import sys

#retrieve port and board inputs from command line
port = sys.argv[1]
own_board = sys.argv[2]

#initialize sockets for servers
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#stopgap to allow server to run on 'any available resource' - need to figure out IP address
HOST = ''   
PORT = int(port)

ip_address = socket.gethostbyname(HOST)
print HOST

#bind first server to socket
s1.bind((HOST, PORT))
s1.listen(1)

#create listening connection to receive data from client
conn, addr = s1.accept()
data = conn.recv(BUFFER_SIZE)
conn.send(data)
conn.close()

#need logic to take data from client side to interact with battleship game
#need to update own_board based on game logic

