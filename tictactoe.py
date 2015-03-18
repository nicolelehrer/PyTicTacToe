#VARS
empt = " - "
move = "99"
currentPlayer = ' X '
winner = 0;
message = 'Blank message'

#make a list to store the game
row0 = [empt, empt, empt]
row1 = [empt, empt, empt]
row2 = [empt, empt, empt]
gridSpots = [row0, row1, row2]
#gridSpots[row][col] access like 2d array


#FUNCTIONS
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
    gridSpots[indexRow][indexCol] = currentPlayer
            
def spotFree(aMove):
    indexRow = int(aMove[0])
    indexCol = int(aMove[1])
    if gridSpots[indexRow][indexCol] == " - ":
        return True
    else:
        return False
            
def inputIsValid(aMove):
    #length
    if len(aMove)!=2:
        return False
    #range
    chars = set('012')
    if  aMove[0] not in chars or aMove[1] not in chars:
        return False
    return True
        
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

#---------------------------------------------------

def recommendNextMove(aCurrentPlayer):
        
    #ignoring other placement
    #if it's the first move go for center
    #if it's the second move go for corners 
    #if it's the third move all else equal 

    #considering other placement 
        #look for where there are two in a row
        #take third spot 
        
    for count in range(0, 3):	
        compareTwo(gridSpots[count][0], gridSpots[count][1], gridSpots[count][2], aCurrentPlayer)
    #     compareTwo(gridSpots[0][count], gridSpots[1][count], gridSpots[2][count], aCurrentPlayer)
    # lDiagResult = compareTwo(gridSpots[0][0], gridSpots[1][1], gridSpots[2][2], aCurrentPlayer)
    # rDiagResult = compareTwo(gridSpots[0][2], gridSpots[1][1], gridSpots[2][0], aCurrentPlayer)


def compareTwo(var1, var2, var3, aPlayer):
    
    holder = [var1, var2, var3]
    
    opposingPlayer = returnNextPlayer(aPlayer)
    
    #first check if you can win, then check if you can block

    if aPlayer in holder: #if one of the pieces is equal to one of interest
        if holder.count(' - ') < 2: #if at least 2 pieces are not equal to -
            if var1 != ' - ' and var1 == var2 or var1 == var3 or  var2 == var3: #if two pieces are equal 
                if var1 == ' - ' or  var2 == ' - ' or  var3 == ' - ': #if third piece is empty
                    print(aPlayer + " can win in this move");
                    return True
    # else:
 #        if var1 == opposingPlayer or var2 == opposingPlayer or var3 == opposingPlayer: #if one of the pieces is equal to one of interest
 #            if var1 == var2 or var1 == var3 or  var2 == var3: #if two pieces are equl
 #                if var1 == ' - ' or  var2 == ' - ' or  var3 == ' - ': #if third piece is empty
 #                    print(opposingPlayer + " can be blocked in this move");
 #                    return True

    print('just pic an open spot');
    return False
#---------------------------------------------------




#MAIN LOOP
while winner == 0:
    
    updateDisplay()
    
    print '\ncurrent player is '+ currentPlayer + '\nenter your move as a combination of first a row number and then a column number, like 00 or 12'
        
    recommendNextMove(currentPlayer)    
    
    move = raw_input('--> ')
    
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
        print('\nWINNER IS' + currentPlayer + "!!! END OF GAME")
        winner = 1

    if noMovesLeft():
        updateDisplay()
        print('\nNO WINNER. END OF GAME')
        winner = 1
   
    if shouldUpdatePlayer:
        currentPlayer =  returnNextPlayer(currentPlayer)
    else:       
        print(message)

#---------------------------------------------------

