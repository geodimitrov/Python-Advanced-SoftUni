from collections import deque

def check_cup_value(cups):
    if cups[0] <= 0:
        cups.popleft()
    return cups

def fill_cups(cups, bottels, wasted_water):
    check_cup_value(cups)
    if bottels[-1] < cups[0]:
        cups[0] -= bottles[-1]
        bottels.pop()
    else:
        wasted_water += bottels[-1] - cups[0]
        cups.popleft()
        bottels.pop()
    return wasted_water

def print_result(cups, bottles, wasted_water):
    if cups:
        print(f"Cups: {' '.join(str(el) for el in cups)}")
    else:
        print(f"Bottles: {' '.join([str(el) for el in reversed(bottles)])}")
    print(f"Wasted litters of water: {wasted_water}")

cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]
wasted_water = 0

while True:
    if not bottles or not cups:
        break
    wasted_water = fill_cups(cups, bottles, wasted_water)

print_result(cups, bottles, wasted_water)