class Return_Duplicate:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def _hash(self, key): #O(1)
        return key % self.size
    
    def get_address(self, key): #O(1)
        address = self._hash(key)
        return address
    
    def return_duplicate(self, GivenArray): #O(n)
        array = self.data
        for i in range(len(GivenArray)):
            if array[self.get_address(GivenArray[i])] == 1:
                return GivenArray[i]
            else:
                array[self.get_address(GivenArray[i])] = 1
        return None



Return = Return_Duplicate(2000)
GivenArray = [2, 5, 5, 2, 3, 5, 1, 2, 4]

print(Return.return_duplicate(GivenArray))

# Python 內建字典版本
def find_first_duplicate(array):
    seen = {}  # 創建空字典
    
    for num in array:
        # 如果數字已經在字典中，表示找到重複值
        if num in seen:
            return num
        # 否則將該數字加入字典
        seen[num] = 1
    
    # 如果沒有找到重複值，返回 None
    return None

# 測試
GivenArray = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(find_first_duplicate(GivenArray))  # 會輸出 2