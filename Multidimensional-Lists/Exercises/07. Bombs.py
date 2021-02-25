def create_matrix(n_lines):
    result = []
    for line in range(n_lines):
        result.append([int(el) for el in input().split()])
    return result

def insert_bombs(matrix, indices):
    for el in indices:
        row = int(el[0])
        col = int(el[1])
        matrix[row][col] = str(matrix[row][col])
    return matrix

def detonate_bombs(matrix, bomb):
    result = []
    for el in matrix:
        if isinstance(el, str) or el == 0 or el < 0:
            el = el
        else:
            el -= bomb
        result.append(el)
    return result

lines = int(input())
matrix = create_matrix(lines)
indices = [el.split(",") for el in input().split()]
insert_bombs(matrix, indices)


for bomb_location in indices:
    r = int(bomb_location[0])
    c = int(bomb_location[1])
    bomb = int(matrix[r][c])
    matrix[r][c] = 0

    if r == 0:
        if c == 0:
            matrix[r][c:c+2] = detonate_bombs(matrix[r][c:c+2], bomb)
            matrix[r+1][c:c+2] = detonate_bombs(matrix[r+1][c:c+2], bomb)
        elif c == lines - 1:
            matrix[r][c-1:c+1] = detonate_bombs(matrix[r][c-1:c+1], bomb)
            matrix[r+1][c-1:c+1] = detonate_bombs(matrix[r+1][c-1:c+1], bomb)
        else:
            matrix[r][c-1:c+2] = detonate_bombs(matrix[r][c-1:c+2], bomb)
            matrix[r+1][c-1:c+2] = detonate_bombs(matrix[r][c-1:c+2], bomb)

    elif r == lines - 1:
        if c == 0:
            matrix[r][c:c+2] = detonate_bombs(matrix[r][c:c+2], bomb)
            matrix[r-1][c:c+2] = detonate_bombs(matrix[r-1][c:c+2], bomb)
        elif c == lines - 1:
            matrix[r][c-1:c+1] = detonate_bombs(matrix[r-1][c:c+1], bomb)
            matrix[r-1][c-1:c+1] = detonate_bombs(matrix[r-1][c-1:c+1], bomb)
        else:
            matrix[r][c-1:c+2] = detonate_bombs(matrix[r][c-1:c+2], bomb)
            matrix[r-1][c-1:c+2] = detonate_bombs(matrix[r-1][c-1:c+2], bomb)

    else:
        if c == 0:
            matrix[r][c:c+2] = detonate_bombs(matrix[r][c:c+2], bomb)
            matrix[r-1][c:c+2] = detonate_bombs(matrix[r-1][c:c+2], bomb)
            matrix[r+1][c:c+2] = detonate_bombs(matrix[r+1][c:c+2], bomb)
        elif c == lines -1:
            matrix[r][c-1:c+1] = detonate_bombs(matrix[r][c-1:c+1], bomb)
            matrix[r-1][c-1:c+1] = detonate_bombs(matrix[r-1][c-1:c+1], bomb)
            matrix[r+1][c-1:c+1] = detonate_bombs(matrix[r+1][c-1:c+1], bomb)
        else:
            matrix[r][c-1:c+2] = detonate_bombs(matrix[r][c-1:c+2], bomb)
            matrix[r-1][c-1:c+2] = detonate_bombs(matrix[r-1][c-1:c+2], bomb)
            matrix[r+1][c-1:c+2] = detonate_bombs(matrix[r+1][c-1:c+2], bomb)

print(matrix)