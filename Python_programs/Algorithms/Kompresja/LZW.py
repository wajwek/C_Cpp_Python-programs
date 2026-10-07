def lzw_encode(tekst):
    # Tworzymy słownik, gdzie '#' to 0, 'A' to 1, 'B' to 2 ... 'Z' to 26
    slownik = {'#': 0}
    for i in range(26):
        litera = chr(ord('A') + i)
        slownik[litera] = i + 1

    # Nowe frazy, których algorytm się nauczy, będą dostawać indeksy od 27 w górę
    nastepny_kod = 27

    # W - nasz aktualnie budowany, znany ciąg
    W = tekst[0]

    wynik = []

    # Przechodzimy przez tekst, zaczynając od drugiego znaku (K)
    for K in tekst[1:]:
        WK = W + K  # Sklejamy to, co znamy (W) z nową literą (K)

        # Jeśli ten zlepek jest już w słowniku, powiększamy W i idziemy dalej
        if WK in slownik:
            W = WK
        # Jeśli nie ma go w słowniku:
        else:
            # 1. Wypisujemy na wyjście kod dla znanego nam W
            wynik.append(slownik[W])

            # 2. Dodajemy nowy zlepek WK do słownika (uczymy się go!)
            slownik[WK] = nastepny_kod
            nastepny_kod += 1

            # 3. Zaczynamy budować nowy ciąg, W staje się literą K
            W = K

    # Na samym końcu musimy "wypchnąć" z pamięci ostatni ciąg W
    if W:
        wynik.append(slownik[W])

    return wynik, slownik


# === DANE TESTOWE (Slajd 18) ===
tekst_do_kompresji = "TOBEORNOTTOBEORTOBEORNOT#"

# Odpalamy kompresję
skompresowane_dane, wygenerowany_slownik = lzw_encode(tekst_do_kompresji)

print(f"Oryginalny tekst: {tekst_do_kompresji}")
print(f"Ilość znaków: {len(tekst_do_kompresji)}")
print("-" * 40)
print(f"Skompresowane kody (liczby):")
print(skompresowane_dane)
print("-" * 40)
print("Nowe frazy dodane do słownika podczas czytania:")
# Wypisujemy tylko nowe kody (od 27 wzwyż)
for fraza, kod in wygenerowany_slownik.items():
    if kod >= 27:
        print(f"Kod {kod}: '{fraza}'")