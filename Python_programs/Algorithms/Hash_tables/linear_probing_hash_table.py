class HashTable:
    def __init__(self, length):
        self.length = length
        self.arr = [None] * length
        self.arr_deleted = [False] * length

    def index(self, value):
        return value % self.length

    def add(self, value):
        idx = self.index(value)
        for i in range(self.length):
            pos = (idx + i) % self.length
            if self.arr[pos] is None:
                self.arr[pos] = value
                self.arr_deleted[pos] = False
                return print("Element added")
        return print("Array full")

    def delete(self, value):
        idx = self.index(value)
        for i in range(self.length):
            pos = (idx + i) % self.length
            if self.arr[pos] == value:
                self.arr[pos] = None
                self.arr_deleted[pos] = True
                return print("Deleted")
            elif not self.arr_deleted[pos] and self.arr[pos] is None:
                break
        return print("Element not found")

    def search(self, value):
        idx = self.index(value)
        for i in range(self.length):
            pos = (idx + i) % self.length
            if self.arr[pos] == value:
                return pos
            elif not self.arr_deleted[pos] and self.arr[pos] is None:
                return None
        return None

    def delete_v2(self, value):
        pos = self.search(value)
        if pos is not None:
            self.arr[pos] = None
            self.arr_deleted[pos] = True
            return print("Deleted")
        else:
            return print("Element not found")

    def display(self):
        print("Array:", self.arr)
        print("Deleted:", self.arr_deleted)

ht = HashTable(10)

print("=== TEST ADD ===")
ht.add(5)
ht.add(15)
ht.add(25)
ht.add(7)
ht.add(17)
ht.display()

print("\n=== TEST SEARCH ===")
print("Search 15:", ht.search(15))
print("Search 25:", ht.search(25))
print("Search 100:", ht.search(100))

print("\n=== TEST DELETE ===")
ht.delete(15)
ht.display()

print("\n=== TEST DELETE_V2 ===")
ht.delete_v2(25)
ht.display()

print("\n=== TEST SEARCH AFTER DELETE ===")
print("Search 25:", ht.search(25))

print("\n=== TEST ADD AFTER DELETE ===")
ht.add(35)
ht.display()
