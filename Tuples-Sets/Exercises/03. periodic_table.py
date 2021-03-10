def create_set_elements(count):
    elements = []
    for _ in range(count):
        for el in input().split():
            elements.append(el)
    return set(elements)

def print_result(set):
    for el in set:
        print(el)

n = int(input())
elements = create_set_elements(n)
print_result(elements)