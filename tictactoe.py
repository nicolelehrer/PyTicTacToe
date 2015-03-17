#inits
#vars
empt = " - "
move = "99"
currentPlayer = ' X '
winner = 0;
message = 'Blank message'

#make a list to store the game

row0 = [empt, empt, empt]
row1 = [empt, empt, empt]
row2 = [empt, empt, empt]

#row[row, col]
gridSpots = [row0, row1, row2]

#extra '\' let's you put code on multiple lines
def updateDisplay():
    gameboard = '   0   1   2 \n0 '+str(gridSpots[0][0])+' '+str(gridSpots[0][1])+' '+str(gridSpots[0][2])+\
                        '\n1 '+str(gridSpots[1][0])+' '+str(gridSpots[1][1])+' '+str(gridSpots[1][2])+\
                        '\n2 '+str(gridSpots[2][0])+' '+str(gridSpots[2][1])+' '+str(gridSpots[2][2])
    print '\n'+gameboard+'\n'
    
    
def returnNextPlayer(aCurrentPlayer):
    if aCurrentPlayer == ' X ':
        return ' O '
    else:
        return ' X '

def translateInput(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    if gridSpots[indexRow][indexCol] == " - ":
         gridSpots[indexRow][indexCol] = currentPlayer
         return True
    else:
        return False


def compareThree(var1, var2, var3):
	if var1 == " X " or var1 == " O ": #really bad need to take formatting out of variable
		if var1 == var2:
			if var1 == var3:
				return 1			
			else:
				return 0
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
    for countRow in range(0,3):
        for countCol in range(0,3):
            if gridSpots[countRow][countCol] == " - ": #really bad need to take formatting out of variable
                return False
    return True


while winner == 0:
    
    updateDisplay()
    
    print '\ncurrent player is '+ currentPlayer + '\nenter your move as a combination of number and number'
        
    move = raw_input('--> ')
    
    if translateInput(move):
        shouldUpdatePlayer = True
    else:
        shouldUpdatePlayer = False
        
    if checkGrid() == 1:
        updateDisplay()
        print('\nWINNER IS' + currentPlayer + "!!! END OF GAME")
        winner = 1

    if noMovesLeft():
        updateDisplay()
        print('\nNO WINNER. END OF GAME')
        winner = 1
   
    if shouldUpdatePlayer:
        currentPlayer =  returnNextPlayer(currentPlayer)
    else:       
        print('\n----spot taken - choose another spot----')







# if type(firstMove) is str:
#     print 'input is a string'
#     print 'length is ' + str(len(firstMove))
#     if len(firstMove) != 2:
#      print 'invalid input'
#
#
#
#     chars = set('abc,')
#     if any((c in chars) for c in firstMove):
#         print('Found a valid letter')
#     else:
#         print('No valid letter found')
#
#     chars = set('123,')
#     if any((c in chars) for c in firstMove):
#         print('Found a valid number')
#     else:
#         print('No valid number found')
    
    
    #tranlating user input into a location on the gameboard
    
    
    
    #list of things to check for 
    # make sure input valid in terms of length, within char and number set
    
    
    # >>> i = 123
    # >>> type(i)
    # <type 'int'>
    # >>> type(i) is int
    # True
    # >>> i = 123456789L
    # >>> type(i)
    # <type 'long'>
    # >>> type(i) is long
    # True
    # >>> i = 123.456
    # >>> type(i)
    # <type 'float'>
    # >>> type(i) is float
    # True