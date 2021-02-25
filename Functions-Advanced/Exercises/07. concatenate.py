from functools import reduce

def concatenate(*args):
    result = reduce(lambda x, y: x + y, args)
    return result