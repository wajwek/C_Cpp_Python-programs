def suma_kwadratow(x):
    suma = 0
    while x > 0:
        suma += pow(x % 10, 2)
        x = int(x / 10)
    return suma
    
def czy_szczesliwa(x):
    tab = []
    while x != 1:
        tab.append(x)
        x = suma_kwadratow(x)
        if x in tab:
            return False
    return True

def zad_1():
    a = int(input("Podaj początek zakresu: "))
    b = int(input("Podaj koniec zakresu: "))
    szcz = []
    licznik = 0
    maks = 0
    for i in range(a, b + 1):
        if czy_szczesliwa(i):
            szcz.append(i)
            licznik += 1
    print(szcz)
    print("Licznik: ", licznik)
    print("Max", max(szcz))
    print("Procent: ", str(round(licznik/(b + 1 - a ) * 100, 2)) + "%")
zad_1()
        
