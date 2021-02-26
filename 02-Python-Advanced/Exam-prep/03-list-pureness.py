def calc_pureness(nums_list):
    return sum([i * nums_list[i] for i in range(len(nums_list))])


def rotate(nums_list):
    nums_list.insert(0, nums_list.pop())


def best_list_pureness(nums_list, k):
    count_rotations = 0
    pureness_value = calc_pureness(nums_list)
    for rotation_index in range(k + 1):
        pureness = calc_pureness(nums_list)
        if pureness > pureness_value:
            pureness_value = pureness
            count_rotations = rotation_index
        rotate(nums_list)
    return f"Best pureness {pureness_value} after {count_rotations} rotations"


nums_list = [4, 3, 2, 6]
k = 4
best_list_pureness(nums_list, k)
