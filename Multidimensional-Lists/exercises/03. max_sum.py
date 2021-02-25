# use a func to create the matrix
def create_matrix(rows):
    result = []
    for _ in range(rows):
        result.append(list(int(el) for el in input().split()))
    return result

#read input
rows, columns = [int(el) for el in input().split()]
matrix = create_matrix(rows)

max_sum_square = -9999999999999

#create for loop to check sums of 3x3 squares
for r in range(rows - 2):
    for c in range(columns - 2):
        sum_square = sum(matrix[r][c:c + 3]) + sum(matrix[r+1][c:c + 3]) + sum(matrix[r+2][c:c + 3])
        if sum_square > max_sum_square:
            max_sum_square = sum_square
            max_square = [matrix[r][c:c + 3], matrix[r+1][c:c + 3], matrix[r+2][c:c + 3]]

print(f"Sum = {max_sum_square}")
for el in max_square:
    print(*el, sep=" ")