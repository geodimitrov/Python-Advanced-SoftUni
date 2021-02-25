nums = [int(num) for num in input().split()]

print(list(filter(lambda x: x % 2 ==0, nums)))