
def recur_expression(nums, current_sum=0, result=""):
    if not nums:
        return result, current_sum

    result_plus = recur_expression(nums[1:], current_sum + nums[0], f"{result}+{nums[0]}")
    result_minus = recur_expression(nums[1:], current_sum - nums[0], f"{result}-{nums[0]}")
    return result_plus + result_minus

def print_result(result):
    formatted_result = "\n".join(f'{result[i]}={result[i+1]}' for i in range(0, len(result), 2))
    print(formatted_result)

nums = list(map(int, input().split(", ")))
result = recur_expression(nums)
print_result(result)