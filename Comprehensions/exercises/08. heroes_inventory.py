def run_command(command, inventory):
    name, item, item_cost = command.split("-")
    if item not in inventory[name]:
        inventory[name][item] = int(item_cost) #turn it into int to calc total cost when printing the result
    return inventory

def get_result(name, items):
    num_items = len(items)
    total_cost = sum([cost for item, cost in items.items()])
    return f"{name} -> Items: {num_items}, Cost: {total_cost}"

def print_result(inventory):
    for name, items in inventory.items():
        print(get_result(name, items))

#read input
names = input().split(", ")

#created nested dictionaries for all names
inventory = {name: {} for name in names}

#use while loop to read and run commands
while True:
    command = input()

    if command == "End":
        break
    else:
        run_command(command, inventory)

#creat func to print the result
print_result(inventory)