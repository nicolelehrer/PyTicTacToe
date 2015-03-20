import random

# VARS
emptySpot = " - "
xPlayer = " x "
oPlayer = " o "  # length of emptySpot, xPlayer, oPlayer should have same character length for layout
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




# want to find a patter of two of one and one of the other
# relevant inputs are one player type (for win or block) and one empty space
# or two empty spaces and one player type
# check for win (2 of current and 1 empty - you want to return the empty
# check for block (2 of opponent and 1 empty - "
# check fro duo 2 of empty and one current - you want to return the empty you always want tor return the empty


# (1)choose an empty random spots
#  -- this can be extended to choose the best spot, ie middle one then corners then anything else
def pickRandomEmptySpot(computerPlayer):
    for countRow in range(0, 3):
        for countCol in range(0, 3):
            if gridSpots[countCol][countRow] == emptySpot:
                emptySpots.append(str(countCol)+str(countRow))
    print(random.choice(emptySpots))
    return random.choice(emptySpots)


def searchListForTwoAndOne(aListOfThree, typeTwo, typeOne):
    if aListOfThree.count(typeOne) == 1 and aListOfThree.count(typeTwo) == 2:
        return aListOfThree.index(emptySpot) # you always want to return the empty spot index
    return noSolFlag


def searchGridForTwoAndOne(typeTwo, typeOne):

    for count in range(0, 3):

        aRow = gridSpots[count][0], gridSpots[count][1], gridSpots[count][2]
        aCol = gridSpots[0][count], gridSpots[1][count], gridSpots[2][count]

        colIndex = searchListForTwoAndOne(aRow, typeTwo, typeOne)
        if colIndex != noSolFlag:
            return str(count)+str(colIndex)

        rowIndex = searchListForTwoAndOne(aCol, typeTwo, typeOne)
        if rowIndex != noSolFlag:
            return str(rowIndex)+str(count)

    leftDiag = [gridSpots[0][0], gridSpots[1][1], gridSpots[2][2]]
    rightDiag = [gridSpots[0][2], gridSpots[1][1], gridSpots[2][0]]

    lDiagIndex = searchListForTwoAndOne(leftDiag, typeTwo, typeOne)
    if lDiagIndex != noSolFlag:
        return str(lDiagIndex)+str(lDiagIndex)

    rDiagIndex = searchListForTwoAndOne(rightDiag, typeTwo, typeOne)
    if rDiagIndex !=noSolFlag:
        return str(rDiagIndex)+str(2-rDiagIndex)

    return noSolFlag

def returnMoveForComputer(aPlayer):

    moveForWin = searchGridForTwoAndOne(currentPlayer, emptySpot)
    if moveForWin != noSolFlag:
        print("strategic WIN")
        return moveForWin

    moveForBlock = searchGridForTwoAndOne(returnNextPlayer(currentPlayer), emptySpot)
    if moveForBlock != noSolFlag:
        print("strategic BLOCK")
        return moveForBlock

    moveForMakeTwo = searchGridForTwoAndOne(emptySpot, currentPlayer)
    if moveForMakeTwo != noSolFlag:
        print("strategic DUO")
        return moveForMakeTwo

    moveRandom = pickRandomEmptySpot(currentPlayer)
    print("random")
    return moveRandom


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
       move = returnMoveForComputer(currentPlayer)

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