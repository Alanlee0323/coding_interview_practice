class node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class doublyLinkedList:
    def __init__(self, value=None):
        if value == None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def append(self, value): # 在結尾加入一個新結點
        # 新節點資訊
        new_node = node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self