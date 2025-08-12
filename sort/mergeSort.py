def mergeSort(arr):
    # 當陣列只剩一個元素時，它已經是排好序的了。
    if len(arr) <= 1:
        return arr
    
    mid_point = len(arr)//2

    left_arr = arr[:mid_point]
    right_arr = arr[mid_point:]

    L_sorted = mergeSort(left_arr)
    R_sorted = mergeSort(right_arr)

    return merge(L_sorted, R_sorted)


def merge(left, right):
    # 建立一個新的空列表，用來存放合併後的結果
    merged_list = []
    # 初始化左右兩個列表的指針
    i = 0  # left 列表的指針
    j = 0  # right 列表的指針

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i != len(left):
         merged_list.append(left[i])
         i += 1

    while j != len(right):
         merged_list.append(right[j])
         j += 1 

        
    return merged_list

# 測試
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_numbers = mergeSort(numbers)

print("原始列表:", numbers)
print("排序後的列表:", sorted_numbers)