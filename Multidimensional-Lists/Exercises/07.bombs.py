dead_cell = 0
deltas = [
    (0, -1), (-1, -1), (-1, 0), (-1, +1),
    (0, +1), (+1, +1), (+1, 0), (+1, -1)
]

# matrix = [
#         [8, 3, 2, 5],
#         [6, 4, 7, 9],
#         [9, 9, 3, 6],
#         [6, 8, 1, 2]
#     ]

def create_matrix(size):
    result = []

    for _ in range(size):
        line = input().split(" ")
        result.append(list(map(int, line)))

    return result

def is_dead(cell):
    return cell <= dead_cell


def is_inside_matrix(matrix, row, column):
    return row in range(len(matrix)) and column in range(len(matrix))


def detonate_bomb(matrix, row, column):
    bomb_value = matrix[row][column]
    matrix[row][column] = dead_cell

    for delta in deltas:
        next_row = row + delta[0]
        next_col = column + delta[1]

        if is_inside_matrix(matrix, next_row, next_col) \
                and not is_dead(matrix[next_row][next_col]):
            matrix[next_row][next_col] -= bomb_value

def get_alive_cells(matrix):
    result = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if not is_dead(matrix[row][col]):
                result.append(matrix[row][col])

    return result

def print_result(matrix):
    alive_cells = get_alive_cells(matrix)
    sum_alive_cells = sum(alive_cells)
    print(f"Alive cells: {len(alive_cells)}\nSum: {sum_alive_cells}")
    print("\n".join([' '.join(map(str, row)) for row in matrix]))

size = int(input())
matrix = create_matrix(size)
bombs = [tuple(map(int, el.split(","))) for el in input().split()]

for bomb in bombs:

    bomb_row, bomb_col = bomb

    if not is_dead(matrix[bomb_row][bomb_col]):
        detonate_bomb(matrix, bomb_row, bomb_col)

print_result(matrix)

