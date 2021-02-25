def is_even(n):
    if n % 2 == 0:
        return True

def is_positive(n):
    if n >= 0:
        return True

def get_result(collection):
    result = [str(x) for x in collection]
    return ", ".join(result)

numbers = [int(x) for x in input().split(", ")]

positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for n in numbers:
    if is_positive(n):
        positive_nums.append(n)
    else:
        negative_nums.append(n)
    if is_even(n):
        even_nums.append(n)
    else:
        odd_nums.append(n)

print(f"Positive: {get_result(positive_nums)}")
print(f"Negative: {get_result(negative_nums)}")
print(f"Even: {get_result(even_nums)}")
print(f"Odd: {get_result(odd_nums)}")