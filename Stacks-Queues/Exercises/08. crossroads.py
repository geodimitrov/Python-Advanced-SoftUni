from collections import deque

def car_exits_successfully(car, free_window_duration):
    if car <= free_window_duration:
        return True

def green_light(cars, passed_cars, crash, green_light_duration, free_window_duration):
    green_light = green_light_duration
    crash_index = 0

    while green_light > 0 and cars:
        car = len(cars[0])
        if car <= green_light:
            passed_cars += 1
            green_light -= car
        else:
            car -= green_light
            exit_range = green_light + free_window_duration
            green_light = 0

            if car_exits_successfully(car, free_window_duration):
                passed_cars += 1
            else:
                crash_index = exit_range
                crash = True
                break

        cars.popleft()

    return cars, passed_cars, crash, crash_index


def read_commands(cars, passed_cars, crash, green_light_duration, free_window_duration):
    command = input()

    while not command == "END":

        if command == "green":
            cars, passed_cars, crash, crash_index = green_light\
                (cars, passed_cars, crash, green_light_duration, free_window_duration)
        else:
            cars.append(command)

        if crash:
            break

        command = input()

    return cars, passed_cars, crash, crash_index


def print_result(cars, passed_cars, crash, crash_index):
    if crash:
        crashed_car = cars.popleft()
        crashed_index_element = crashed_car[crash_index]
        print("A crash happened!")
        print(f"{crashed_car} was hit at {crashed_index_element}.")
    else:
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")


green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
passed_cars = 0
crash = False

cars, passed_cars, crash, crash_index = read_commands(cars, passed_cars, crash, green_light_duration, free_window_duration)
print_result(cars, passed_cars, crash, crash_index)