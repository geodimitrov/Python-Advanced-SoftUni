
# test_board = [
#     ["0", "K", "0", "K", "0"],
#     ["K", "0", "0", "0", "K"],
#     ["0", "0", "K", "0", "0"],
#     ["K", "0", "0", "0", "K"],
#     ["0", "K", "0", "K", "0"]
# ]

knight = "K"
k_dimensions = [
    (+1, -2), (-1, -2), (-2, -1), (-2, +1),
    (-1, +2), (+1, +2), (+2, +1), (+2, -1)
]

def create_board(size):
    result = []
    for _ in range(size):
        line = [el for el in input()]
        result.append(line)

    return result


def get_knights_positions(board, size):
    result = []

    for row in range(size):
        for col in range(size):
            if board[row][col] == knight:
                result.append((row, col))

    return result


def is_inside_board(board, row, column):
    return row in range(len(board)) and column in range(len(board))


def move_knight_on_board(board, row, column, dimensions):
    global counter

    for dimension in dimensions:
        current_row = row + dimension[0]
        current_col = column + dimension[1]


        if is_inside_board(board, current_row, current_col) \
                and board[current_row][current_col] == knight:
            board[current_row][current_col] = "0"
            counter += 1

size = int(input())
board = create_board(size)
knights = get_knights_positions(board, size)
counter = 0

for knight in knights:
    row, col = knight
    move_knight_on_board(board, row, col, k_dimensions)

print(board)
print(counter)