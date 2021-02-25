
# matrix = [
#     [7, 1, 3, 3, 2, 1],
#     [1, 3, 9, 8, 5, 6],
#     [4, 6, 7, 9, 1, 0],
# ]

def create_matrix():
    rows, columns = [int(el) for el in input().split(", ")]
    result = []
    for r in range(rows):
        result.append(list(map(int, input().split(", "))))
    return result

def calc_sum_matrix(matrix):
    sum_matrix = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            num = matrix[row][col]
            sum_matrix += num
    return sum_matrix

matrix = create_matrix()
print(calc_sum_matrix(matrix))
print(matrix)



