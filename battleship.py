from __future__ import print_function #to be able to print without a new line




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

#Loop through board to print its values
def printBoard(board):
    print("  A B C D E F G H I J")
    for x in range(10):
        print(x,end='')
        for y in range(10):
            print(" " + opponentBoard[x][y], end='') #print without a new line
        print()

#gets input and returns and array of format [letter, number] (both strings)
def getInput():
    print('Letter Component (A-J): ', end='')
    rawLetter = input()
    letter = rawLetter.upper() #Always converts letter to uppercase
    print('Number Component (0-9): ', end='')
    number = input()
    guess = [letter, number]
    return guess

#makes sure letter is A-J and number is 0-9
def validateInput():
    letter = guess[0]
    number = guess[1]
    if(letter < 'A' or letter > 'J' or int(number) < 0 or int(number) > 9):
        return False
    return True

def convertInputToInt(guess):
    yChr = list(guess[0])[0]  #Convert letter to char
    y = ord(yChr)-65 #Converts char to number
    x = int(guess[1])
    intGuess = [x, y]
    return intGuess

def updateOpponentBoard(guess, opponentBoard):
    intGuess = convertInputToInt(guess)
    x = intGuess[0]
    y = intGuess[1]
    boardValue = opponentBoard[x][y]
    if(boardValue == "H" or boardValue == "M"): #Check for repeats
        return "Invalid"
    elif(boardValue == "B"): #Battleship
        opponentBoard[x][y] = "H"
        return "B"
    elif(boardValue == "D"): #Destoryer
        opponentBoard[x][y] = "H"
        return "D"
    elif(boardValue == "C"): #Carrier
        opponentBoard[x][y] = "H"
        return "C"
    elif(boardValue == "S"): #Sub
        opponentBoard[x][y] = "H"
        return "S"
    elif(boardValue == "R"): #cRuiser
        opponentBoard[x][y] = "H"
        return "R"
    else: #Blank
        opponentBoard[x][y] = 'M'
        return 'M'


opponentBoard = loadBoard("opponent_board.txt")
printBoard(opponentBoard)
guess = getInput()
if(validateInput()):
    #x,y coordinates: print(convertInputToInt(guess)[0], convertInputToInt(guess)[1])
    boardValue = updateOpponentBoard(guess, opponentBoard)
    if(boardValue == 'Invalid'):
        print("Already Guessed There Ya Silly Goose")
    else:
        if(boardValue == 'M'):
            print("Miss")
        printBoard(opponentBoard)
        saveBoard("own_board copy.txt",opponentBoard)
else:
    print("A-J, 0-9, is it really that hard?")
