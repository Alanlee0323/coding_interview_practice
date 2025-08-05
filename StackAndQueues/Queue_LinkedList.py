class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value=None):
        if value == None:
            self.length = 0
            self.last = None
            self.first = None
        else:
            new_node = node(value)
            self.length = 1
            self.last = new_node
            self.first = new_node
    
    def push(self, value):
        new_node = node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node          
            
        self.length += 1
        return self
    
    def pop(self):
        popped_data = self.first.value
        if self.length <= 1:
            self.first = None
            self.last = None
            self.length = 0
        else:
            self.first = self.first.next
            self.length -= 1
        return popped_data
    
    def peek(self):
        if self.length == 0:
            return None
        return self.first.value
    
myqueue = Queue()
myqueue.push(2)
myqueue.push(8)
myqueue.push(3)
print(myqueue.peek())
print(myqueue.pop())
print(myqueue.peek())
print(myqueue.pop())
print(myqueue.peek())
print(myqueue.pop())
print(myqueue.peek())