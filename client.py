import socket, sys
from pprint import pprint

#take command line input and save as variables
HOST = sys.argv[1]
PORT = int(sys.argv[2])
X_COORD = sys.argv[3]
Y_COORD = sys.argv[4]
BUFFER_SIZE = 1024

c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#initialize opponent board for each client
c1_opponent_board = [ (['_'] * 10) for i in range(10) ]
c2_opponent_board = c1_opponent_board
#print the board
# pprint(c1_opponent_board)
#simulate a move to test board structure and reprint
c1_opponent_board[4][4] = 'H'
# pprint(c1_opponent_board)
		

#code to write to file 

# filename1 = 'c1_opponent_board.txt'
# f = open(filename,'w')
# f.write()
# f.close()
# filename2 = 'c2_opponent_board.txt'
# f = open(filename,'w')
# f.write()
# f.close()


message = X_COORD + ' and ' + Y_COORD #send the x and y coordinates

#connect to the server
c1.connect((HOST, PORT))
print 'Client connecting'

#send the message to the server
c1.send(bytes(message))
print 'Client sending'

data = c1.recv(BUFFER_SIZE)
c1.close()  