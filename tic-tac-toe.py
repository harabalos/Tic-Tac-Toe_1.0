def display_board(board):
    print('     |', '    ', '|')
    print(' ', board[1], '    ', board[2], '   ', board[3])
    print('_____|', '____', '|_____')
    print('     |', '    ', '|')
    print(' ', board[4], '    ', board[5], '   ', board[6])
    print('_____|', '____', '|_____')
    print('     |', '    ', '|')
    print(' ', board[7], '    ', board[8], '   ', board[9])
    print('     |', '    ', '|')


test = ['#', 'X', 'X', 'O', 'X', 'O', 'O', 'X', 'O', 'X']
display_board(test)
