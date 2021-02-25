def turn_nums_to_absolute(nums):
    return [abs(num) for num in nums]

nums = [float(el) for el in input().split()] #turn elements into floats
print(turn_nums_to_absolute(nums))