import socket, sys, httplib
import urllib, ast, webbrowser

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

def getShip(hit):
	if hit == 'B':
		return 'Battleship'
	elif hit == 'C':
		return 'Carrier'
	elif hit == 'D':
		return 'Destroyer'
	elif hit == 'R':
		return 'Cruiser'
	elif hit == 'S':
		return 'Submarine'
	else:
		return 'Big Oops'

#take command line input and save as variables
HOST = sys.argv[1]
PORT = int(sys.argv[2])
X_COORD = sys.argv[3]
Y_COORD = sys.argv[4]
BUFFER_SIZE = 1024
ENDPOINT = "127.0.0.1:" + str(PORT)
#format for sending coordinate data in http post request
payload = urllib.urlencode({ 'x': X_COORD, 'y' : Y_COORD })  
#create a connection  
conn = httplib.HTTPConnection(ENDPOINT)  

#request command to server  
conn.request('POST', '/fire', payload)  
  
#get response from server  
resp = conn.getresponse()  

#print server response and data  
print(resp.status, resp.reason)  
data_received = resp.read() 


#take string response and convert back to dictionary of results
resp = ast.literal_eval(data_received)
position = [X_COORD, Y_COORD]

#conditions to determine results of fire message
if resp['sink='] == 'T':
	result = resp['hit=']
	ship = getShip(result)
	updateOpponentBoard(result, position)
	print 'You sunk the ' + ship + '!'
elif resp['sink='] == 'F':
	result = resp['hit=']
	ship = getShip(result)
	updateOpponentBoard(result, position)
	print 'You hit the ' + ship + '!'
else:
	print 'You got no results'

cmd = raw_input('Please enter own or opp to view board): ')   
param = urllib.urlencode({ 'key' : cmd})
if cmd == 'own':
	conn.request('GET', '/own_board', param)
elif cmd == 'opp':
	conn.request('GET', '/opponent_board.html', param)

r = conn.getresponse()
print r.read()
conn.close()
    
