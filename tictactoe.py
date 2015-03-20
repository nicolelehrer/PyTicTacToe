import random

# VARS
emptySpot = " - "
xPlayer = " X "
oPlayer = " O "  # length of emptySpot, xPlayer, oPlayer should have same character length for layout
move = "99"  # initial bogus value for debug
currentPlayer = xPlayer
winner = 0
message = 'Blank message'
emptySpots = []  # empty spots from which computer can select next move

noSolFlag = "na"

# make a list of lists to store the game
row0 = [emptySpot, emptySpot, emptySpot]
row1 = [emptySpot, emptySpot, emptySpot]
row2 = [emptySpot, emptySpot, emptySpot]
gridSpots = [row0, row1, row2]
# gridSpots[row][col] just access it like a 2d array


# FUNCTIONS
def updateDisplay():
    spacer = " " * len(xPlayer)
    colHeading = spacer + '0' + spacer + '1' + spacer + '2'
    print('\n'+colHeading)
    for row in range(0, 3):
        gameboard = str(row) + ' ' + (str(gridSpots[row][0])+' '+str(gridSpots[row][1])+' '+str(gridSpots[row][2]))
        print gameboard


def returnNextPlayer(aPlayer):
    if aPlayer == xPlayer:
        return oPlayer
    else:
        return xPlayer


def translateInput(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    gridSpots[indexRow][indexCol] = currentPlayer


def spotsStillFree(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    if gridSpots[indexRow][indexCol] == emptySpot:
        return True
    else:
        return False


def inputIsValid(aMove):
    # length
    if len(aMove)!=2:
        return False
    # range, type
    chars = set('012')
    if aMove[0] not in chars or aMove[1] not in chars:
        return False
    return True


def compareThree(var1, var2, var3):
    if var1 != emptySpot and var1 == var2 and var1 == var3:
        return True
    else:
        return False


def evalGameBoard():
    for count in range(0, 3):	
        aRowResult = compareThree(gridSpots[count][0], gridSpots[count][1], gridSpots[count][2])
        aColResult = compareThree(gridSpots[0][count], gridSpots[1][count], gridSpots[2][count])
        if aRowResult or aColResult:
            return True
    lDiagResult = compareThree(gridSpots[0][0], gridSpots[1][1], gridSpots[2][2])
    rDiagResult = compareThree(gridSpots[0][2], gridSpots[1][1], gridSpots[2][0])
    if lDiagResult or rDiagResult:
        return True


def noMovesLeft():
    for countRow in range(0, 3):
        for countCol in range(0, 3):
            if gridSpots[countRow][countCol] == emptySpot:
                return False
    return True

# ---------------------------------------------------

    
# (1)choose an empty random spots
def identifyEmptySpots(computerPlayer):
    for countRow in range(0, 3):
        for countCol in range(0, 3):
            if gridSpots[countCol][countRow] == emptySpot:
                emptySpots.append(str(countCol)+str(countRow))
    print(random.choice(emptySpots))
    return random.choice(emptySpots)
   
   
# (3)add some strategy
def compareToWin(var1, var2, var3, aPlayer):
    holder = [var1, var2, var3]    
    if holder.count(aPlayer) == 2 and holder.count(emptySpot) == 1:  # if two instances of current player and 1 empty
        index = holder.index(emptySpot)
        print('spot to win is '+str(index))
        return index
    return noSolFlag


def recommendNextMove(aCurrentPlayer):        
    for count in range(0, 3):	
        aRecCol = compareToWin(gridSpots[count][0], gridSpots[count][1], gridSpots[count][2], aCurrentPlayer)
        aRecRow = compareToWin(gridSpots[0][count], gridSpots[1][count], gridSpots[2][count], aCurrentPlayer)
        if aRecRow != noSolFlag:
            computerAnswer = str(aRecRow)+str(count)
            print(computerAnswer)
            return computerAnswer
        elif aRecCol != noSolFlag:
            computerAnswer = str(count)+str(aRecCol)
            print(computerAnswer)
            return computerAnswer
    aRecLDiag = compareToWin(gridSpots[0][0], gridSpots[1][1], gridSpots[2][2], aCurrentPlayer)
    if aRecLDiag != noSolFlag:
        computerAnswer = str(aRecLDiag)+str(aRecLDiag)
        print(computerAnswer)
        return computerAnswer
    aRecRDiag = compareToWin(gridSpots[0][2], gridSpots[1][1], gridSpots[2][0], aCurrentPlayer)
    if aRecRDiag != noSolFlag:
        computerAnswer = str(aRecRDiag)+str(2-aRecRDiag)
        print(computerAnswer)
        return  computerAnswer
    return noSolFlag
# ---------------------------------------------------

# MAIN LOOP
while winner == 0:
    
    updateDisplay()
    
    print '\nCurrent player is '+currentPlayer+'\nEnter your move as a combination of first a row number and then a column number, like 00 or 12'

    # move = raw_input('--> ')
    
    # (2)add a way for you to know who is proving input
    if currentPlayer == xPlayer:
        move = raw_input('--> ')
    else:
        if recommendNextMove(currentPlayer) != noSolFlag:
            print("strategic")
            move = recommendNextMove(currentPlayer)
        else:
            print("random")
            move = identifyEmptySpots(currentPlayer)


    if inputIsValid(move):
        if spotsStillFree(move):
            translateInput(move)
            shouldUpdatePlayer = True
        else:
            message = '\n----spot taken - choose another spot----'
            shouldUpdatePlayer = False
    else:
        message = '\n----input is not valid-----'
        shouldUpdatePlayer = False
        
    if evalGameBoard() == 1:
        updateDisplay()
        print("\nWINNER IS" + currentPlayer + "!!! END OF GAME\n")
        winner = 1
        break

    if noMovesLeft():
        updateDisplay()
        print('\nNO WINNER. END OF GAME\n')
        winner = 1
        break
   
    if shouldUpdatePlayer:
        currentPlayer = returnNextPlayer(currentPlayer)
    else:       
        print(message)