class Hash_table:
    def __init__(self, length):
        self.length = length
        self.arr = [[] for _ in range(length)]
    
    def index(self, wartosc):
        return wartosc % self.length
    
    def add(self, wartosc):
        idx = self.index(wartosc)
        self.arr[idx].append(wartosc)
    
    def search(self, wartosc):
        idx = self.index(wartosc)
        for i in range(len(self.arr[idx])):
            if self.arr[idx][i] == wartosc:
                return idx, i
        return None, None
        
    def delete(self, wartosc):
        idx, pos = self.search(wartosc)
        if idx is not None and pos is not None:
            self.arr[idx].pop(pos)
            return print("Usunięto element")
        else:
            return print("Brak elementu")
            
ht = Hash_table(5)

print("TEST 1: dodawanie")
ht.add(1)
ht.add(6)
ht.add(11)
print(ht.arr)

print("TEST 2: szukanie")
print(ht.search(1))
print(ht.search(6))
print(ht.search(11))
print(ht.search(100))

print("TEST 3: usuwanie")
ht.delete(6)
print(ht.arr)

print("TEST 4: usuwanie nieistniejącego")
ht.delete(100)
print(ht.arr)
        