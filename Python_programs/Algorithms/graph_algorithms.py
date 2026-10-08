connections = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("D", "F", 6),
    ("E", "F", 3)
]
print("####################### ZAD A ############################")

def zad_A(tablica):
    słownik_graf = {}
    for zestaw in tablica:
        słownik_graf[zestaw[0]] = słownik_graf.get(zestaw[0], tuple([])) + tuple([tuple([zestaw[1], zestaw[2]])])
        słownik_graf[zestaw[1]] = słownik_graf.get(zestaw[1], tuple([])) + tuple([tuple([zestaw[0], zestaw[2]])])
    return słownik_graf

graf = zad_A(connections)
print("Słownik grafu:")
for zestaw in graf:
    print(zestaw, graf[zestaw])

print("####################### ZAD B ############################")

def zad_B(tablica):
    wierzcholki = set()
    zbiór_krawędzi = set()
    for zestaw in tablica:
        wierzcholki.add(zestaw[0])
        wierzcholki.add(zestaw[1])
        zbiór_krawędzi.add(tuple([min(zestaw[0], zestaw[1]), max(zestaw[0], zestaw[1])]))
    return wierzcholki, zbiór_krawędzi

wierzcholki, zbiór_krawędzi = zad_B(connections)
print("Zbiór wierzchołków:", wierzcholki)
zbiór_krawędzi = sorted(zbiór_krawędzi)
print("Zbiór krawędzi:")
for zestaw in zbiór_krawędzi:
    print(zestaw)

print("####################### ZAD C ############################")

def zad_C(slownik, start, koniec):

    koszt_dojscia = {}
    poprzedni_węzeł = {}

    for węzeł in slownik:
        koszt_dojscia[węzeł] = float('inf')
        poprzedni_węzeł[węzeł] = None

    koszt_dojscia[start] = 0

    do_sprawdzenia = set()
    do_sprawdzenia.add(start)

    odwiedzone = set()

    while do_sprawdzenia:
        aktualny = min(do_sprawdzenia, key=koszt_dojscia.get)
        do_sprawdzenia.remove(aktualny)
        odwiedzone.add(aktualny)

        if aktualny == koniec:
            break

        for sasiad, waga in slownik[aktualny]:
            if sasiad in odwiedzone:
                continue

            nowy_koszt = koszt_dojscia[aktualny] + waga

            if nowy_koszt < koszt_dojscia[sasiad]:
                koszt_dojscia[sasiad] = nowy_koszt
                poprzedni_węzeł[sasiad] = aktualny
                do_sprawdzenia.add(sasiad)

    if koszt_dojscia[koniec] == float('inf'):
        print("Brak scieżki")
        return "0", 0

    sciezka = []
    węzeł = koniec
    while węzeł is not None:
        sciezka.append(węzeł)
        węzeł = poprzedni_węzeł[węzeł]
    sciezka.reverse()

    return sciezka, koszt_dojscia[koniec]

print("Optymalna scieżka od A do E")
sciezka, koszt = zad_C(graf, "A", "E")
print(" -> ".join(element for element in sciezka))
print("Koszt:", koszt)

print("####################### ZAD D ############################")

def zad_D(graf):

    odwiedzone = set()
    skladowe = []

    for start in graf:

        if start in odwiedzone:
            continue

        składowa = set()
        do_sprawdzenia = set()
        do_sprawdzenia.add(start)

        while do_sprawdzenia:
            aktualny = do_sprawdzenia.pop()

            if aktualny in odwiedzone:
                continue

            odwiedzone.add(aktualny)
            składowa.add(aktualny) # jeśli pojawi się jakiś unikalny wierzchołek, to zostanie dodany w późniejszym appendzie i wyjdzie niespójny

            for sasiad, waga in graf[aktualny]:
                if sasiad not in odwiedzone:
                    do_sprawdzenia.add(sasiad)

        skladowe.append(składowa)

    if len(skladowe) == 1: # ilość grafów, czyli czy jest jeden - spójny 
        return True, skladowe[0]
    else:
        return False, skladowe
    
spojnosc = zad_D(graf)
print("Czy graf spójny:", spojnosc)

print("####################### ZAD E ############################")

def zad_E(slownik, wierzchołek):

    mapa_kosztow = {}
    for w in slownik:
        mapa_kosztow[w] = float('inf')
    mapa_kosztow[wierzchołek] = 0

    do_odwiedzenia = set()
    do_odwiedzenia.add(wierzchołek)

    odwiedzone = set()

    while do_odwiedzenia:
        obecne = min(do_odwiedzenia, key=mapa_kosztow.get)
        do_odwiedzenia.remove(obecne)

        obecny_koszt = mapa_kosztow[obecne]
        odwiedzone.add(obecne)

        for węzeł, koszt in slownik[obecne]:
            nowy_koszt = obecny_koszt + koszt
            if węzeł not in odwiedzone and nowy_koszt < mapa_kosztow[węzeł]:
                mapa_kosztow[węzeł] = nowy_koszt
                do_odwiedzenia.add(węzeł)

    return sum(mapa_kosztow.values())

tab = []
minimum = float('inf')
for wierzchołek in wierzcholki:
    koszt_łączny = zad_E(graf, wierzchołek)
    tab.append([wierzchołek, koszt_łączny])
    if  koszt_łączny < minimum:
        minimum = koszt_łączny
for element in tab:
    if element[1] == minimum:
        print(element, "<- węzeł centralny")
    else:
        print(element)
    