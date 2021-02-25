from collections import deque

water = int(input())
people = deque()

#create the queue
while True:
    command = input()
    if command == 'Start':
        break
    else:
        people.append(command)

#start water consumption
while True:
    command = input()

    if command == "End":
        print(f"{water} liters left")
        break
    elif command.startswith("refill"):
        qty_refill = int(command.split()[1])
        water += qty_refill
    else:
        person_water = int(command)
        person = people.popleft()
        if person_water > water:
            print(f"{person} must wait")
        else:
            water -= person_water
            print(f"{person} got water")