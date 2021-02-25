def create_intersection(data):
    ranges = []
    for el in data:
        start = int(el.split(",")[0])
        end = int(el.split(",")[1])
        range_nums = set(int(n) for n in range(start, end + 1))
        ranges.append(range_nums)
    intersection = ranges[0].intersection(ranges[1])
    return intersection

def create_and_store_intersections(n_lines):
    intersections = []
    for _ in range(n_lines):
        data = input().split("-")
        intersections.append(create_intersection(data))
    return intersections

def find_longest_intersec(list_intersections):
    longest_intersection = []
    for intersec in list_intersections:
        if len(intersec) > len(longest_intersection):
            longest_intersection = list(intersec)
    return longest_intersection

n = int(input())
intersections = create_and_store_intersections(n)
longest_intersection = find_longest_intersec(intersections)

print(f"Longest intersection is {longest_intersection} with length \
{len(longest_intersection)}")



