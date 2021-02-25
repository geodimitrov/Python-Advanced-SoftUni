QUEEN = "Q"
KING = "K"


def read_board(lines):
    result = []
    for line in range(lines):
        result.append(input().split())
    return result

def find_king_position(board, KING):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == KING:
                return (row, column)

def in_range(index, board):
    if index in range(len(board)):
        return True

def search_for_queens(board, king_position, delta):
    row, col = king_position

    while True:

        if not in_range(row, board) or not in_range(col, board):
            return

        if board[row][col] == QUEEN:
            return (row, col)

        row += delta[0]
        col += delta[1]

def find_capturing_queens(king_position, board, QUEEN):
    deltas = [
        (0, -1),  # LEFT
        (-1, -1),  # UP-LEFT DIAGONAL
        (-1, 0),  # UP
        (-1, 1),  # UP-RIGHT DIAGONAL
        (0, 1),  # RIGHT
        (1, 1),  # DOWN-RIGHT DIAGONAL
        (1, 0),  # DOWN
        (1, -1)  # DOWN-LEFT DIAG
 ]

    queens = [search_for_queens(board, king_position, delta) for delta in deltas]

    return [list(queen) for queen in queens if queen]

def print_result(queens):
    if queens:
        [print(el) for el in queens if el]
    else:
        print("The king is safe!")


board = read_board(lines=8)
king_position = find_king_position(board, KING)
queens = find_capturing_queens(king_position, board, QUEEN)
print_result(queens)
