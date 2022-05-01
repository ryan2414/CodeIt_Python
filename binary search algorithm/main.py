def binary_search(element, some_list):
    start_index = 0
    last_index = len(some_list) - 1

    # if some_list[start_index] > element or some_list[last_index] < element:
    #     return None

    while start_index <= last_index:
        mid_idx = (start_index + last_index) // 2

        if some_list[mid_idx] > element:
             last_index = mid_idx - 1
        elif some_list[mid_idx] == element:
            return mid_idx
        else:
            start_index = mid_idx + 1

    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
