def round_nums(nums):
    return [round(num) for num in nums]

nums = [float(el) for el in input().split()] #turn elements into floats
print(round_nums(nums))