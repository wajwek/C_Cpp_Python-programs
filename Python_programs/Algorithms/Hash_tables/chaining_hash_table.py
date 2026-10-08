class HashTable:
    def __init__(self, length):
        self.length = length
        self.arr = [[] for _ in range(length)]
    
    def index(self, value):
        return value % self.length
    
    def add(self, value):
        idx = self.index(value)
        self.arr[idx].append(value)
    
    def search(self, value):
        idx = self.index(value)
        for i in range(len(self.arr[idx])):
            if self.arr[idx][i] == value:
                return idx, i
        return None, None
        
    def delete(self, value):
        idx, pos = self.search(value)
        if idx is not None and pos is not None:
            self.arr[idx].pop(pos)
            return print("Element deleted")
        else:
            return print("Element not found")
            
ht = HashTable(5)

print("TEST 1: adding")
ht.add(1)
ht.add(6)
ht.add(11)
print(ht.arr)

print("TEST 2: searching")
print(ht.search(1))
print(ht.search(6))
print(ht.search(11))
print(ht.search(100))

print("TEST 3: deleting")
ht.delete(6)
print(ht.arr)

print("TEST 4: deleting non-existent")
ht.delete(100)
print(ht.arr)
