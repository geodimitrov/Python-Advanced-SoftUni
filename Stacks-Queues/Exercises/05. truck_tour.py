from collections import deque

def fill_pump_data(n_pumps):
    result = deque()
    for _ in range(n_pumps):
        pump_data = tuple(map(int, input().split()))
        result.append(pump_data)
    return result

n = int(input())
N_STATIONS = n
pump_data = fill_pump_data(n)
mission_success = False

for i in range(len(pump_data)):
    pump_index = i
    tank = 0
    counter = 0

    for pump in pump_data:
        petrol, distance = pump
        if tank + petrol < distance:
            pump_data.append(pump_data.popleft())
            break
        else:
            tank += petrol - distance
            counter += 1

    if counter == N_STATIONS:
        break

print(pump_index)



