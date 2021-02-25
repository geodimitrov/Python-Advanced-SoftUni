from functools import reduce

def operate(operator, *args):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    product = reduce(operations.get(operator), args)

    return product

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
