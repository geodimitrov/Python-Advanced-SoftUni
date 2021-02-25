# Solution 1
# use func permutations from itertools module
from itertools import permutations

def text_permutation(string):
    return list(permutations(string))

text = input()
[print("".join(el)) for el in text_permutation(text)]

# Solution 2
# use recursion
def char_combinations(text, index=0):
    if index == len(text):
        print("".join(text))
        return

    for i in range(index, len(text)):
        text[index], text[i] = text[i], text[index]
        char_combinations(text, index + 1)
        text[index], text[i] = text[i], text[index]

text = list(input())
char_combinations(text)