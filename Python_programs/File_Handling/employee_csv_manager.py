import datetime

def dodawanie(rekord):
    with open("baza_danych.csv", 'a+') as baza:
        rekord = ';'.join(r for r in rekord)
        baza.write('\n' + rekord)
        add_time = datetime.datetime.now()
    baza.close()
    with open("log_file", 'a+') as log_file:
        log_file.write(f"\n{add_time} Dodanie rekordu: {rekord}")
    log_file.close()

def wyswietlenie(baza_rekordow):
    show_time = datetime.datetime.now()
    for rekord in baza_rekordow:
        print(rekord[1], rekord[2])
    with open("log_file", 'a+') as log_file:
        log_file.write(f"\n{show_time} Wyświetlenie bazy")
    log_file.close()

def wyszukiwanie(baza_rekordow, szukana):
    for rekord in baza_rekordow:
        if rekord[0] == str(szukana):
            print(rekord)
            search_time = datetime.datetime.now()
            break
    with open("log_file", 'a+') as log_file:
        log_file.write(f"\n{search_time} Wyszukanie ID nr {szukana}")
    log_file.close()

def start():
    with open("baza_danych.csv", 'r') as baza_raw:
        baza = []
        for rekord_raw in baza_raw.readlines():
            baza.append(rekord_raw.strip().split(';'))
        choice = int(input("Podaj akcje którą chcesz wykonać (1 - dodanie rekordu, 2 - wyświetlenie bazy, 3 - wyszukanie po ID, 4 - wyświetlenie logów, 5 - exit) \n"))
        baza_raw.close()
        
        match choice:
            case 1:
                rekord = input("Podaj rekord (wartości po spacji - ID Imie Nazwisko Stanowisko Pensja)")
                rekord = rekord.strip().split(" ")
                baza_id = [r[0] for r in baza]
                if rekord[0] in baza_id: 
                    print("Błędne ID")
                    start()
                else:
                    dodawanie(rekord)
                    start()
            case 2:
                wyswietlenie(baza)
                start()
            case 3:
                a = input("Podaj ID: ")
                wyszukiwanie(baza, a)
                start()
            case 4:
                show_log = datetime.datetime.now()
                with open("log_file", 'a') as log_file:
                    log_file.write(f"\n{show_log} Wyświetlenie logów")
                log_file.close()

                with open("log_file", 'r') as logs:
                    for log in logs.readlines():
                        print(log.strip())
                logs.close()
                
                start()
            case 5:
                print("Dobrego dnia!")
start()

            