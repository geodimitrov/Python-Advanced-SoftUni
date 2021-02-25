def run_command(command, list_nums, length):
    if command == "Even":
        result = sum([num for num in list_nums if num % 2 == 0])
    else:
        result = sum([num for num in list_nums if not num % 2 == 0])

    return result * length

command = input()
nums = [int(el) for el in input().split()]
LENGTH = len(nums) #the length of the list of all nums
print(run_command(command, nums, LENGTH))