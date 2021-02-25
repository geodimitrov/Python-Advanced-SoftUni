def create_matrix(rows):
    result = []
    for _ in range(rows):
        row = [int(el) for el in input().split(", ")]
        result.append(row)
    return result

def get_biggest_sum_elements(matrix, r, c):
    result = [matrix[r][c:c + 2], matrix[r + 1][c:c + 2]]
    return result

def print_result(biggest_sum, biggest_sum_elements):
    for el in biggest_sum_elements:
        print(*list(map(str, el)), sep=" ")
    print(biggest_sum)

rows, columns = list(map(int, input().split(", ")))
matrix = (create_matrix(rows))

sum_square = 0
biggest_sum_square = sum_square

for c in range(columns - 1):
    for r in range(rows - 1):
        sum_square = matrix[r][c] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r][c+1]
        if sum_square > biggest_sum_square:
            biggest_sum_square = sum_square
            biggest_sum_elements = get_biggest_sum_elements(matrix, r, c)

print_result(biggest_sum_square, biggest_sum_elements)