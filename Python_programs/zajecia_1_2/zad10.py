h = int(input("Podaj wysokosc:"))
if h > 0:
    ilosc_gwiazdek = 1
    pieniek = True
for i in range(h):
    print(" " * (h - i) + "*" * ilosc_gwiazdek)
    ilosc_gwiazdek += 2
if pieniek:
    print(" " * h + "*")
