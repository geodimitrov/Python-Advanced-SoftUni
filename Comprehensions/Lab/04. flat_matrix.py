def create_matrix():
    rows = int(input())
    result = [[int(x) for x in input().split(", ")] for _ in range(rows)]
    return result

def flatten_matrix(matrix):
    result = [n for row in matrix for n in row]
    return result

matrix = create_matrix()
print(flatten_matrix(matrix))