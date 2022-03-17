from random import randint

# Legend
# k for placing ship and hit battleship

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