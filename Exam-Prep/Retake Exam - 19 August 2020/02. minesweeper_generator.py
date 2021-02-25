BOMB = "*"

def insert_bombs(result, bombs):
    for bomb in range(bombs):
    # for bomb in [
    #         "(0, 3)",
    #         "(1, 1)",
    #         "(2, 2)",
    #         "(3, 0)"
    # ]:
        bomb_row, bomb_column = eval(input())
        result[bomb_row][bomb_column] = "*"

    return result


def create_matrix():
    size = int(input())
    bombs = int(input())
    result = []
    for row in range(size):
        result.append([])
        for col in range(size):
            result[row].append(0)

    return insert_bombs(result, bombs)

def in_range(index, matrix):
    if index in range(len(matrix)):
        return True

def search_for_bombs(matrix, row, col, delta, BOMB):
    delta_row = row + delta[0]
    delta_col = col + delta[1]

    if in_range(delta_row, matrix) and in_range(delta_col, matrix):
        if matrix[delta_row][delta_col] == BOMB:
            matrix[row][col] += 1

    return matrix

def play_game(matrix, BOMB):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if not matrix[row][col] == BOMB:
                [search_for_bombs(matrix, row, col, delta, BOMB) for delta in deltas]

    return matrix


def print_result(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

matrix = create_matrix()
play_game(matrix, BOMB)
print_result(matrix)
