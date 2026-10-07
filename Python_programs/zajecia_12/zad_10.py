import pickle
import shelve

CONFIG_PLIK = "conf" 
tasks = {}

def wczytaj_konfiguracje():
    domyslna = {
        "data_file": "tasks.pkl",
        "autosave": True
    }

    try:
        with shelve.open(CONFIG_PLIK) as plik:
            if "config" not in plik:
                plik["config"] = domyslna
            config = plik["config"]
            
            if "data_file" not in config:
                config["data_file"] = domyslna["data_file"]
            if "autosave" not in config:
                config["autosave"] = domyslna["autosave"]

            plik["config"] = config
            return config
    except Exception as e:
        print("Błąd ->", e, "Ustawiam domyślną")
        return domyslna

def zapisz_konfiguracje(config):
    try:
        with shelve.open(CONFIG_PLIK) as plik:
            plik["config"] = config
        print("Konfiguracja zapisana.")
    except Exception:
        print("Nie udało się zapisać konfiguracji.")

def wczytaj_stan(plik):
    global tasks
    try:
        with open(plik, 'rb') as f:
            dane = pickle.load(f)
            if isinstance(dane, dict):
                tasks = dane
            else:
                print("Plik stanu ma zły format. Ustawiam pustą listę")
            tasks = {}
    except FileNotFoundError:
        print("Brak pliku z zapisanym stanem.")
        tasks = {}
    except (pickle.UnpicklingError, EOFError):
        print("Plik pickle jest uszkodzony.")
        tasks = {}
    except Exception as e:
        print("Błąd ->", e, "Ustawiam pustą listę")
        tasks = {}

def zapisz_stan(plik):
    try:
        with open(plik, 'wb') as f:
            pickle.dump(tasks, f)
        print("Zapisano.")
    except Exception as e:
        print("Nie udało się zapisać stanu ->", e)

def wyswietl():
    print("\n--- Lista ---")
    for kategoria, lista in tasks.items():
        print(f"Kategoria: {kategoria}")
        for i, zadanie in enumerate(lista):
            opis = zadanie[0]
            status = zadanie[1]
            znaczek = "[x]" if status else "[ ]"
            print(f"  {i}. {znaczek} {opis}")
    print("-------------")

def dodaj(plik):
    kategoria = input("Podaj kategorię: ").strip()
    opis = input("Treść zadania: ").strip()

    if not kategoria:
        print("Kategoria nie może być pusta.")
        return
    if not opis:
        print("Treść zadania nie może być pusta.")
        return

    if kategoria not in tasks:
        tasks[kategoria] = []

    tasks[kategoria].append((opis, False))
    zapisz_stan(plik)

def oznacz_wykonane(plik):
    kategoria = input("Podaj kategorię: ").strip()

    if kategoria in tasks:
        numer = input("Podaj numer zadania (od 0): ").strip()
        try:
            numer = int(numer)
        except ValueError:
            print("Złe wejście: numer musi być liczbą.")
            return

        lista_zadan = tasks[kategoria]
        if 0 <= numer < len(lista_zadan):
            stary_opis = lista_zadan[numer][0]
            lista_zadan[numer] = (stary_opis, True)
            zapisz_stan(plik)
        else:
            print("Zły numer zadania.")
    else:
        print("Nie ma takiej kategorii.")

def ustawienia(config):
    while True:
        print("\n--- Ustawienia ---")
        print(f"1 - Zmień plik danych (teraz: {config['data_file']})")
        print(f"2 - Przełącz autosave (teraz: {config['autosave']})")
        print("3 - Powrót")
        wybor = input("Wpisz opcje -> ").strip()

        if wybor == "1":
            nowy = input("Podaj nową nazwę pliku: ").strip()
            if not nowy:
                print("Nazwa nie może być pusta.")
            else:
                config["data_file"] = nowy
                zapisz_konfiguracje(config)
                print("Uruchom ponownie")
        elif wybor == "2":
            config["autosave"] = not config["autosave"]
            zapisz_konfiguracje(config)
        elif wybor == "3":
            break
        else:
            print("Nieznana opcja.")

config = wczytaj_konfiguracje()
PLIK = config["data_file"]

wczytaj_stan(PLIK)

while True:
    print("\n 1 - Wyświetl, 2 - Dodaj, 3 - Wykonane, 4 - Ustawienia, 5 - Exit")
    wybor = input("Wpisz opcje -> ").strip()

    if wybor == '1':
        wyswietl()
    elif wybor == '2':
        dodaj(PLIK)
    elif wybor == '3':
        oznacz_wykonane(PLIK)
    elif wybor == '4':
        ustawienia(config)
        PLIK = config["data_file"]
    elif wybor == '5':
        if config.get("autosave", True):
            zapisz_stan(PLIK)
        print("Dobrego dnia!")
        break
    else:
        print("Nieznana opcja.")

