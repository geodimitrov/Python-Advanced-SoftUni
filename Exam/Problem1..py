from collections import deque

def divisible(sum_values, firework_types):
    is_divisible = True

    if sum_values % 3 == 0 and sum_values % 5 == 0:
        firework_types["Crossette"] += 1
    elif sum_values % 3 == 0:
        firework_types["Palm"] += 1
    elif sum_values % 5 == 0:
        firework_types["Willow"] += 1
    else:
        is_divisible = False

    return is_divisible

def execute_operation(sum_values, firework_types):
    if divisible(sum_values, firework_types):
        fireworks.popleft()
        explosive_power.pop()
    else:
        fireworks[0] -= 1
        fireworks.append(fireworks.popleft())

    return firework_types

def firework_show(firework_types):
    count = 0
    for value in firework_types.values():
        if value >= 3:
            count += 1
    if count == 3:
        return True

def print_result(fireworks, explosive_power, firework_types):
    if firework_show(firework_types):
        print("Congrats! You made the perfect firework show!")
    else:
        print("Sorry. You can’t make the perfect firework show.")

    if fireworks:
        print(f'Firework Effects left: {", ".join(map(str, fireworks))}')
    if explosive_power:
        print(f'Explosive Power left: {", ".join(map(str, explosive_power))}')

    for key, value in firework_types.items():
        print(f"{key} Fireworks: {value}")


fireworks = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]
firework_types = {"Palm": 0, "Willow": 0, "Crossette": 0}

while True:

    if not fireworks or not explosive_power:
        break

    firework_value = fireworks[0]
    explosive_power_value = explosive_power[-1]

    if firework_value > 0 and explosive_power_value > 0:
        sum_values = firework_value + explosive_power_value
        firework_types = execute_operation(sum_values, firework_types)
        if firework_show(firework_types):
            break

    else:
        if firework_value <= 0:
            fireworks.popleft()
        else:
            explosive_power.pop()

print_result(fireworks, explosive_power, firework_types)