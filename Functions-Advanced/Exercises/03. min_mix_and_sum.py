def print_result(nums):
    print(f"The minimum number is {min(nums)}")
    print(f"The maximum number is {max(nums)}")
    print(f"The sum number is: {sum(nums)}")

nums = [int(el) for el in input().split()]
print_result(nums)