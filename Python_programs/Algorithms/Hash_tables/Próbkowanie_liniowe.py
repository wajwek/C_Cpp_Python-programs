class Hash_table:
    def __init__(self, length):
        self.length = length
        self.arr = [None] * length
        self.arr_deleted = [False] * length

    def index(self, wartosc):
        return wartosc % self.length

    def add(self, wartosc):
        idx = self.index(wartosc)
        for i in range(self.length):
            pos = (idx + i) % self.length
            if self.arr[pos] is None:
                self.arr[pos] = wartosc
                self.arr_deleted[pos] = False
                return print("Dodano element")
        return print("Tablica pełna")

    def delete(self, wartosc):
        idx = self.index(wartosc)
        for i in range(self.length):
            pos = (idx + i) % self.length
            if self.arr[pos] == wartosc:
                self.arr[pos] = None
                self.arr_deleted[pos] = True
                return print("Usunięto")
            elif not self.arr_deleted[pos] and self.arr[pos] is None:
                break
        return print("Brak elementu")

    def search(self, wartosc):
        idx = self.index(wartosc)
        for i in range(self.length):
            pos = (idx + i) % self.length
            if self.arr[pos] == wartosc:
                return pos
            elif not self.arr_deleted[pos] and self.arr[pos] is None:
                return None
        return None

    def delete_v2(self, wartosc):
        pos = self.search(wartosc)
        if pos is not None:
            self.arr[pos] = None
            self.arr_deleted[pos] = True
            return print("Usunięto")
        else:
            return print("Brak elementu")

    def display(self):
        print("Tablica:", self.arr)
        print("Deleted:", self.arr_deleted)

ht = Hash_table(10)

print("=== TEST ADD ===")
ht.add(5)
ht.add(15)
ht.add(25)
ht.add(7)
ht.add(17)
ht.display()

print("\n=== TEST SEARCH ===")
print("Szukanie 15:", ht.search(15))
print("Szukanie 25:", ht.search(25))
print("Szukanie 100:", ht.search(100))

print("\n=== TEST DELETE ===")
ht.delete(15)
ht.display()

print("\n=== TEST DELETE_V2 ===")
ht.delete_v2(25)
ht.display()

print("\n=== TEST SEARCH PO DELETE ===")
print("Szukanie 25:", ht.search(25))

print("\n=== TEST ADD PO DELETE ===")
ht.add(35)
ht.display()