import shelve
PLIK = 'baza_uzytkownikow'

def dodaj_uzytkownika(klucz, dane):
    with shelve.open(PLIK) as slownik:
        slownik[klucz] = dane

def pobierz_uzytkownika(klucz):
    with shelve.open(PLIK) as slownik:
        dane = slownik.get(klucz)
        
        if dane:
            print(f"{klucz}: {dane}")
        else:
            print(f"Nie znaleziono klucza: {klucz}")
        return dane

def usun_uzytkownika(klucz):
    with shelve.open(PLIK) as slownik:
        if klucz in slownik:
            print(f"Usunięto -> {slownik.get(klucz)}")
            del slownik[klucz]
        else:
            print(f"Nie można usunąć. Klucz {klucz} nie istnieje.")

def wyswietl_wszystkich():
    with shelve.open(PLIK) as slownik:
        if len(slownik) == 0:
            print("Baza pusta")
        else:
            for klucz, wartosc in slownik.items():
                print(f"ID: {klucz} Dane: {wartosc}")
                
print("dodaj_uzytkownika 1 (Maciej, Wrzesiński, 18)")
dodaj_uzytkownika("1", ("Maciej", "Wrzesiński", 18))
print("wyswietl_wszystkich")
wyswietl_wszystkich()
print("pobierz_uzytkownika 1")
pobierz_uzytkownika("1")
print("usun_uzytkownika 1")
usun_uzytkownika("1")
print("wyswietl_wszystkich")
wyswietl_wszystkich()