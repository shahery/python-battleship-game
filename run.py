matrixSize = int(input('Please enter matrix size (between 3 and 9): '))
hidden_board = [['']*matrixSize for x in range(matrixSize)]
guess_board = [['']*matrixSize for x in range(matrixSize)]


def print_board(board):
    """
    Create the function to print the board
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