knight = "K"

board = [
    ["0", "K", "0", "K", "0"],
    ["K", "0", "0", "0", "K"],
    ["0", "0", "K", "0", "0"],
    ["K", "0", "0", "0", "K"],
    ["0", "K", "0", "K", "0"]
]

k_dimensions = [
    (-1, -2), (-1, +2), (+1, +2), (+1, -2),
    (-2, -1), (-2, +1), (+2, +1), (+2, -1)
]

def move_knight_on_board(board, row, column, counter, dimensions):

    for dimension in dimensions:
        current_row = row + dimension[0]
        current_col = col + dimension[1]

        if board[current_row][current_col] == knight:
            board[row][column] = "0"
            counter += 1

size = 5
counter = 0

for row in range(size):
    for col in range(size):
        if board[row][col] == knight:
            move_knight_on_board(board, row, col, counter, k_dimensions)
