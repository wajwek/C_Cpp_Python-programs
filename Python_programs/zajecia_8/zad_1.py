def zad_1():
    liczby = [x for x in range(1, 21)]
    podzielne = [z for z in liczby if z % 3 == 0]
    print(podzielne)
    print(sum(podzielne))
zad_1()
