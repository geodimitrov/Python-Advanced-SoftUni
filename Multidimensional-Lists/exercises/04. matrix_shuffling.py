# use functions to break down the code
def create_matrix(rows):
    result = []
    for _ in range(rows):
        result.append(input().split())
    return result

def in_range(indices, rows_range, columns_range):
    is_in_range = True
    r_1, c_1, r_2, c_2 = indices
    if not r_1 in rows_range or not r_2 in rows_range:
        is_in_range = False
    if not c_1 in columns_range or not c_2 in columns_range:
        is_in_range = False
    return is_in_range

def is_valid(command, rows, columns):
    rows_range = range(0, rows)
    columns_range = range(0, columns)
    is_valid = True
    if not command.startswith("swap"):
        is_valid = False
    else:
        command = command.split()
        if not len(command) == 5:
            is_valid = False
        else:
            indices = [int(el) for el in command[1:len(command)]]
            if not in_range(indices, rows_range, columns_range):
                is_valid = False

    return is_valid

def execute_command(matrix, indices):
    r_1, c_1, r_2, c_2 = indices
    matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
    for el in matrix:
        print(*el, sep=" ")

rows, columns = [int(el) for el in input().split()]
matrix = create_matrix(rows)

while True:
    command = input()
    if command == "END":
        break
    else:
        if is_valid(command, rows, columns):
            indices = [int(el) for el in command.split()[1:len(command)]]
            execute_command(matrix, indices)
        else:
            print("Invalid input!")