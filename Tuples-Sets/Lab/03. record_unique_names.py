def fill_list(count):
    list = []
    for _ in range(count):
        list.append(input())
    return list

def print_result(list):
    for el in list:
        print(el)

n = int(input())
names = set(fill_list(n))
print_result(names)