def create_matrix():
    rows = int(input())
    result = [[int(x) for x in input().split(", ")] for _ in range(rows)]
    return result

def even_matrix(matrix):
    result = [[n for n in row if n % 2 == 0] for row in matrix]
    return result

matrix = create_matrix()
print(even_matrix(matrix))