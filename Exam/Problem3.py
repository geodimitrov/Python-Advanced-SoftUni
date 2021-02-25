from collections import deque

def execute_sell_order(sell_order, flavors):
    if isinstance(sell_order[0], int):
        [flavors.popleft() for _ in range(sell_order[0])]
    else:
        sold_flavors = sell_order
        for flavor in sold_flavors:
            if flavor in flavors:
                flavor_count = flavors.count(flavor)
                for i in range(flavor_count):
                    flavors.remove(flavor)

def stock_availability(*args):
    flavors = deque(args[0])
    command_type = args[1]

    if command_type == "delivery":
        new_flavors = args[2:]
        [flavors.append(el) for el in new_flavors]

    else:
        sell_order = args[2:]
        if sell_order:
            execute_sell_order(sell_order, flavors)
        else:
            flavors.popleft()

    return list(flavors)

# # print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# # print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))