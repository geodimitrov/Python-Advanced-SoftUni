def create_matrix(size):
    return [input().split() for line in range(size)]

def find_miner_start_position(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "s":
                return r, c

def find_total_coal(matrix):
    result = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "c":
                result += 1
    return result

def read_command(command, row, col, size):
    if command == "up":
        if row - 1 in range(size):
            row -= 1
    elif command == "down":
        if row + 1 in range(size):
            row += 1
    elif command == "left":
        if col - 1 in range(size):
            col -= 1
    elif command == "right":
        if col + 1 in range(size):
            col += 1
    return row, col

def move_miner(matrix, row, col):
    return matrix[row][col]

def element_is_end(element):
    if element == "e":
        return True

def print_game_over(row, col):
    return f"Game over! ({row}, {col})"

def element_is_coal(element, matrix, row, col):
    if element == "c":
        matrix[row][col] = "*"
        return True

def collected_all_coals(coals_count, total_coal):
    if coals_count == total_coal:
        return True

def print_collected_all_coals(row, col):
    return f"You collected all coals! ({row}, {col})"

def print_remaining_coals(coals_count, total_coal, row, col):
    return f"{total_coal - coals_count} coals left. ({row}, {col})"

def start_mining(matrix, miner_s_position, commands, size):
    total_coal = find_total_coal(matrix)
    coals_count = 0
    r, c = miner_s_position

    for command in commands:
        r, c = read_command(command, r, c, size)
        element = move_miner(matrix, r, c)

        if element_is_end(element):
            return print_game_over(r, c)

        elif element_is_coal(element, matrix, r, c):
            coals_count += 1
            if collected_all_coals(coals_count, total_coal):
                return print_collected_all_coals(r, c)

    return print_remaining_coals(coals_count, total_coal, r, c)


size = int(input())
commands = input().split()
# lines = [
#         "* * * c *",
#         "* * * e *",
#         "* * c * *",
#         "s * * c *",
#         "* * c * *",
# ]

matrix = create_matrix(size)
miner_start_position = find_miner_start_position(matrix, size)
result = start_mining(matrix, miner_start_position, commands, size)
print(result)