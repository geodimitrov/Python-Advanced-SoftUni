def split_negative_from_positive(nums):
    negative_nums = sum(filter(lambda x: x < 0, nums))
    positive_nums = sum(filter(lambda x: x > 0, nums))
    return negative_nums, positive_nums

def print_result(sum_negative, sum_positive):
    print(sum_negative)
    print(sum_positive)
    if abs(sum_negative) > sum_positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

numbers = [int(el) for el in input().split()]
sum_negative, sum_positive = split_negative_from_positive(numbers)
print_result(sum_negative, sum_positive)