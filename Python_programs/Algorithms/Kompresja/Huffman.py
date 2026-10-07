import heapq
# --- STRUKTURA DANYCH ---
class Wezel:
    def __init__(self, znak, czestotliwosc):
        self.znak = znak  # Przechowuje literę (lub None dla połączonych węzłów)
        self.czestotliwosc = czestotliwosc  # Ile razy znak występuje (waga węzła)
        self.lewy = None  # Wskaźnik na lewe dziecko (0)
        self.prawy = None  # Wskaźnik na prawe dziecko (1)
    # Aby algorytm heapq (kolejka priorytetowa) wiedział, jak sortować nasze węzły,
    # musimy zdefiniować operator "mniejsze niż" (<). Sortujemy po częstotliwości!
    def __lt__(self, inny):
        return self.czestotliwosc < inny.czestotliwosc

# --- GŁÓWNA FUNKCJA BUDUJĄCA DRZEWO ---
def zbuduj_drzewo_huffmana(czestotliwosci):
    kolejka = []
    # KROK 1: Uporządkowanie znaków.
    # Tworzymy węzły dla każdego znaku i wrzucamy je do kolejki.
    for znak, freq in czestotliwosci.items():
        heapq.heappush(kolejka, Wezel(znak, freq))

    # FAZA REDUKCJI (łączenie dwóch najmniej prawdopodobnych znaków)
    # Powtarzamy krok tak długo, aż w kolejce zostanie tylko 1 element (korzeń drzewa)
    while len(kolejka) > 1:
        # Pobieramy (i usuwamy z kolejki) dwa elementy o NAJMNIEJSZEJ częstotliwości
        lewy_wezel = heapq.heappop(kolejka)
        prawy_wezel = heapq.heappop(kolejka)

        # Tworzymy nowy, połączony węzeł-rodzica. Nie ma on własnego znaku (None).
        # Jego częstotliwość to po prostu suma częstotliwości dzieci.
        suma_freq = lewy_wezel.czestotliwosc + prawy_wezel.czestotliwosc
        rodzic = Wezel(None, suma_freq)

        # Podpinamy wyciągnięte węzły jako dzieci nowego rodzica
        rodzic.lewy = lewy_wezel
        rodzic.prawy = prawy_wezel

        # Wrzucamy nowo powstałego rodzica z powrotem do kolejki priorytetowej
        heapq.heappush(kolejka, rodzic)
        
    # Na koniec pętli w kolejce zostaje tylko jeden element - cały połączony korzeń
    return kolejka[0]

# --- FUNKCJA REKURENCYJNA NADARZAJĄCA KODY (0 i 1) ---
# FAZA KONSTRUKCJI KODU

def wygeneruj_kody_huffmana(wezel, aktualny_kod, slownik_kodow):
    if wezel is None:
        return

    # Jeśli węzeł ma znak (czyli jest "liściem", a nie węzłem pomocniczym),
    # zapisujemy wygenerowany do tej pory ciąg zer i jedynek.
    if wezel.znak is not None:
        slownik_kodow[wezel.znak] = aktualny_kod
        return

    # KROKI 4, 5 i 6: Przypisywanie zer i jedynek.
    # Schodząc w dół w lewą stronę, do kodu doklejamy '0'
    wygeneruj_kody_huffmana(wezel.lewy, aktualny_kod + "0", slownik_kodow)

    # Schodząc w dół w prawą stronę, do kodu doklejamy '1'
    wygeneruj_kody_huffmana(wezel.prawy, aktualny_kod + "1", slownik_kodow)


# === DANE TESTOWE Z PREZENTACJI (Slajd 9 i 10) ===
if __name__ == "__main__":
    # Dane wejściowe z prezentacji: 6 znaków i ich częstotliwości
    czestotliwosci_z_wykladu = {
        'x1': 20,
        'x2': 17,
        'x3': 10,
        'x4': 9,
        'x5': 3,
        'x6': 1
    }
    # Budujemy drzewo
    korzen_drzewa = zbuduj_drzewo_huffmana(czestotliwosci_z_wykladu)
    # Generujemy z niego kody słownikowe
    kody_wynikowe = {}
    wygeneruj_kody_huffmana(korzen_drzewa, "", kody_wynikowe)
    print("--- OTRZYMANE KODY HUFFMANA ---")
    for znak, kod in sorted(kody_wynikowe.items(), key=lambda x: len(x[1])):
        ilosc = czestotliwosci_z_wykladu[znak]
        print(f"Znak {znak} (ilość: {ilosc:2d}) -> Kod: {kod}")