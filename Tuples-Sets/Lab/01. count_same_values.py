nums = map(float, input().split())
count_values = {}

for num in nums:
    if num not in count_values:
        count_values[num] = 0

    count_values[num] += 1

for key, value in count_values.items():
    print(f"{key} - {value} times")

