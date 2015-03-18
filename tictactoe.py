# VARS
emptySpot = " - "
xPlayer = " X "
oPlayer = " O "
move = "99"
currentPlayer = xPlayer
winner = 0
message = 'Blank message'

# make a list to store the game
row0 = [emptySpot, emptySpot, emptySpot]
row1 = [emptySpot, emptySpot, emptySpot]
row2 = [emptySpot, emptySpot, emptySpot]
gridSpots = [row0, row1, row2]
# gridSpots[row][col] just access it like a 2d array


# FUNCTIONS
# extra '\' let's you put code on multiple lines
def updateDisplay():
    gameboard = '   0   1   2 \n0 '+str(gridSpots[0][0])+' '+str(gridSpots[0][1])+' '+str(gridSpots[0][2]) + \
                        '\n1 '+str(gridSpots[1][0])+' '+str(gridSpots[1][1])+' '+str(gridSpots[1][2]) + \
                        '\n2 '+str(gridSpots[2][0])+' '+str(gridSpots[2][1])+' '+str(gridSpots[2][2])
    print '\n'+gameboard+'\n'


def returnNextPlayer(aPlayer):
    if aPlayer == xPlayer:
        return oPlayer
    else:
        return xPlayer


def translateInput(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    gridSpots[indexRow][indexCol] = currentPlayer


def spotFree(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    if gridSpots[indexRow][indexCol] == " - ":
        return True
    else:
        return False


def inputIsValid(aMove):
    # length
    if len(aMove)!=2:
        return False
    # 'range'
    chars = set('012')
    if aMove[0] not in chars or aMove[1] not in chars:
        return False
    return True


def compareThree(var1, var2, var3):
    if var1 != emptySpot:
        if var1 == var2 and var1 == var3:
            return 1
        else:
            return 0
    else:
        return 0


def checkGrid():
    for count in range(0, 3):	
        aRowResult = compareThree(gridSpots[count][0], gridSpots[count][1], gridSpots[count][2])
        aColResult = compareThree(gridSpots[0][count], gridSpots[1][count], gridSpots[2][count])
        if aRowResult or aColResult == 1:
            return 1
    lDiagResult = compareThree(gridSpots[0][0], gridSpots[1][1], gridSpots[2][2])
    rDiagResult = compareThree(gridSpots[0][2], gridSpots[1][1], gridSpots[2][0])
    if lDiagResult or rDiagResult == 1:
        return 1


def noMovesLeft():
    for countRow in range(0, 3):
        for countCol in range(0, 3):
            if gridSpots[countRow][countCol] == emptySpot:
                return False
    return True

# ---------------------------------------------------

    
# (1)identify empty spots
def identifyEmptySpots(computerPlayer):
    for countRow in range(0, 3):
        for countCol in range(0, 3):
            # if gridSpots[countRow][countCol] == emptySpot:
            if gridSpots[countCol][countRow] == emptySpot:
                # computerAnswer = str(countRow)+str(countCol)
                computerAnswer = str(countCol)+str(countRow)
                return computerAnswer
   
   
# (3)add some strategy
def compareToWin(var1, var2, var3, aPlayer):
    holder = [var1, var2, var3]    
    if holder.count(aPlayer) == 2:  # if there are two instances of the current player
        if holder.count(emptySpot) == 1:  # and a free spot to move to
            col = holder.index(emptySpot)
            print('spot to win is '+str(col))
            return col           
    return 99


def recommendNextMove(aCurrentPlayer):        
    for count in range(0, 3):	
        aRow = compareToWin(gridSpots[count][0], gridSpots[count][1], gridSpots[count][2], aCurrentPlayer)
        aCol = compareToWin(gridSpots[0][count], gridSpots[1][count], gridSpots[2][count], aCurrentPlayer)

        if aCol != 99:
            computerAnswer = str(aCol)+str(count)
            print(computerAnswer)
            return computerAnswer
        elif aRow != 99:
            computerAnswer = str(count)+str(aRow)
            print(computerAnswer)
            return computerAnswer
        else:
            return 99
        
# ---------------------------------------------------

# MAIN LOOP
while winner == 0:
    
    updateDisplay()
    
    print '\ncurrent player is '+currentPlayer+'\nenter your move as a combination of first a row number and then a column number, like 00 or 12'

    # move = raw_input('--> ')
    
    # (2)add a way for you to know who is proving input
    if currentPlayer == xPlayer:
        move = raw_input('--> ')
    else:
        if recommendNextMove(currentPlayer) != 99:
            move = recommendNextMove(currentPlayer)
        else:
            move = identifyEmptySpots(currentPlayer)


    if inputIsValid(move):
        if spotFree(move):
            translateInput(move)
            shouldUpdatePlayer = True
        else:
            message = '\n----spot taken - choose another spot----'
            shouldUpdatePlayer = False
    else:
        message = '\n----input is not valid-----'
        shouldUpdatePlayer = False
        
    if checkGrid() == 1:
        updateDisplay()
        print("\nWINNER IS" + currentPlayer + "!!! END OF GAME")
        winner = 1
        break

    if noMovesLeft():
        updateDisplay()
        print('\nNO WINNER. END OF GAME')
        winner = 1
        break
   
    if shouldUpdatePlayer:
        currentPlayer = returnNextPlayer(currentPlayer)
    else:       
        print(message)