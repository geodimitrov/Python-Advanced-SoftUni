def find_duplicates(nums):
    result = []
    for num in nums:
        if nums.count(num) > 1 and num not in result:
            result.append(num)
            nums.remove(num)
    return result, nums

def find_missing_nums(nums):
    missing_nums = []
    for n in range(min(nums), max(nums)):
        if n not in nums:
            missing_nums.append(n)
    return missing_nums

def numbers_searching(*nums):
    duplicates, nums = find_duplicates(list(nums))
    result = find_missing_nums(nums)
    result.append(sorted(duplicates))
    return result

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))