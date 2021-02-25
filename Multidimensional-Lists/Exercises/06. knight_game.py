
def create_matrix(n_lines):
    result = []
    for line in range(n_lines):
        result.append([el for el in input()])
    return result

lines = 5
matrix = create_matrix(lines)
