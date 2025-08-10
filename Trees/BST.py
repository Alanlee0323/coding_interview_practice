class node:
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value

class BST:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        new_node = node(value)
        if self.root == None:
            self.root = new_node
            return
        
        current_node = self.root
        while True:
            if value > current_node.value:
                if current_node.right == None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right
            else:
                if current_node.left == None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
        

    def lookup(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left

    # def remove(self, value):

            


tree = BST()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
