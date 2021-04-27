from collections import deque


def is_valid_order(order):
    return 0 < order < 11


def print_result(result, total_pizza, employees, orders):

    if not result:
        print("Not all orders are completed.\n" \
              + f"Orders left: {', '.join(map(str, orders))}")

    else:
        print("All orders are successfully completed!\n" \
              + f"Total pizzas made: {total_pizza}\n" \
              + f"Employees: {', '.join(map(str, employees))}")


pizza_orders = deque(map(int, input().split(", ")))
employees = list(map(int, input().split(", ")))
orders_completed = True
total_pizza_made = 0

while pizza_orders:

    if not employees:
        orders_completed = False
        break

    pizza_order = pizza_orders.popleft()

    if is_valid_order(pizza_order):
        employee = employees.pop()

        if pizza_order > employee:
            pizza_remainder = pizza_order - employee
            pizza_orders.insert(0, pizza_remainder)
            total_pizza_made += employee

        else:
            total_pizza_made += pizza_order

print_result(orders_completed, total_pizza_made, employees, pizza_orders)