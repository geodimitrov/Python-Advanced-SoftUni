
def create_matrix(size):
    result = []
    for n in range(size):
        result.append(list(map(int, input().split())))
    return result

def calc_sum_primary_diagonal(matrix, size):
    sum_primary_diagonal = 0
    for n in range(size):
        num = matrix[n][n]  #num of row and column are the same
        sum_primary_diagonal += num
    return sum_primary_diagonal

size = int(input())
matrix = create_matrix(size)
print(calc_sum_primary_diagonal(matrix, size))
