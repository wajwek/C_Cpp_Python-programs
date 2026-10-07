def dodawanie(rekord):
    with open("baza_danych.csv", 'a') as baza:
        rekord = ';'.join(r for r in rekord)
        baza.write('\n' + rekord)
    baza.close()
    
def wyswietlenie(baza_rekordow):
    for rekord in baza_rekordow:
        print(rekord[1], rekord[2])

def wyszukiwanie(baza_rekordow, szukana):
    for rekord in baza_rekordow:
        if rekord[0] == str(szukana):
            print(rekord)
            return
    print("Brak rekordu o takim ID")

def start():
    with open("baza_danych.csv", 'r') as baza_raw:
        baza = []
        for rekord_raw in baza_raw.readlines():
            baza.append(rekord_raw.strip().split(';'))
        choice = int(input("Podaj akcje którą chcesz wykonać (1 - dodanie rekordu, 2 - wyświetlenie bazy, 3 - wyszukanie po ID, 4 - exit) \n"))
        baza_raw.close()
        match choice:
            case 1:
                rekord = input("Podaj rekord (wartości po spacji - ID Imie Nazwisko Stanowisko Pensja)")
                rekord = rekord.strip().split(" ")
                if len(rekord) != 5:
                    print("Złe wejście")
                else:
                    try:
                        int(rekord[0])
                        int(rekord[4])
                        if (rekord[1].isalpha() and rekord[2].isalpha() and rekord[3].isalpha()):
                            baza_id = [r[0] for r in baza]
                            if rekord[0] in baza_id: 
                                print("Błędne ID")
                            else:
                                dodawanie(rekord)
                        else:
                            print("Błędny format")
                    except Exception as e:
                        print("Błąd", e)
                start()
            case 2:
                wyswietlenie(baza)
                start()
            case 3:
                a = input("Podaj ID: ")
                try:
                    int(a)
                    wyszukiwanie(baza, a)
                    start()
                except Exception as e:
                    print("Błąd", e)
                    start()
            case 4:
                print("Dobrego dnia!")
start()

            