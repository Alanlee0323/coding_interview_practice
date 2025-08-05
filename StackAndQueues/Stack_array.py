        
class Stack_Array:
    def __init__(self, value=None):
        self.list = []
        if value != None:
            self.list.append(value)

    def push(self, value):
        self.list.append(value)        
        return self
    
    def pop(self):
        if not self.list:
            return None           
        return self.list.pop()
    
    def peek(self):
        if not self.list:
            return None
        return self.list[-1]
