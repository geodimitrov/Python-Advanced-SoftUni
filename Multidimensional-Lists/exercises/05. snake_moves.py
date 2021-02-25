def create_matrix(rows, columns):
    result = []
    for r in range(rows):
        row = ["" for c in range(columns)]
        result.append(row)
    return result

def print_result(matrix):
    for el in matrix:
        print("".join(el))

rows, columns = map(int, input().split())
snake = input()
matrix = create_matrix(rows, columns)
snake_index = 0

for r in range(rows):
    if r % 2 == 0:
        for c in range(columns):
            if snake_index == len(snake):
                snake_index = 0
            matrix[r][c] = snake[snake_index]
            snake_index += 1
    else:
        for c in range(columns - 1, -1, -1):
            if snake_index == len(snake):
                snake_index = 0
            matrix[r][c] = snake[snake_index]
            snake_index += 1

print_result(matrix)