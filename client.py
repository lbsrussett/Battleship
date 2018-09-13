import socket, sys
from pprint import pprint

def updateOpponentBoard(result, position):
    opponentBoard = loadBoard("opponent_board.txt")
    if(result == "I"):
        print("Wrong")
    else:
        opponentBoard[position[x]][position[y]] = result
    saveBoard("opponent_board.txt",opponentBoard)

def loadBoard(fileName):
    board = [] #representation of where my battleships are and which have been hit
    line = []
    file = open(fileName,"r")
    for x in range(10):
        line = file.readline()
        lineList = list(line)
        board.append(lineList)#add line to board
    file.close()
    return board

def saveBoard(fileName, board):
    file = open(fileName,"w")
    for x in range(10):
        line = ""
        for y in range(10):
            line += opponentBoard[x][y]
        line+="\n"
        file.write(line)
    file.close()
    return board

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
c2_opponent_board = [ (['_'] * 10) for i in range(10) ]
#print the board
pprint(c1_opponent_board)

#update opponents board based on result


	

#code to write to file - needs to be updated to read current state of board before changing
filename1 = 'c1_opponent_board.txt'
c1b = str(c1_opponent_board)
f = open(filename1,'w')
f.write(c1b)
f.close()
filename2 = 'c2_opponent_board.txt'
c2b = str(c2_opponent_board)
f = open(filename2,'w')
f.write(c2b)
f.close()


message = X_COORD + ',' + Y_COORD #send the x and y coordinates

#connect to the server
c1.connect((HOST, PORT))

#send the message to the server
c1.send(bytes(message))

result = c1.recv(BUFFER_SIZE)
print data + ' and received by client'
c1.close()

position = [X_COORD, Y_COORD]
updateOpponentBoard(result, position)
    
