import random

def zad_5():
    liczby = []
    wystepowanie = {}
    for i in range(20):
        x = int(random.randint(1,10))
        liczby.append(x)
        wystepowanie[x] = 0
    for liczba in liczby:
        wystepowanie[liczba] += 1
    for i in set(liczby):
        print(i, "wystąpiło:", wystepowanie[i], "razy")
zad_5()
