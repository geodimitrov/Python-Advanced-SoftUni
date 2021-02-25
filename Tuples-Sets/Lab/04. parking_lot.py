def fill_list(count):
    list = []
    for _ in range(count):
        list.append(input())
    return list

n = int(input())
data = fill_list(n)
car_numbers = set()

for car_num in data:
    command, number = car_num.split(", ")

    if command == "IN":
        car_numbers.add(number)
    else:
        car_numbers.remove(number)

if car_numbers:
    for car_num in car_numbers:
        print(car_num)
else:
    print("Parking Lot is Empty")