def get_evens(nums):
    return list(filter(lambda x: x % 2 ==0, nums))

def print_evens(even_nums):
    print(even_nums)

nums = [int(num) for num in input().split()]
even_nums = get_evens(nums)
print_evens(even_nums)