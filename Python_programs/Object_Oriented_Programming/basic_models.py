class Counter():
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value}"
    def inc(self, x):
        self.value += x
    def dec(self, x):
        self.value -= x
    def reset(self):
        self.value = 0

licznik = Counter(5)
print(licznik)
licznik.inc(10)
licznik.dec(5)
print(licznik)
licznik.reset()
print(licznik)
    


