start = int(input())
end = int(input())

def is_divisible(x):
    if any(x % i == 0 for i in range(2, 11)):
        return True

result = [x for x in range(start, end+1) if is_divisible(x)]
print(result)