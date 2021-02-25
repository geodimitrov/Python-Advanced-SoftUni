# Solution 1
# use the func combinations from itertools module

from itertools import combinations

def chair_combinations(names, n_chairs):
    return combinations(names, n_chairs)

names = input().split(", ")
n = int(input()) #num of chairs
[print(*el, sep=", ") for el in chair_combinations(names, n)]


# Solution 2
# Use recursion

def calc_combinations(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_combinations(names[i+1:], n, combs)
        combs.pop()

names = input().split(", ")
n = int(input())

calc_combinations(names, n)