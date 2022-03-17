from random import randint

# Legend
# k for placing ship and hit battleship
# '' for available space
# x for missing turns

matrixSize = int(input('Please enter matrix size (between 3 and 9): '))
hidden_board = [['']*matrixSize for x in range(matrixSize)]
guess_board = [['']*matrixSize for x in range(matrixSize)]


def print_board(board):
    """
    Return the board for the game
    using the matrixSize.
    """
    i = 2
    print(' -----------')
    print("   1", end="")
    while i <= matrixSize:
        print(" ", i, end="")
        i += 1
    row_number = 1
    print()
    for row in board:
        print("%d | %s |" % (row_number, " | ".join(row)))
        row_number += 1


def create_ship(board):
    """
    Return the ship for the board
    using the random integer
    """
    for ship in range(matrixSize):
        ship_row, ship_column = randint(0, matrixSize-1), randint(0, matrixSize-1)
    board[ship_row][ship_column] = 'k'


def get_ship_location():
    """
    Return the ship location in the board,
    Raise the value error for ship row and
    ship column with message.
    """
    print(' -----------')
    while True:
        try:
            row = int(input(('Please enter a ship row 1 - %d : ' 
                             % matrixSize)))
        except ValueError:
            print('Please enter a valid integer')
            continue
        if(row > 0 and row <= matrixSize):
            break

    while True:
        try:
            column = int(input('Please enter a ship column 1 - %d : '
                               % matrixSize))
        except ValueError:
            print('Please enter a valid integer')
            continue
        if(column > 0 and column <= matrixSize):
            break
    return(int(row)-1, int(column)-1)


def count_hit_ship(board):
    """
    Return the count for hitting ship
    in the board and indicate with k.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'k':
                count += 1
    return count


def validate_name(name):
    """
    Return the validate user name.
    """
    return name.isalpha()


def main():
    """
    Return the check for username, matrixSize
    and holding the control of all functions 
    with different messages and alert.
    """
    while True:
        name = (input('Please enter your name: '))
        if validate_name(name):
            break
        else:
            print('Name should only contain string characters')
    print(f'Hello {name} welcome to battleship')
    while True:
        try:
            matrixSize = int(input
                             ('Please enter matrix size (between 3 and 9): '))
        except ValueError:
            print('Please enter a valid integer')
            continue
        if(matrixSize > 2 and matrixSize < 10):
            break

    create_ship(hidden_board)
    print(hidden_board)
    turns = 5
    while turns > 0:
        print_board(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == 'x':
            print('You already guessed that')
        elif hidden_board[row][column] == 'k':
            print('Congratulations, You have hit the target.\n ---You Won---')
            print('Play again :)')

            guess_board[row][column] = 'k'
            print_board(guess_board)

            break
        else:
            print('Sorry, You missed the target')
            guess_board[row][column] = 'x'
            turns -= 1
            print('You have ' + str(turns) + ' turns remaining')
        if turns == 0:
            print('Sorry, your turns are finished,\n ---The game over---')
            break


main()