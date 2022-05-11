# # 두 요소의 위치를 바꿔주는 helper function
# def swap_elements(my_list, index1, index2):
#     pivot = index2
#     b = 0
#     for idx in range(index1, pivot):
#         if my_list[idx] < my_list[pivot]:
#             my_list[b], my_list[idx] = my_list[idx], my_list[b]
#             b += 1
#
#     if my_list[pivot - 1] > my_list[pivot]:
#         my_list[b], my_list[pivot] = my_list[pivot], my_list[b]
#
#     return my_list
#
#
# # 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
#     if start == end
#         return my_list[start]
#
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    b = start
    for i in range(start,end):
        if my_list[i] < my_list[end]:
            swap_elements(my_list, i, b)
            b += 1

    swap_elements(my_list, b, end)
    return b



# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
