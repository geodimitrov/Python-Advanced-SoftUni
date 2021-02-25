nums = [int(n) for n in input().split()]
nums_stack = []

while nums:
    nums_stack.append(nums.pop())

print(*nums_stack, sep=" ")