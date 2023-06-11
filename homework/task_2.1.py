def minimum(arr):
    if len(arr) == 0:
        return None

    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num

    return min_num


def maximum(arr):
    if len(arr) == 0:
        return None

    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num

    return max_num