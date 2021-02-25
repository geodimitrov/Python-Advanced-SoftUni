# use as many funcs as possible to break down the code
def create_matrix(n_lines):
    matrix = []
    for n in range(n_lines):
        line = [el for el in input()]
        matrix.append(line)
    return matrix

#get the initial position of the player
def get_player_position(player, matrix):
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == player:
                position = [row, col]
    return position

# check if the new posiiton of the player is out of range
def out_of_range(new_position, matrix):
    if new_position not in range(len(matrix)):
        return True

def remove_last_letter(text):
    if text:
        return text[:len(text) - 1]

def print_result(text, matrix):
    print(text)
    for line in matrix:
        print("".join(line))

text = input()
lines = int(input())   # the size of the matrix, n * n
matrix = create_matrix(lines)

commands = int(input())  # num of commands
PLAYER = "P"
player_position = get_player_position(PLAYER, matrix)

for i in range(commands):
    command = input()
    r, c = player_position

    if command == "up":
        new_position = r - 1
        if out_of_range(new_position, matrix):  # check if player goes out of range
            text = remove_last_letter(text)
        else:
            if matrix[new_position][c] == "-":
                matrix[r][c], matrix[r-1][c] = matrix[r-1][c], matrix[r][c]
            else:
                text += matrix[new_position][c]
                matrix[new_position][c] = PLAYER
                matrix[r][c] = "-"
            player_position[0] = new_position #move the player/change to new position

    elif command == "down":
        new_position = r + 1
        if out_of_range(new_position, matrix):
            text = remove_last_letter(text)
        else:
            if matrix[new_position][c] == "-":
                matrix[r][c], matrix[r + 1][c] = matrix[r + 1][c], matrix[r][c]
            else:
                text += matrix[new_position][c]
                matrix[new_position][c] = PLAYER
                matrix[r][c] = "-"
            player_position[0] = new_position

    elif command == "right":
        new_position = c + 1
        if out_of_range(new_position, matrix):
            text = remove_last_letter(text)
        else:
            if matrix[r][new_position] == "-":
                matrix[r][c], matrix[r][c + 1] = matrix[r][c + 1], matrix[r][c]
            else:
                text += matrix[r][new_position]
                matrix[r][new_position] = PLAYER
                matrix[r][c] = "-"
            player_position[1] = new_position

    elif command == "left":
        new_position = c - 1
        if out_of_range(new_position, matrix):
            text = remove_last_letter(text)
        else:
            if matrix[r][new_position] == "-":
                matrix[r][c], matrix[r][c - 1] = matrix[r][c - 1], matrix[r][c]
            else:
                text += matrix[r][new_position]
                matrix[r][new_position] = PLAYER
                matrix[r][c] = "-"
            player_position[1] = new_position

print_result(text, matrix)