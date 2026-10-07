n = int(input("Podaj zakres górny: ")) #Podajemy zakres
licznik = 0 #Deklaracja
for x in range(2, n + 1): #Pętla od 2 do n włącznie
    bol = 0 #Deklaracja
    if x == 2: #Nie wchodzimy do petli bo 2 jest liczba pierwsza
        licznik += 1 #inkrementacja
    else: #jak if nie jest spelniony to:
        for i in range(2, int(n ** (1/2) + 1)): #nie ma sensu szukac wyzej niz pierwiastek z n bo na pewno nie bedzie tam dzielnika
            if x % i == 0: #czy i dzieli x bez reszty?
                bol = 1 #Zaznaczenie zmiany, pojawil sie dzielnik, wiec nie jest pierwsza
                break #wyjscie z petli, mozna bez, ale po co ma sie liczyc
    if bol == 0: #czy nie wykrylo zadnego dzielnika?
        licznik += 1 #jak nie wykryto to inkrementuj
print(licznik) #wyswietl wynik

        