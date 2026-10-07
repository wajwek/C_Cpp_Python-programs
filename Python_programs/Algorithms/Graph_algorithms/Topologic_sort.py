
from collections import deque


def sortowanie_topologiczne(graf):
    # 1. Inicjalizujemy słownik stopni wejściowych (dla każdego węzła na start 0)
    stopnie_wejsciowe = {wezel: 0 for wezel in graf}

    # Liczymy faktyczne stopnie wejściowe
    for wezel in graf:
        for sasiad in graf[wezel]:
            stopnie_wejsciowe[sasiad] += 1

    # 2. Szukamy węzłów, które nie mają żadnych wymagań wstępnych (wartość 0)
    kolejka = deque([wezel for wezel in graf if stopnie_wejsciowe[wezel] == 0])

    posortowana_lista = []

    # 3. Zaczynamy przetwarzanie kolejki
    while kolejka:
        # Pobieramy węzeł bez wymagań
        obecny = kolejka.popleft()
        posortowana_lista.append(obecny)

        # "Wykonaliśmy" zadanie, więc jego sąsiedzi mają o jedno wymaganie mniej
        for sasiad in graf[obecny]:
            stopnie_wejsciowe[sasiad] -= 1

            # Jeśli sąsiad stracił wszystkie wymagania, jest gotowy do wykonania!
            if stopnie_wejsciowe[sasiad] == 0:
                kolejka.append(sasiad)

    # 4. Sprawdzenie na koniec: czy udało się posortować wszystkie węzły?
    # Jeśli lista wynikowa jest krótsza niż liczba wszystkich węzłów, to znaczy,
    # że w grafie był cykl i sortowanie topologiczne jest niemożliwe.
    if len(posortowana_lista) == len(graf):
        return posortowana_lista
    else:
        return "Błąd: W grafie wykryto cykl! To nie jest DAG."

print()
# Nasz testowy graf - reprezentacja ubierania się:
# Skarpetki(A), Buty(B), Bielizna(C), Spodnie(D)
# Zależności: Skarpetki -> Buty | Bielizna -> Spodnie -> Buty
graf_ubran = {
    'Skarpetki': ['Buty', 'Spodnie'],
    'Bielizna': ['Spodnie', 'Skarpetki'],
    'Spodnie': ['Buty'],
    'Buty': []  # Koniec procesu dla tej ścieżki
}

wynik = sortowanie_topologiczne(graf_ubran)
print(f"Kolejność ubierania: {wynik}")