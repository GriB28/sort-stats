def bubble(array: list[int], length: int):
    for i in range(length):
        breaker = True
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                breaker = False
        if breaker:
            break


def do_merge(array: list[int], left: int, middle: int, right: int):
    left_length = middle - left + 1
    right_length = right - middle
    left_sublist = [array[left + i] for i in range(left_length)]
    right_sublist = [array[middle + 1 + i] for i in range(right_length)]
    i = 0
    j = 0
    k = left

    while i < left_length and j < right_length:
        if left_sublist[i] <= right_sublist[j]:
            array[k] = left_sublist[i]
            i += 1
        else:
            array[k] = right_sublist[j]
            j += 1
        k += 1

    while i < left_length:
        array[k] = left_sublist[i]
        k += 1
        i += 1
    while j < right_length:
        array[k] = right_sublist[j]
        k += 1
        j += 1

def merge_shell(array: list[int], left: int, right: int):
    if left < right:
        middle = left + (right - left) // 2

        merge_shell(array, left, middle)
        merge_shell(array, middle + 1, right)

        do_merge(array, left, middle, right)

def merge(array: list[int], length: int):
    merge_shell(array, 0, length - 1)
