class heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, item):
        self.heap.append(item)
        self.__swim(len(self.heap) - 1)

    def extract_max(self):
        
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__sink(0)
        return value

    def __swim(self, nums):
        while nums > 0 and self.heap[nums] > self.heap[(nums-1) // 2]:
            self.__swap((nums - 1) // 2, nums)
            nums = (nums - 1) // 2

    def __swap(self, j, k):
        self.heap[j], self.heap[k] = self.heap[k], self.heap[j]

    def __sink(self, start_point):
        while len(self.heap) > start_point * 2 + 1:
            next_point = start_point * 2 + 1

            if next_point + 1 < len(self.heap) and self.heap[next_point] < self.heap[next_point + 1]:
                next_point += 1
            
            if self.heap[start_point] >= self.heap[next_point]:
                break

            self.__swap(next_point, start_point)
            start_point = next_point
            

            