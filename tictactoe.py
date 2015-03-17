#inits
#vars
empt = " - "
move = "99"
currentPlayer = ' X '
winner = 0;

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
    print gameboard
    
    
def returnNextPlayer(aCurrentPlayer):
    if aCurrentPlayer == ' X ':
        return ' O '
    else:
        return ' X '


def translateInput(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    gridSpots[indexRow][indexCol] = currentPlayer


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
             
def checkValues():
    for rowCount in range(0, 3):	
       aResult = compareThree(gridSpots[rowCount][0], gridSpots[rowCount][0+1], gridSpots[rowCount][0+2])
       if aResult == 1:
           return 1

while winner == 0:
    updateDisplay()
    print '\ncurrent player is '+ currentPlayer + '\nenter your move as a combination of number and number'
    move = raw_input('--> ')
    translateInput(move)
    if checkValues() == 1:
        updateDisplay()
        print('winner received in main loop')
        winner = 1
    currentPlayer =  returnNextPlayer(currentPlayer)







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