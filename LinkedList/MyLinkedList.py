class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1
    
    def append(self, value): # 在結尾加入一個新結點
        # 新節點資訊
        new_node = {
            'value' : value,
            'next': None # 因為是結尾，所以後面接 None
        }

        self.tail['next'] = new_node   # 本來的結尾指向現在的新節點
        self.tail = new_node    # 將本來的結尾更新
        self.length += 1    # 節點數量+1
        
        return self
    
    def prepend(self, value): # 在開頭加入一個新節點
        # 新結點資訊
        new_node = {
            'value': value,
            'next': self.head   # 將新節點指向原本的開頭
        }
        self.head = new_node    # 將本來的起始點更新為現在的新節點
        self.length += 1    # 節點數量+1
        return self
    
    def printList(self):    # 利用 Key:Value 的方式去取出我們剛剛定義的節點資訊
        array = []
        CurrentNode = self.head     # 從起始點開始找
        while (CurrentNode != None):    # 只要起始點還沒找到最後的 None
            array.append(CurrentNode['value'])  # 就將目前走到的起始點數值加入 array 中
            CurrentNode = CurrentNode['next']   # 將起始點更新為下一個點
        return array

    def TraverseToIndex(self, index): # 插入需要 O(n) 的原因
        counter = 0
        CurrentNode = self.head
        while(counter != index):
            CurrentNode = CurrentNode['next']
            counter += 1
        return CurrentNode

    def insert(self, index, value): # 在指定序列位置插入數值 
        # 輸入資料檢查
        if index >= self.length:    # 新增的 index 超過本來的 list 長度代表加入在最尾端
            return self.append(value)   # 直接使用前面定義過的 append 加在最後
        if not isinstance(index, int):
            raise ValueError('索引數值請輸入正整數')
        
        if index == 0:
            return self.prepend(value)
        
        new_node = {
            'value' : value,
            'next': None
        }
        leader = self.TraverseToIndex(index-1)  # 找到指定序列的前一個節點
        new_node['next'] = leader['next']   # 新結點指向本來節點定義的下一個點
        leader['next'] = new_node   # 前一節點改指向新節點
        self.length += 1    # 節點數量+1
        return self
    
    def remove(self, index):
        # check data
        if index < 0 or index >= self.length:   # 不刪除任何節點
            return self
        
        if index == 0:  # 把頭刪掉
            self.head = self.head['next']
            self.length -= 1
            return self
        
        leader = self.TraverseToIndex(index-1)  # 先找到要刪除節點的前一個節點
        Unwanted = self.TraverseToIndex(index)  #  找到要刪除的節點
        
        if index == self.length - 1:    # 把尾刪掉
            self.tail = leader
            self.tail["next"] = None

        leader['next'] = Unwanted['next']   # 把要刪除節點的前一個節點接到刪除節點本來的下一個點
        
        self.length -= 1
        return self
    
    def reverse(self):
        if self.head["next"] == None:
            return self
        else:
            self.tail = self.head
            first = self.head
            second = first["next"]
            while second != None:
                temp = second["next"]
                second["next"] = first
                first = second
                second = temp
            self.head = first
            self.tail["next"] = None
            return self
            


my_list = LinkedList(10)
print(my_list.printList())

my_list.append(5) 
my_list.append(14)
my_list.prepend(8)
print(my_list.printList())
print(my_list.TraverseToIndex(2))

my_list.insert(2, 99)
print(my_list.printList())

my_list.remove(6)
print(my_list.printList())
print(my_list.reverse().printList())
