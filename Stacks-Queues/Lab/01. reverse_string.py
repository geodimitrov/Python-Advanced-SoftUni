
def reverse_str():
    string = [ch for ch in input()]
    reversed_string = ""

    while string:
        reversed_string += string.pop()
    return reversed_string

print(reverse_str())

