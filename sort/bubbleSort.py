def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - i -1):
            if list[j] > list[j+1]:
                list[j+1], list[j]=  list[j], list[j+1]

    return list

num_list = [2, 65, 1, 34, 2, 1, 7, 8]
sorted_list = bubbleSort(num_list)
print("原始列表", num_list)
print("排序後的列表:", sorted_list)