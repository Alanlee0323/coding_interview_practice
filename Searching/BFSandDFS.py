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

    def breadthFirstSearch(self):
        if self.root == None:
            return None
        
        currentNode = self.root
        binarySearchResult = []
        queue = []
        queue.append(currentNode)
        
        while queue:
            currentNode = queue.pop(0)
            binarySearchResult.append(currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)
            
            if currentNode.right is not None:
                queue.append(currentNode.right)
        
        return binarySearchResult
    
    def TraverseInorder(self, node, list):
        if node.left is not None:
            self.TraverseInorder(node.left, list)
        list.append(node.value)
        if node.right is not None:
            self.TraverseInorder(node.right, list)
        return list
    
    def TraversePreorder(self, node, list):
        list.append(node.value)
        
        if node.left is not None:
            self.TraversePreorder(node.left, list)
        
        if node.right is not None:
            self.TraversePreorder(node.right, list)
        return list
    
    def TraversePostorder(self, node, list):
        if node.left is not None:
            self.TraverseInorder(node.left, list)
        if node.right is not None:
            self.TraverseInorder(node.right, list)
        list.append(node.value)
        return list
    
    def DFSInorder(self):
        return self.TraverseInorder(self.root, [])
    
    def DFSPreorder(self):
        return self.TraversePreorder(self.root, [])

    def DFSPostorder(self):
        return self.TraversePostorder(self.root, [])
    
    

tree = BST()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.breadthFirstSearch())
print(tree.DFSInorder())
print(tree.DFSPreorder())
print(tree.DFSPostorder())