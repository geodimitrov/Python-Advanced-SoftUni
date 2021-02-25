def create_matrix(size):
    result = []
    for n in range(size):
        result.append(list(map(str, input())))
    return result

def search_symbol(matrix, size, symbol):
    is_found = False
    location = []
    for r in range(size):
        if is_found:
            break
        for c in range(size):
            char = matrix[r][c]
            if char == symbol:
                location = (r, c)
                is_found = True
                break
    return location

def print_result(symbol, result):
    if result:
        print(result)
    else:
        print(f"{symbol} does not occur in the matrix")


size = int(input())
matrix = create_matrix(size)
symbol = input()
print_result(symbol, search_symbol(matrix, size, symbol))