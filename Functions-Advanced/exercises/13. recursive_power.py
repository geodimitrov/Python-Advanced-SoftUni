#Solution 1: recursion
def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

print(recursive_power(2, 5))

# Solution 2: simple ^ operation
def recursive_power(number, power):
    return number ** power

print(recursive_power(2, 5))