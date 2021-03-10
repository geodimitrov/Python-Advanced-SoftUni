def create_matrix(rows):
    result = []
    for row in rows:
        result.append([el for el in row])
    return result

def player(matrix, row, col):
    if matrix[row][col] == "P":
        return True

def find_player_position(matrix, rows, columns):
    for row in range(rows):
        for col in range(columns):
            if player(matrix, row, col):
                return row, col

def row_not_in_range(row, rows):
    if row not in range(rows):
        return True

def column_not_in_range(col, columns):
    if col not in range(columns):
        return True

def read_command(command, row, col, rows, columns):
    won_game = False

    if command == "U":
        if row_not_in_range(row - 1, rows):
            won_game = True
        else:
            row -= 1

    elif command == "D":
        if row_not_in_range(row + 1, rows):
            won_game = True
        else:
            row += 1

    elif command == "L":
        if column_not_in_range(col - 1, columns):
            won_game = True
        else:
            col -= 1

    else:
        if column_not_in_range(col + 1, columns):
            won_game = True
        else:
            col += 1

    return row, col, won_game


def print_won_game(matrix, row, col):
    for line in matrix:
        print("".join(line))
    print(f"won: {row} {col}")

def move_player(matrix, row, col):
    pass


def play_game(commands, matrix, player_position, rows, columns):
    row, col = player_position

    for command in commands:
        row, col, won_game = read_command(command, row, col, rows, columns)
        if won_game:
            return print_won_game(matrix, row, col)
        move_player()


rows, columns = [int(el) for el in "5 8".split()]

matrix_data = [
    ".......B",
    "...B....",
    "....B..B",
    "........",
    "..P.....",
]

matrix = create_matrix(matrix_data)
commands = [el for el in "ULLL"]
player_position = find_player_position(matrix, rows, columns)
play_game(commands, matrix, player_position, rows, columns)