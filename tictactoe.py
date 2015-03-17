#inits
#vars
empt = " - "

#make a list to store the game
emptyRow = [empt, empt, empt]

row0 = [0, 1, 2]
row1 = [3, 4, 5]
row2 = [6, 7, 8]

#row[row, col]
rows = [row0, row1, row2]

#extra '\' let's you put code on multiple lines
gameboard = '  0 1 2 \n1 '+str(rows[0][0])+' '+str(rows[0][1])+' '+str(rows[0][2])+\
                    '\n2 '+str(rows[1][0])+' '+str(rows[1][1])+' '+str(rows[1][2])+\
                    '\n2 '+str(rows[2][0])+' '+str(rows[2][1])+' '+str(rows[2][2])
print gameboard
print '\nfirst player is X\nenter your move as a combination of letter and number'
firstMove = raw_input('--> ')

indexRow = int(firstMove[0])
indexCol = int(firstMove[1])

rows[indexRow][indexCol] = 'X'


gameboard = '  0 1 2 \n1 '+str(rows[0][0])+' '+str(rows[0][1])+' '+str(rows[0][2])+\
                    '\n2 '+str(rows[1][0])+' '+str(rows[1][1])+' '+str(rows[1][2])+\
                    '\n2 '+str(rows[2][0])+' '+str(rows[2][1])+' '+str(rows[2][2])

print gameboard



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