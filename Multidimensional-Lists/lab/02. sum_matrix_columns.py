
def create_matrix(rows):
    result = []
    for r in range(rows):
        result.append(list(map(int, input().split())))
    return result

def calc_sum_columns(matrix, rows, columns):
    for c in range(columns):
        column_sum = 0
        for r in range(rows):
            element = matrix[r][c]
            column_sum += element
        print(column_sum)

rows, columns = [int(x) for x in input().split(", ")]
matrix = create_matrix(rows)
calc_sum_columns(matrix, rows, columns)