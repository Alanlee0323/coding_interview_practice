def insertionSort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]: # 如果新加入的比最右邊的小
            list[j+1] = list[j] #現有元素往右移直到找到比右邊的大
            j -= 1
        
        list[j+1] = key
                    
    return list

num_list = [2, 65, 1, 34, 2, 1, 7, 8]
sorted_list = insertionSort(num_list)
print("原始列表", num_list)
print("排序後的列表:", sorted_list)

