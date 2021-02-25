def print_result(time, collection):
    if collection:
        print("Not all customers were driven to their destinations")
        print(f'Customers left: {", ".join(map(str,collection))}')
    else:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")

customers = [int(el) for el in input().split(", ")]
taxi_drivers = [int(el) for el in input().split(", ")]
total_time = 0

while customers and taxi_drivers:
    customer = customers[0]
    taxi_driver = taxi_drivers[-1]

    if taxi_driver >= customer:
        total_time += customer
        customers.pop(0)
        taxi_drivers.pop()
    else:
        taxi_drivers.pop()

print_result(total_time, customers)