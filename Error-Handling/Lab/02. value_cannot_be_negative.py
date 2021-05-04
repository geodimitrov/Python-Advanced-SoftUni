class ValueCannotBeNegative(Exception):
    pass

numbers = [1, 4, -5, 3, 10]

for num in numbers:
    if num < 0:
        raise ValueCannotBeNegative