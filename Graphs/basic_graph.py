class Graphs:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):  #添加節點/頂點
        if node not in self.adjacentList:
            self.adjacentList[node] = []
            self.numberOfNodes += 1

    # 使用 in 關鍵字來判斷字典的鍵是否存在
    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            if node2 not in self.adjacentList[node1]:
                self.adjacentList[node1].append(node2)
            if node1 not in self.adjacentList[node2]:
                self.adjacentList[node2].append(node1)

    def showConnections(self):
        """
        印出圖的鄰接串列，用以視覺化連接關係。
        """
        # 取得所有節點的列表，並將其排序以確保輸出的一致性
        all_nodes = sorted(list(self.adjacentList.keys()))
        for node in all_nodes:
            connections = self.adjacentList[node]
            # 將相鄰節點列表轉換為字串，並用空格分隔
            print(f'{node} --> {" ".join(map(str, sorted(connections)))}')

myGraph = Graphs()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge("3", "1")
myGraph.addEdge("1", "3")
myGraph.addEdge("2", "3")
myGraph.addEdge("4", "2")
myGraph.showConnections()