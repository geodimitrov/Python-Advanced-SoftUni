from math import floor

PLAYER = "P"
WALLS = "X"

def create_matrix(size):
    return [input().split() for line in range(size)]

def find_player_position(matrix, PLAYER):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == PLAYER:
                return (row, col)

def in_range(row, column, matrix):
    if row in range(len(matrix)) and column in range(len(matrix)):
        return True


def read_commands(matrix, player_position, valid_commands, WALLS):
    player_row, player_col = player_position
    coins = 0
    path = []
    game_over = False

    while True:
        if coins >= 100:
            break
        command = input()

        if command in valid_commands:
            move_row, move_col = valid_commands[command]

            if in_range(player_row + move_row, player_col + move_col, matrix):
                player_row += move_row
                player_col += move_col

                if matrix[player_row][player_col] == WALLS:
                    game_over = True
                    break

                else:
                    coins += int(matrix[player_row][player_col])
                    path.append([player_row, player_col])

            else:
                game_over = True
                break

    return game_over, path, coins

def print_result(game, path, coins):
    if game:
        coins /= 2
        print(f"Game over! You've collected {floor(coins)} coins.")
    else:
        print(f"You won! You've collected {floor(coins)} coins.")

    print('Your path:')
    for el in path:
        print(el)

# data = [
#     "1 X 7 9 11",
#     "X 14 46 62 0",
#     "15 33 21 95 X",
#     "P 14 3 4 18",
#     "9 20 33 X 0",
# ]

size = int(input())
matrix = create_matrix(size)
player_position = find_player_position(matrix, PLAYER)
valid_commands = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

game, path, coins = read_commands(matrix, player_position, valid_commands, WALLS)
print_result(game, path, coins)


