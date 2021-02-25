from collections import deque

food_qty = int(input())
#split the data and use list comprehension to create list of ints, then dequeue it
order_data = [int(el) for el in input().split()]
print(max(order_data))   #find max number & print it

queue = deque([str(el) for el in order_data])

for order in order_data:

    if order <= food_qty:
        food_qty -= order
        queue.popleft()
    else:
        break

if queue:
    orders_left = " ".join(queue)
    print(f"Orders left: {orders_left}")
else:
    print("Orders complete")