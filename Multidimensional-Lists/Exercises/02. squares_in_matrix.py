#create the matrix
def create_matrix(rows):
    result = []
    for _ in range(rows):
        result.append(input().split())
    return result

def contains_equal_chars(square):
    if square.count(square[0]) == len(square):
        return True

rows, columns = [int(el) for el in input().split()]
matrix = create_matrix(rows)
valid_squares_count = 0

for r in range(rows - 1):
    for c in range(columns - 1):
        square = matrix[r][c:c + 2] + matrix[r + 1][c:c + 2]
        if contains_equal_chars(square):
            valid_squares_count += 1

print(valid_squares_count)