def best_list_pureness(*data):
    nums, k = data
    rotation = 0
    max_sum = 0
    max_sum_rotation = rotation

    for _ in range(k+1):
        sum_variation = 0
        for i in range(len(nums)):
            sum_variation += nums[i] * i
            if sum_variation > max_sum:
                max_sum = sum_variation
                max_sum_rotation = rotation

        nums.insert(0, nums.pop())
        rotation += 1

    return f"Best pureness {max_sum} after {max_sum_rotation} rotations"