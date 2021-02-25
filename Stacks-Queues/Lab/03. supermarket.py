#Solution 1

# Make sure you import the deque function
from collections import deque

#Use constants to start getting used to good practices
END_COMMAND = "End"
PAID_COMMAND = "Paid"
names_queue = deque()

while True:
    command = input()

    if command == END_COMMAND:
        print(f"{len(names_queue)} people remaining.")
        break
    elif command == PAID_COMMAND:
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)