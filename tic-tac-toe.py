from random import randint


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


def place_marker(board, choice, position):
    board[position] = choice
    return board


def replay():
    choice = 'wrong'
    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input('Do you want to play again (Y or N)?: ')
        if choice not in ['Y', 'y', 'N', 'n']:
            print('I dont understand please put Y or N')
        if choice == 'Y' or choice == 'y':
            return True
        elif choice == 'N' or choice == 'n':
            return False


def win_check(board, choise):
    for i in board:
        if board[1] == choise:
            if board[2] == choise and board[3] == choise:
                return True
            elif board[4] == choise and board[7] == choise:
                return True
            elif board[5] == choise and board[9] == choise:
                return True
        elif board[2] == choise:
            if board[5] == choise and board[8] == choise:
                return True
        elif board[3] == choise:
            if board[5] == choise and board[7] == choise:
                return True
            elif board[6] == choise and board[9] == choise:
                return True
        elif board[4] == choise:
            if board[5] == choise and board[6] == choise:
                return True
        elif board[7] == choise:
            if board[8] == choise and board[9] == choise:
                return True


def choose_first():
    first = randint(1, 2)
    print(f'player {first} will go first')


def space_check(board, position):
    if ' ' in board:
        return True
    else:
        return False


def full_board_check(board):
    s = 0
    for i in board:
        if i == 'O' or i == 'X':
            s = s + 1
        elif i == '#':
            continue
    if s == 9:
        return True
    else:
        return False


def player_choice(board):
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
    if space_check:

        return int(position)
