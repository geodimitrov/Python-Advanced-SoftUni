def reverse_list(nums):
    result = [el.split() for el in reversed(nums)]
    return result

def flatten_list(nums):
    result = [n for el in nums for n in el]
    return " ".join(result)

# read input data
nums = input().split("|")

# reverse and split the elements of the list
nums = reverse_list(nums)

# flatten the list and print the result
print(flatten_list(nums))