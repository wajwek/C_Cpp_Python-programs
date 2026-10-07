#Preferowane rozwiazanie(wolniejsze, ale bardziej intuicyjne(przynajmniej dla mnie))

def zamiana_na_bin(x): #Deklarujemy funkcję
    reszty = [] #Tworzymy tablice
    while x >= 1: #Dopóki x wiekszy bądź równy 1
        reszty.append(x % 2) #Dodajemy do naszej tablicy resztę z dzielenia przez 2
        x //= 2 #Dzielimy całkowicie x przez 2 np 5 // 2 = 2
    liczba = ''.join(str(znak) for znak in reszty) #Łączymy wszystkie cyfry z tablicy w jeden string
    print(liczba[::-1]) #Odwracamy stringa i go wyświetlamy
x = int(input("Podaj liczbę do zmiany: ")) #Pobieramy dane od użytkownika
zamiana_na_bin(x) #Wywołujemy funkcję

####################################################################################
#Rozwiązanie bez funkcji, tablic, etc.

a = int(input("Podaj liczbę do zmiany: ")) #Pobieramy dane od użytkownika
wynik = 0 #Deklaracja zmiennej
mnoznik = 0 #Deklaracja zmiennej
while a >= 1: #Dopóki a wieksze bądź równe 1
    wynik += a % 2 #Do wyniku dodajemy reszte z dzielenia przez 2
    a //= 2 #Dzielimy całkowicie a przez 2 np 5 // 2 = 2
    skladowa = 10 ** mnoznik #Robimy to żeby moć "przeczytać od dołu" czyli pierwszy element bedzie najmniejszy 1 lub 0, a ostatni(czyli ten na koncu przy dzieleniu) bedzie najwiekszy dzieki czemu wyladuje na poczatku bo jest razy 10 do potegi
    mnoznik += 1 #inkrementujemy mnoznik co przejscie
    if a % 2 == 1: #Sprawdzamy czy reszta jest równa 1, bo inaczej nam by się popsuło i 0 zamienialibysmy na 1
        wynik *= skladowa #Przesuwamy cyfre w lewo, tak jakby czytac od dołu
print(wynik) #Wyświetlamy wynik
