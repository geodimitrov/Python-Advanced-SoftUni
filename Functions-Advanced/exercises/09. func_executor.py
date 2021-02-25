from functools import reduce

def sum_numbers(*args):
    return reduce(lambda x, y: x + y, args)

def multiply_numbers(*args):
    return reduce(lambda x, y: x * y, args)

def func_executor(*args):
    result = []
    for el in args:
        func_name, elements = el
        result.append(func_name(*elements))
    return result