def flights(*args):
    FINISH = "Finish"
    result = {}

    for i in range(0, len(args), 2):
        destination = args[i]

        if destination == FINISH:
            break

        if destination not in result:
            result[destination] = 0

        passengers = args[i + 1]
        result[destination] += passengers

    return result

# Test code
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))