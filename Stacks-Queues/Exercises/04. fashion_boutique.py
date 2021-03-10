#Use stack to solve it

clothes = [int(el) for el in input().split()]
capacity = int(input())
sum_values = 0
counter = 1

while clothes:
    cloth_value = clothes.pop()
    sum_values += cloth_value

    if sum_values == capacity:
        if len(clothes) > 0:
            counter += 1
            sum_values = 0
    elif sum_values > capacity:
        counter += 1
        sum_values = cloth_value

print(counter)