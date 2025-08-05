class doublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value' : value,
            'next' : None,
            'preNode' : None
        }
        self.length = 1
        self.tail = self.head

    def append(self, value): # 在結尾加入一個新結點
        # 新節點資訊
        new_node = {
            'value' : value,
            'next': None,  # 因為是結尾，所以後面接 None
            'preNode' : self.tail
        }

        self.tail['next'] = new_node   # 本來的結尾指向現在的新節點
        self.tail = new_node    # 將本來的結尾更新
        self.length += 1    # 節點數量+1
        return self

    def prepend(self, value): # 在開頭加入一個新節點
        # 新結點資訊
        new_node = {
            'value': value,
            'next': self.head,   # 將新節點指向原本的開頭
            'preNode' : None
        }
        self.head['preNode'] = new_node
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
        
        leader = self.TraverseToIndex(index-1)  # 找到指定序列的前一個節點
        after = leader['next']

        new_node = {
            'value' : value,
            'next': leader['next'], # 新結點指向本來節點定義的下一個點
            'preNode' : leader 
        }

        leader['next'] = new_node   # 前一節點改指向新節點

        if after:   # 避免 after 插在最後
            after['preNode'] = new_node
        self.length += 1    # 節點數量+1
        return self
    
    def remove(self, index):
        # check data
        if index < 0 or index >= self.length:   # 不刪除任何節點
            return self
        
        if index == 0:  # 把頭刪掉
            self.head = self.head['next']
            self.head['preNode'] = None
            self.length -= 1
            return self
        
        leader = self.TraverseToIndex(index-1)  # 先找到要刪除節點的前一個節點
        Unwanted_node = leader['next']  #  找到要刪除的節點

        if Unwanted_node['next'] == None:
            self.tail = leader
            self.tail['next'] = None
        else:
            leader['next'] = Unwanted_node['next']
            Unwanted_node['next']['preNode'] = leader
        self.length -= 1

        return self
    
    def printDetailedList(self):
        current_node = self.head
        while current_node is not None:
            value = current_node['value']
            prev_val = current_node['preNode']['value'] if current_node['preNode'] else "None"
            next_val = current_node['next']['value'] if current_node['next'] else "None"
            print(f"Value: {value}, Prev: {prev_val}, Next: {next_val}")
            current_node = current_node['next']
        print("---")

    def reverse(self):
        if self.length == 1:
            return self
        else:
            self.tail = self.head
            current_node = self.head

            while current_node != None:
                temp = current_node["next"]
                current_node["next"] = current_node["preNode"]
                current_node["preNode"] = temp
                current_node = temp
                
            self.tail["next"] = None
            self.head = current_node["preNode"]
        return self

my_list = doublyLinkedList(10)
print(my_list.printDetailedList())

my_list.append(5) 
my_list.append(14)
my_list.prepend(8)
print(my_list.printDetailedList())

my_list.insert(2, 99)
print(my_list.printDetailedList())


my_list.remove(3)
print(my_list.printDetailedList())