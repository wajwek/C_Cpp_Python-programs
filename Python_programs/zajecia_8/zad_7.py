def zad_7():
    tab = input("Podaj wartości do talicy po spacji: ").split(" ")
    p = int(input("Podaj przesunięcie: "))
    new_tab = tab[-p:] + tab[:-p]
    print(new_tab)
zad_7()