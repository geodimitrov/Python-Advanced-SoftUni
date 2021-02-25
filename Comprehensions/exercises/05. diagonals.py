def read_matrix_lines():
    return [int(x) for x in input().split(", ")]

def create_matrix(size):
    result = [read_matrix_lines() for _ in range(size)]
    return result

def get_first_diagonal(matrix, size):
    return [matrix[i][i]for i in range(size)]

def get_second_diagonal(matrix, size):
    result = []
    for r in range(size):
        result.append(matrix[r][size - r - 1])
    return result

def turn_diagonal_to_str(diagonal):
    result = ", ".join(map(str,diagonal))
    return result

size = int(input())

matrix = create_matrix(size)
first_diagonal = get_first_diagonal(matrix, size)
second_diagonal = get_second_diagonal(matrix, size)
print(f"First diagonal: {turn_diagonal_to_str(first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {turn_diagonal_to_str(second_diagonal)}. Sum: {sum(second_diagonal)}")