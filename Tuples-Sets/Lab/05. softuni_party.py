def fill_list(count):
    data = []
    for _ in range(count):
        data.append(input())
    return data

def arrived_to_party(end_command):
    guests = []
    while True:
        command = input()
        if not command == end_command:
            guests.append(command)
        else:
            break
    return guests

def print_result(list_guests):
    print(len(list_guests))
    for guest in sorted(list_guests):
        print(guest)

n = int(input())
reservations = set(fill_list(n))
guests_arrived = set(arrived_to_party("END"))

guests_not_arrived = reservations.difference(guests_arrived)
print_result(guests_not_arrived)