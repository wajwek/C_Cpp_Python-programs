def oblicz_srednia(liczby):
    if not liczby:
        print("Lista nie zawiera ocen")
        return
    suma = sum(liczby)
    return suma / len(liczby)

lista_ocen = []

wynik = oblicz_srednia(lista_ocen)

print(f"Twój wynik to: {wynik}. Gratulacje z okazji ukończenia obliczeń.")