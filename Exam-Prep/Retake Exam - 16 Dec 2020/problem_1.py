# use as many functions as possible to break down the code
# use the deque func from collections
from collections import deque

def less_or_equal_to_zero(m_value, f_value, males, females):
    result = False
    if m_value <= 0:
        males.pop()
        result = True
    if f_value <= 0:
        females.popleft()
        result = True
    return result

def divisible_by_25(m_value, f_value, males, females):
    result = False
    if m_value % 25 == 0:
        males.pop()
        males.pop()
        result = True
    if f_value % 25 == 0:
        females.popleft()
        females.popleft()
        result = True
    return result


#create a func to print result
def print_result(males, females):
    if not males:
        print("Males left: none")
    else:
        print(f'Males left: {", ".join(list(map(str, males[::-1])))}') #turn the ints int str to join them, reverse order

    if not females:
        print("Females left: none")
    else:
        print(f'Females left: {", ".join(list(map(str, females)))}') # #turn the ints int str to join them, DO NOT reverse order

#read input and turn data into list of ints
males = [int(el) for el in input().split()]
females = deque(int(el) for el in input().split())

matches = 0  # counter for the matches

# try to match values untill there are values in both lists
while males and females:
    male_value = males[-1]
    female_value = females[0]

    #check if the values are <= 0
    if less_or_equal_to_zero(male_value, female_value, males, females):
        continue
    #check if the values are divisible by 25
    if divisible_by_25(male_value, female_value, males, females):
        continue
    # if equal, match the values
    if male_value == female_value:
        females.popleft()
        males.pop()
        matches += 1
    # if not, remove f value and reduce m value by 2; remove m value if <= 0
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {matches}")
print_result(males, females)