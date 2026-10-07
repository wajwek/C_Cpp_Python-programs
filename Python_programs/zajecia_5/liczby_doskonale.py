a = int(input("Podaj liczbe: ")) #podajemy liczbe
suma = 0 #deklaracja
for i in range(1, a): #zaczynamy od 1 zeby nie dzielic przez 0, robimy do a - 1
    if a % i == 0: #jesli i jest dzielnikiem to 
        suma += i #dodaj go do sumy dzielnikow
    if suma >= a: #jesli suma jest rowna, albo nawet przekroczyla nasza liczbe to przerwij petle
        break #przerwanie
if suma == a: #czy jest doskonala
    print("Ta liczba jest doskonala") #jak tak to wypisz ze jest
else:#a jak nie
    print("Ta liczba nie jest doskonala") #to wypisz ze nie jest