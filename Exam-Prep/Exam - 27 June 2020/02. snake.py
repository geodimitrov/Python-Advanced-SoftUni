def create_matrix(n_lines):
    result = []
    for _ in range(n_lines):
        line = [el for el in input()]
        result.append(line)
    return result

def find_snake_position(matrix, SNAKE):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == SNAKE:
                snake_position = (r, c)
    return snake_position

def mark_old_position(r, c, matrix):
    matrix[r][c] = "."
    return matrix

def check_for_food(r, c, matrix, total_food):
    if matrix[r][c] == "*":
        total_food += 1
    return total_food

def find_burrow_position(matrix, BURROW):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == BURROW:
                burrow_position = (r, c)
    return burrow_position

def check_for_burrow(r, c, matrix, BURROW):
    if matrix[r][c] == BURROW:
        mark_old_position(r, c, matrix)
        r, c = find_burrow_position(matrix, BURROW)
    return (r, c)

def print_matrix(matrix):
    for line in matrix:
        print("".join(line))

lines = int(input())
matrix = create_matrix(lines)
SNAKE = "S"
BURROW = "B"
total_food = 0
row, col = find_snake_position(matrix, SNAKE)
out_of_range = False

while True:
    command = input()
    mark_old_position(row, col, matrix)

    if command == "up":
        if row - 1 not in range(lines):
            out_of_range = True
        else:
            row -= 1
            total_food = check_for_food(row, col, matrix, total_food)
            row, col = check_for_burrow(row, col, matrix, BURROW)
            matrix[row][col] = SNAKE

    elif command == "down":
        if row + 1 not in range(lines):
            out_of_range = True
        else:
            row += 1
            total_food = check_for_food(row, col, matrix, total_food)
            row, col = check_for_burrow(row, col, matrix, BURROW)
            matrix[row][col] = SNAKE

    elif command == "right":
        if col + 1 not in range(lines):
            out_of_range = True
        else:
            col += 1
            total_food = check_for_food(row, col, matrix, total_food)
            row, col = check_for_burrow(row, col, matrix, BURROW)
            matrix[row][col] = SNAKE

    elif command == "left":
        if col - 1 not in range(lines):
            out_of_range = True
        else:
            col -= 1
            total_food = check_for_food(row, col, matrix, total_food)
            row, col = check_for_burrow(row, col, matrix, BURROW)
            matrix[row][col] = SNAKE

    if total_food >= 10:
        print("You won! You fed the snake.")
        break

    if out_of_range:
        mark_old_position(row, col, matrix)
        print("Game over!")
        break

print(f"Food eaten: {total_food}")
print_matrix(matrix)