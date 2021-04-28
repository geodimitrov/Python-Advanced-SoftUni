deltas = [
    (0, -1), (0, +1),
    (-1, 0), (+1, 0)
]

SIZE = 7
BULLSEYE = "B"


def create_matrix():
    result = []
    for _ in range(SIZE):
        result.append(input().split())

    return result


def inside_dartboard(row, column):
    return row in range(SIZE) and column in range(SIZE)


def get_points(board, row, column, count):
    points = 0

    for delta in deltas:
        curr_row = row + delta[0]
        curr_col = col + delta[1]

        while True:

            if not inside_dartboard(curr_row, curr_col):
                break

            if board[curr_row][curr_col].isdigit():
                points += int(board[curr_row][curr_col])
                break

            curr_row += delta[0]
            curr_col += delta[1]


    return points * count


def throw_dart(players, player, board, row, column):

    global is_won
    board_element = board[row][column]

    if board_element == BULLSEYE:
        is_won = True
        return

    elif board_element == "D":
        points = get_points(board, row, column, 2)

    elif board_element == "T":
        points = get_points(board, row, column, 3)

    else:
        points = int(board_element)

    players[player][0] -= points

    if players[player][0] <= 0:
        is_won = True


def print_winners_result(winner, throw_count):
    print(f"{winner} won the game with {throw_count} throws!")


players = {name: [501, 0] for name in input().split(", ")}
dartboard = create_matrix()
is_won = False

while not is_won:

    for player in players.keys():
        row, col = eval(input())
        players[player][1] += 1

        if inside_dartboard(row, col):
            throw_dart(players, player, dartboard, row, col)

        if is_won:
            throw_count = players[player][1]
            print_winners_result(player, throw_count)
            break