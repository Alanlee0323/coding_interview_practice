def sellectionSort(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

num_list = [2, 65, 1, 34, 2, 1, 7, 8]
sorted_list = sellectionSort(num_list)
print("原始列表", num_list)
print("排序後的列表:", sorted_list)