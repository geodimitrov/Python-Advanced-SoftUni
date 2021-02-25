def add_nums_to_list(nums, second_param, nums_to_add):
    if second_param == "beginning":
        return list(nums_to_add) + nums

    else:
        return nums + list(nums_to_add)

def remove_nums_to_list(nums, second_param, nums_to_remove):
    if second_param == "beginning":
        if nums_to_remove:
            value = nums_to_remove[0]
            return nums[value: len(nums)]
        else:
            return nums[1:len(nums)]
    else:
        if nums_to_remove:
            value = nums_to_remove[0]
            return nums[:len(nums) - value]
        else:
            return nums[:len(nums) - 1]


def list_manipulator(nums, first_param, second_param, *args):

    if first_param == "add":
        return add_nums_to_list(nums, second_param, args)
    else:
        return remove_nums_to_list(nums, second_param, args)