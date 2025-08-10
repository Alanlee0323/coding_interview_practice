def sellectionSort(list):
    for i in range(len(list)):
        min_index = i # 在每一輪開始時，假設當前元素就是最小的，並記錄其索引

        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:        
            list[i], list[min_index] = list[min_index], list[i]

    return list

num_list = [2, 65, 1, 34, 2, 1, 7, 8]
sorted_list = sellectionSort(num_list)
print("原始列表", num_list)
print("排序後的列表:", sorted_list)