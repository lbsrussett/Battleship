

import socket, sys
from pprint import pprint
import requests 

def updateOpponentBoard(result, position):
    opponentBoard = loadBoard("opponent_board.txt")
    if(result == "I"):
        print("Wrong")
    else:
        opponentBoard[int(position[0])][int(position[1])] = result
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
            line += board[x][y]
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
ENDPOINT = "http://127.0.0.1:" + str(PORT) + '/post'


c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the server
c1.connect((HOST, PORT))

#format for sending coordinate data in http post request
payload = { 'x': X_COORD, 'y' : Y_COORD }

#post request to http server - response should be returned in fire variable
#there is something wrong with this, as the result never gets returned
fire = requests.post(ENDPOINT, data=payload)
print 'sent fire message'
#if a response is received, should be able to print its text with this command
print fire.text

#send the message to the server
# c1.send(bytes(fire))

# result = c1.recv(BUFFER_SIZE)
# print result.text
# print data + ' and received by client'
c1.close()

position = [X_COORD, Y_COORD]
updateOpponentBoard(result, position)
    
