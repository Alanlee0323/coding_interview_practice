class MergeSortedArrays:
    
    def Validate_input(self, arr1, arr2):
        # 型別檢查
        if not isinstance(arr1, list) or not isinstance(arr2, list):
            raise TypeError("輸入必須是列表")
        
        # 元素型別檢查
        if not all(isinstance(x, (int, float)) for x in arr1 + arr2):
            raise TypeError("列表必須只包含數字")
        
        # 排序檢查
        if arr1 != sorted(arr1) or arr2 != sorted(arr2):
            raise ValueError("輸入陣列必須是升序排列")
        
        # 非空檢查
        if len(arr1) == 0 or len(arr2) == 0:
            raise ValueError("輸入陣列不能為空")
    
    def MergeArrays(self, arr1, arr2):
        self.Validate_input(arr1, arr2)

        NewArray = []
        i, j= 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                NewArray.append(arr1[i])
                i += 1
            else:
                NewArray.append(arr2[j])
                j += 1

        # 添加 arr1 剩餘元素
        while i < len(arr1):
            NewArray.append(arr1[i])
            i += 1
        
        # 添加 arr2 剩餘元素
        while j < len(arr2):
            NewArray.append(arr2[j])
            j += 1

        return NewArray
    
Combine = MergeSortedArrays()

A = [1, 4, 5, 8, 21, 25, 37]
B = [4, 6, 30]
print(Combine.MergeArrays(A, B))