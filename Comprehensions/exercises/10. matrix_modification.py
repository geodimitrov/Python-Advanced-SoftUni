def create_matrix(n_lines):
    result = []
    for line in range(n_lines):
        result.append(list(int(el) for el in input().split()))
    return result

def run_command(command, matrix, range):
    command_type = command.split()[0]
    row, col, value = [int(el) for el in command.split()[1:]]
    is_valid = True
    if row not in range or col not in range:
        is_valid = False
    else:
        if command_type == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    if not is_valid:
        print("Invalid coordinates")

def print_result(matrix):
    for row in matrix:
        print(*[str(el) for el in row], sep=" ")

#read input and create matrix
rows = int(input())
matrix = (create_matrix(rows))
matrix_range = range(0, rows)

#read commands
while True:
    command = input()
    if command == "END":
        break
    else:
        run_command(command, matrix, matrix_range)

print_result(matrix)