class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value=None):
        if value == None:
            self.top = None
            self.bottom = None
            self.length = 0
        else:
            new_node = node(value)
            self.top = new_node
            self.bottom = new_node
            self.length = 1   

    def push(self, value):
        new_node = node(value)

        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
        self.length += 1
        return self
    
    def pop(self):
        popped_data = self.top.value
        if self.length <= 1:
            self.top = None
            self.bottom = None
            self.length = 0
        else:
            self.top = self.top.next
            self.length -= 1
        return popped_data
    
    def peek(self):
        if self.length == 0:
            return None
        return self.top.value
    
    
    
mystack = Stack()
mystack.push(2)
mystack.push(8)
print(mystack.peek())
mystack.pop()
print(mystack.peek())
