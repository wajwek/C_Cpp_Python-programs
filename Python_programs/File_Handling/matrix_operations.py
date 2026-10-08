def wczytaj_dane(sciezka):
    try:
        with open(sciezka, 'r') as f:
            tresc = f.read().split()
            n = int(tresc[0])
            macierz_a = []
            macierz_b = []
            licznik = 1
            for x in range(2):
                macierz = []
                for i in range(n):
                    wiersz = []
                    for j in range(n):
                        wiersz.append(int(tresc[licznik]))
                        licznik += 1
                    macierz.append(wiersz)
                if x == 0:
                    macierz_a = macierz
                else:
                    macierz_b = macierz
        return n, macierz_a, macierz_b
    except FileNotFoundError:
        return None, None, None
    
def dodawanie(A, B, n):
    C = []
    for i in range(n):
        wiersz = []
        for j in range(n):
            suma = A[i][j] + B[i][j]
            wiersz.append(suma)
        C.append(wiersz)
    return C

def mnozenie(A, B, n):
    C = [[0]*n for x in range(n)] # [[0] *n]*n nie działa, bo python dodaje referencje w pamięci na odpowiadających pozycjach :(
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def zapisz_macierz(plik, macierz, komunikat):
    with open(plik, 'a') as plik:
        wszystkie_liczby = [str(x) for wiersz in macierz for x in wiersz]
        szerokosc = len(max(wszystkie_liczby, key=len)) + 1 
        plik.write(f"--------------- {komunikat} ----------------\n")
        for wiersz in macierz:
            linia = ""
            for liczba in wiersz:
                linia += f"{liczba:>{szerokosc}}"
            plik.write(linia + "\n")
    plik.close()

def przetworz_macierze(plik_wejsciowy, plik_wyjsciowy):
    dane = wczytaj_dane(plik_wejsciowy)
    n, A, B = dane

    suma = dodawanie(A, B, n)
    iloczyn = mnozenie(A, B, n)

    with open(plik_wyjsciowy, 'w') as f:
        zapisz_macierz("wynik.txt", A, "Macierz A")
        zapisz_macierz("wynik.txt", B, "Macierz B")
        zapisz_macierz("wynik.txt", suma, "Suma A+B")
        zapisz_macierz("wynik.txt", iloczyn, "Iloczyn A*B")

with open("wynik.txt", 'w') as plik:
    plik.close()
przetworz_macierze('dane.txt', 'wynik.txt')