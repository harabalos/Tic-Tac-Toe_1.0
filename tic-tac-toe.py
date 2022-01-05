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


def player_input():
    choice = 'wrong'
    correct_items = ['X', 'x', 'O', 'o']
    while choice not in correct_items:
        choice = input('Please enter X or O: ')
        if choice not in correct_items:
            print('You can only enter X or O')
    return choice


def user_position():
    position = 'wrong'
    acceptable_range = range(1, 9)
    within_range = False
    while position.isdigit() == False or within_range == False:
        position = input('Please enter a number between 1 - 9: ')
        if position.isdigit() == False:
            print('Sorry that is not a digit')
        if position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
            else:
                print('Your are out of acceptable range (1-9)')
                within_range = False
    return int(position)
