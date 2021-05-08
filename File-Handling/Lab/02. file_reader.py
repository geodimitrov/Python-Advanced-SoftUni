
def get_nums_from_text(file):
    result = [int(line[:-1]) for line in file.readlines()]
    return result

with open("numbers.txt") as file:
    nums = get_nums_from_text(file)


print(sum(nums))