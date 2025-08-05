class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
   
    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value
    
    def set(self, key, value):
        address = self._hash(key)
        if (self.data[address] is None):
            self.data[address] = []
            self.data[address].append([key, value])
        else:
            self.data[address].append([key, value])
        return self.data
    
    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket is not None:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None
    
    def keys(self):
        KeyArray = []
        for items in self.data:
             if items is not None and len(items) > 0:
                KeyArray.extend([item[0] for item in items])
        return KeyArray

myhashtable = HashTable(10)
myhashtable.set('grapes', 10000)
myhashtable.set('ks', 2000)
myhashtable.set('apples', 100)
myhashtable.set('oranges', 10)
print(myhashtable.keys())
