gameboard = '  A B C \n1 - - - \n2 - - - \n3 - - -'
print gameboard
print '\nfirst player is X\nenter your move as a combination of letter and number'
firstMove = raw_input('--> ')
if type(firstMove) is str:
    print 'input is a string'
    print 'length is ' + str(len(firstMove))
    if len(firstMove) != 2:
     print 'invalid input'
    
    
    
    
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