from random import randint

# Legend
# k for placing ship and hit battleship
# '' for available space
# x for missing turns


def print_board(board):
    """
    Print the board for the game
    based on the MATRIX_SIZE,
    board: the board to play.
    """
    i = 2
    print(' -----------')
    print("   1", end="")
    while i <= MATRIX_SIZE:
        print(" ", i, end="")
        i += 1
    row_number = 1
    print()
    for row in board:
        print("%d | %s |" % (row_number, " | ".join(row)))
        row_number += 1


def create_ship(board):
    """
    Print the ship for the board
    using the random integer,
    board: the board to play.
    """
    for ship in range(MATRIX_SIZE):
        ship_row, ship_column = randint(0, MATRIX_SIZE-1), randint(0, MATRIX_SIZE-1)
    board[ship_row][ship_column] = 'k'


def get_ship_location():
    """
    Returns the ship location in the board,
    Raise the value error for ship row and
    ship column with message,
    Returns: the location of the ship as a tuple.
    """
    print(' -----------')
    while True:
        try:
            row = int(input(('Please enter a ship row 1 - %d : \n'
                             % MATRIX_SIZE)))
        except ValueError:
            print('Please enter a valid integer\n')
            continue
        if(row > 0 and row <= MATRIX_SIZE):
            break

    while True:
        try:
            column = int(input('Please enter a ship column 1 - %d : \n'
                               % MATRIX_SIZE))
        except ValueError:
            print('Please enter a valid integer\n')
            continue
        if(column > 0 and column <= MATRIX_SIZE):
            break
    return(int(row)-1, int(column)-1)


def count_hit_ship(board):
    """
    Returns the count for hitting ship
    in the board and indicate with k,
    board: the board to play.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'k':
                count += 1
    return count


def validate_name(name):
    """
    Returns the validate user name,
    name: the username.
    """
    return name.isalpha()


def main():
    """
    Add the check for username, MATRIX_SIZE
    and holding the control of all functions
    with different messages and alerts.
    """
    while True:
        name = (input('Please enter your name: \n'))
        if validate_name(name):
            break
        else:
            print('Name should only contain string characters\n')
    print(f'Hello {name} welcome to battleship\n')
    global MATRIX_SIZE
    while True:
        try:
            MATRIX_SIZE = int(input
                              ('Please enter matrix size (between 3 and 9): \n'))
        except ValueError:
            print('Please enter a valid integer\n')
            continue
        if(MATRIX_SIZE > 2 and MATRIX_SIZE < 10):
            break

    global HIDDEN_BOARD
    global GUESS_BOARD
    HIDDEN_BOARD = [['']*MATRIX_SIZE for x in range(MATRIX_SIZE)]
    GUESS_BOARD = [['']*MATRIX_SIZE for x in range(MATRIX_SIZE)]
    create_ship(HIDDEN_BOARD)
    print(HIDDEN_BOARD)
    turns = 5
    while turns > 0:
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == 'x':
            print('You already guessed that\n')
        elif HIDDEN_BOARD[row][column] == 'k':
            print('Congratulations, You have hit the target.\n ---You Won---\n')
            print('Play again :)\n')

            GUESS_BOARD[row][column] = 'k'
            print_board(GUESS_BOARD)

            break
        else:
            print('Sorry, You missed the target\n')
            GUESS_BOARD[row][column] = 'x'
            turns -= 1
            print('You have ' + str(turns) + ' turns remaining\n')
        if turns == 0:
            print('Sorry, your turns are finished,\n ---The game over---\n')
            print('Play again :)\n')

            GUESS_BOARD[row][column] = 'x'
            print_board(GUESS_BOARD)

            break


main()
