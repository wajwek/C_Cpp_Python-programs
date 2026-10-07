def zad_8():
    poz = input("Podaj pozycję skoczka: ")
    x = int(ord(poz[0]) - ord("a") + 1) # zamiana np. e na 5 na bazie wartosci ascii, + 1 jest po to aby pozycja a odpowiadała 1 a nie 0
    y = int(poz[1])
    options = [-2, -1, 1, 2]
    for i in options:
        for j in options:
            if j == i or i == -j:
                continue
            if 1 <= x + i <= 8 and 1 <= y + j <= 8:
                print("Możliwe ruchy:", chr((x + i - 1) + ord("a")) + str(y + j))
zad_8()
