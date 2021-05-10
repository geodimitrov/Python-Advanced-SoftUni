
# board = [
#     ["0", "K", "0", "K", "0"],
#     ["K", "0", "0", "0", "K"],
#     ["0", "0", "K", "0", "0"],
#     ["K", "0", "0", "0", "K"],
#     ["0", "K", "0", "K", "0"]
# ]

k_dimensions = [
    (+1, -2), (-1, -2), (-2, -1), (-2, +1),
    (-1, +2), (+1, +2), (+2, +1), (+2, -1)
]

def create_board(size):
    result = []
    for _ in range(size):
        line = list(input())
        result.append(line)

    return result


def is_inside_board(row, column, size):
    return 0 <= row < size and 0 <= column < size

def calc_kills(board, size, row, column, dimensions):
    result = 0

    for dimension in dimensions:
        current_row = row + dimension[0]
        current_col = column + dimension[1]

        if is_inside_board(current_row, current_col, size) \
                and board[current_row][current_col] == "K":
            result += 1

    return result

size = int(input())
board = create_board(size)
min_killed_knights = 0

while True:
    max_kills = 0
    killer_knight_position = None

    for row in range(size):
        for col in range(size):
            if board[row][col] == "K":
                kills = calc_kills(board, size, row, col, k_dimensions)

                if max_kills < kills:
                    max_kills = kills
                    killer_knight_position = (row, col)

    if killer_knight_position:
        row, col = killer_knight_position
        board[row][col] = "0"
        min_killed_knights += 1

    else:
        break

print(min_killed_knights)