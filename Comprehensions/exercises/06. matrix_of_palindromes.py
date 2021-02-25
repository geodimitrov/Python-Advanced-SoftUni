def get_string(row, col, letter):
    return chr(letter + row) + chr(letter + row + col) + chr(letter + row)

def create_matrix(rows, columns, letter):
    matrix = []
    for r in range(rows):
        matrix_row = []
        for c in range(columns):
            matrix_row.append(get_string(r, c, letter))
        matrix.append(matrix_row)
    return matrix

#read input
rows, columns = [int(x) for x in input().split()]

# "a" is 97 in the ascii table, we can use it as a constant
FIRST_LETTER = 97

# let's create the matrix (use a func)
matrix = create_matrix(rows, columns, FIRST_LETTER)

# print the matrix
for el in matrix:
    print(" ".join(el))