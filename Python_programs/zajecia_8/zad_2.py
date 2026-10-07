import random
tab = ["Ania", "Kasia", "Włodzimierz", "Kazimierz", "Lucjan"]
imiona = []
def zad_2():
    print("Podaj 5 imon")
    for i in range(5):
        x = input(str(i + 1) +  ". Imię: ")
        imiona.append(x)

    imiona[:] = [tab[int(random.randint(0,4))] if x == "" else x for x in imiona]

    if "Anna" in imiona:
        print("W zbiorze jest imię Anna")
        
    print("Wpisz imię które chcesz zamienić z niżej podanych:")
    print(imiona)
    zmiana = int(input("Index: "))
    nowe = input("Zmieniam na: ")
    imiona[zmiana] = nowe

    print("Gotowe")
    print(imiona)
zad_2()
