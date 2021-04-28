from datetime import time, datetime, timedelta

END_COMMAND = "End"

def read_product_lines():
    result = []

    while True:
        command = input()

        if command == END_COMMAND:
            break

        result.append(command)

    return result

def read_input():
    robots_data = [el.split("-") for el in input().split(";")]
    starting_time = input()
    products = read_product_lines()

    return robots_data, starting_time, products


def create_robots_from_data(data):
    return {el[0]: [int(el[1]), int(el[1])] for el in data}


def format_starting_time(time):
    hours, minutes, seconds = time.split(":")
    result = datetime(100, 1, 1, int(hours), int(minutes), int(seconds))

    return result

def is_available(robots, robot):
    processing_capacity = robots[robot][0]
    passed_processing_time = robots[robot][0]
    return processing_capacity == passed_processing_time


def print_details(product, robot_name, time):
    print(f"{robot_name} - {product} [{time.time()}]")


def process_products(products, robots, start_time):
    robots_line = [robot for robot in robots]

    while products:

        start_time += timedelta(0, 1)
        processing_robot = robots_line[0]

        if is_available(robots, processing_robot):
            product = products.pop(0)
            robots_line.append(robots_line.pop(0))
            print_details(product, processing_robot, start_time)

robots_data, starting_time, products = read_input()
robots = create_robots_from_data(robots_data)
formatted_start_time = format_starting_time(starting_time)
process_products(products, robots, formatted_start_time)


'''
import datetime
a = datetime.datetime(100,1,1,11,34,59)
b = a + datetime.timedelta(0,3) # days, seconds, then other fields.
print(a.time())
print(b.time())
'''
