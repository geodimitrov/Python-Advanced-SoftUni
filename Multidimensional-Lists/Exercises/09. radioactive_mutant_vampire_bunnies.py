player = "P"
bunny = "B"
dot = "."

# matrix_data = [
#     ".......B",
#     "...B....",
#     "....B..B",
#     "........",
#     "..P.....",
# ]

deltas = [
    (0, -1), (0, +1),
    (-1, 0), (+1, 0)
]

def create_matrix(rows):
    result = []

    for r in range(rows):
        line = input()
        result.append([char for char in line])

    return result

def get_players_position(matrix):

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == player:
                return row, col


def get_next_move_dimensions(command, curr_row, curr_col):

    if command == "L":
        curr_col -= 1

    elif command == "R":
        curr_col += 1

    elif command == "U":
        curr_row -=1

    else:
        curr_row += 1

    return curr_row, curr_col


def inside_matrix(row, column, rows, columns):
    return row in range(rows) and column in range(columns)


def get_bunnies_positions(matrix, rows, columns):
    result = []

    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == bunny:
                result.append((row, col))

    return result


def multiply_bunnies(matrix, rows, columns):
    bunnies_to_multiply = get_bunnies_positions(matrix, rows, columns)
    global is_dead

    for position in bunnies_to_multiply:
        curr_row, curr_col = position

        for delta in deltas:
            next_row = curr_row+ delta[0]
            next_col = curr_col + delta[1]

            if inside_matrix(next_row, next_col, rows, columns):
                if matrix[next_row][next_col] == player:
                    is_dead = True
                matrix[next_row][next_col] = bunny


def print_result(matrix, is_won, position):
    print("\n".join(''.join(row) for row in matrix))
    position_str = ' '.join(map(str, position))

    if is_won:
        print(f"won: {position_str}")
    else:
        print(f"dead: {position_str}")


rows, columns = map(int, input().split())
matrix = create_matrix(rows)
commands = input()
players_position = get_players_position(matrix)
is_won = False
is_dead = False

for command in commands:

    if is_won or is_dead:
        break

    curr_row, curr_col = players_position
    next_row, next_col = get_next_move_dimensions(command, curr_row, curr_col)

    if not inside_matrix(next_row, next_col, rows, columns):
        matrix[curr_row][curr_col] = dot
        is_won = True

    else:
        if matrix[next_row][next_col] == bunny:
            is_dead = True
        else:
            matrix[curr_row][curr_col] = dot
            matrix[next_row][next_col] = player

        players_position = next_row, next_col

    multiply_bunnies(matrix, rows, columns)

print_result(matrix, is_won, players_position)