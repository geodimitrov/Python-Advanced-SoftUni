# Solution 1
def read_lines(n):
    res = []
    for _ in range(n):
        for el in input().split():
            res.append(el)
    return res

def read_input():
    n = int(input())  # num of lines
    result = read_lines(n)
    return result

def print_result(elements):
    print("\n".join(set(elements)))

elements = read_input()
print_result(elements)


# Solution 2

n = int(input())
elements = set()

for _ in range(n):
    line = input().split()
    for el in line:
        elements.add(el)

print("\n".join(elements))