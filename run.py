from random import randint
import os
from colorama import Fore, Style


# Legend
# k for placing ship and hit battleship
# '' for available space
# x for missing turns

os.system('clear')


def print_board(board, matrix_size):
    """
    Print the board for the game
    based on the matrix_size,
    board: the board to play,
    matrix_size: selection of board
    size for the user.
    """
    i = 2
    print(' -----------')
    print("   1", end="")
    while i <= matrix_size:
        print(" ", i, end="")
        i += 1
    row_number = 1
    print()
    for row in board:
        print("%d | %s |" % (row_number, " | ".join(row)))
        row_number += 1


def create_ship(board, matrix_size):
    """
    Print the ship for the board
    using the random integer,
    board: the board to play,
    matrix_size: selection of board
    size for the user.
    """
    random_row = randint(0, matrix_size-1)
    random_column = randint(0, matrix_size - 1)
    ship_row, ship_column = random_row, random_column
    board[ship_row][ship_column] = 'k'


def get_ship_location(matrix_size):
    """
    Returns the ship location in the board,
    Raise the value error for ship row and
    ship column with message,
    Returns: the location of the ship as a tuple,
    matrix_size: selection of board
    size for the user.
    """
    print(' -----------')
    while True:
        try:
            string = "Please enter a ship row"
            row = int(input(f'> {string} 1 - {matrix_size} : \n'))
        except ValueError:
            print(Fore.RED + '> Please enter a valid integer\n')
            print(Style.RESET_ALL)
            continue
        else:
            if not validate_input(matrix_size, row):
                print(Fore.RED + f"> Oops, You entered {row} but your input",
                      f" is not between {1} and {matrix_size}\n")
                print(Style.RESET_ALL)
            else:
                break

    while True:
        try:
            string = "Please enter a ship column"
            column = int(input(f"> {string} 1 - {matrix_size} : \n"))
        except ValueError:
            print(Fore.RED + '> Please enter a valid integer\n')
            print(Style.RESET_ALL)
            continue
        else:
            if not validate_input(matrix_size, column):
                print(Fore.RED + f'> Oops, You entered {column} but your',
                      f'input is not between {1} and {matrix_size}\n')
                print(Style.RESET_ALL)
            else:
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


def validate_matrix_size(matrix_size):
    """
    matrix_size: selection of board
    size for the user.
    """
    return matrix_size > 2 and matrix_size < 10


def validate_input(matrix_size, coordinates):
    """
    matrix_size: selection of board
    size for the user,
    coordinates: for rows and columns of board.
    """
    return coordinates > 0 and coordinates <= matrix_size


def main():
    """
    Add the check for username, matrix_size
    and holding the control of all functions
    with different messages and alerts.
    """
    print('> WELCOME TO PYTHON GAME\n')
    title = """ _           _   _   _           _     _
| |         | | | | | |         | |   (_)
| |__   __ _| |_| |_| | ___  ___| |__  _ _ __
| '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \.
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                        | |
                                        |_| """

    print(f'{title}')
    while True:
        is_enter_pressed = (input('> PRESS ENTER TO START THE GAME\n'))
        if is_enter_pressed == "":
            while True:
                name = (input('> Please enter your name: \n'))
                if validate_name(name):
                    break
                else:
                    print(Fore.RED + '> Name should only contain string',
                          'characters\n')
                    print(Style.RESET_ALL)
            print(Fore.GREEN + f'> Hello {name} welcome to battleship\n')
            print(Style.RESET_ALL)
            while True:
                try:
                    string = "> Please enter matrix size"
                    matrix_size = int(input(f'{string} (between 3 and 9): \n'))
                except ValueError:
                    print(Fore.RED + '> Please enter a valid integer\n')
                    print(Style.RESET_ALL)
                    continue
                else:
                    if not validate_matrix_size(matrix_size):
                        print(Fore.RED + f'> Oops, You entered {matrix_size}',
                              'but your input is not between 3 and 9\n')
                        print(Style.RESET_ALL)
                    else:
                        break
            hidden_board = [['']*matrix_size for x in range(matrix_size)]
            guess_board = [['']*matrix_size for x in range(matrix_size)]
            create_ship(hidden_board, matrix_size)
            print(hidden_board)
            turns = 5
            while turns > 0:
                print_board(guess_board, matrix_size)
                row, column = get_ship_location(matrix_size)
                if guess_board[row][column] == 'x':
                    print(Fore.RED + '> You already guessed that\n')
                    print(Style.RESET_ALL)
                elif hidden_board[row][column] == 'k':
                    print(Fore.GREEN + '> Congratulations, You have hit',
                          'the target.\n ---You Won---\n')
                    print(Style.RESET_ALL)
                    print(Fore.BLUE + '> Play again :)\n')
                    print(Style.RESET_ALL)

                    guess_board[row][column] = 'k'
                    print_board(guess_board, matrix_size)

                    break
                else:
                    print(Fore.RED + '> Sorry, You missed the target\n')
                    print(Style.RESET_ALL)
                    guess_board[row][column] = 'x'
                    turns -= 1
                    print(Fore.BLUE + '> You have ' + str(turns) + '',
                          'turns remaining\n')
                    print(Style.RESET_ALL)
                if turns == 0:
                    print(Fore.RED + '> Sorry, your turns are finished,\n',
                          '---GAME OVER---\n')
                    print(Style.RESET_ALL)
                    print(Fore.BLUE + '> Play again :)\n')
                    print(Style.RESET_ALL)

                    guess_board[row][column] = 'x'
                    print_board(guess_board, matrix_size)

                    break
            break
        else:
            print(Fore.RED + '> Enter button will only start the game\n')
            print(Style.RESET_ALL)


main()
