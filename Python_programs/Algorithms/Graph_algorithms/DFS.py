from operator import truediv

krawedzie = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'E'),
    ('C', 'F'),
    ('D', 'G'),
    ('E', 'G'),
    ('F', 'H'),
    ('G', 'H')
]

def macierz_sasiedztwa(arr):
    # 1. Zbieramy unikalne wierzchołki
    apex = set()
    for u, v in arr:
        apex.add(u)
        apex.add(v)

    # 2. Tworzymy POSORTOWANĄ listę wierzchołków.
    # Dzięki temu mamy pewność, że A=0, B=1, C=2 itd.
    posortowane_wierzcholki = sorted(apex) # Tworzy tablicę

    # 3. Tworzymy mapę (węzeł -> indeks) za pomocą enumerate
    mapa = {wezel: indeks for indeks, wezel in enumerate(posortowane_wierzcholki)}

    # 4. Inicjalizujemy pustą macierz N x N wypełnioną zerami
    n = len(posortowane_wierzcholki)
    matrix = [[0] * n for _ in range(n)]

    # 5. Zaznaczamy krawędzie w macierzy (uwzględnia skierowanie u -> v)
    for u, v in arr:
        indeks_u = mapa[u]
        indeks_v = mapa[v]
        matrix[indeks_u][indeks_v] = 1  # Wstawiamy 1 tylko dla istniejących połączeń

    return mapa, matrix


# Uruchomienie i ładne wypisanie wyników
mapa_wierzcholkow, test_macierz = macierz_sasiedztwa(krawedzie)

print("--- Przypisanie indeksów ---")
for w, idx in mapa_wierzcholkow.items():
    print(f"Węzeł {w} ->  {idx}")

print("\n--- Macierz sąsiedztwa ---")
for wiersz in test_macierz:
    print(wiersz)

def lista_sasiedztwa(arr):
    apex = {}
    for u, v in arr:
        if u not in apex:
            apex[u] = [v]
        else:
            apex[u].append(v)
        if v not in apex:
            apex[v] = [] # Dodanie wierzchołków bez wychodzących krawędzi
    tab = dict(sorted(apex.items()))
    return tab
print()

lista_s = lista_sasiedztwa(krawedzie)
print(lista_s)

print("=================== DFS =====================")

def dfs(arr, start, visited=None, path=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbour in arr[start]:
        if neighbour not in visited:
            dfs(arr, neighbour, visited)
    return visited

def czy_ma_cykl(arr, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = set()  # Pamięta tylko aktualnie rozpatrywaną ścieżkę

    # Dodajemy węzeł do odwiedzonych oraz do aktualnej ścieżki
    visited.add(start)
    path.add(start)

    # Przeszukujemy sąsiadów
    for neighbour in arr.get(start, []):
        # 1. ZNALEZIONO CYKL!
        # Jeśli sąsiad jest już w naszej aktualnej ścieżce, zrobiliśmy kółko.
        if neighbour in path:
            return True

        # 2. Idziemy dalej w głąb
        if neighbour not in visited:
            # Jeśli wywołanie rekurencyjne znalazło cykl niżej, przekazujemy to wyżej
            if czy_ma_cykl(arr, neighbour, visited, path):
                return True

    # 3. BACKTRACKING (Nawrót)
    # Kończymy badać ten węzeł, więc usuwamy go z aktualnej ścieżki,
    # ale ZOSTAWIAMY w 'visited', by nie wchodzić tu ponownie z innych gałęzi.
    path.remove(start)

    return False

def sprawdz_cykle_w_grafie(arr):
    visited = set()

    # Sprawdzamy każdy węzeł w grafie (na wypadek grafów niespójnych)
    for wezel in arr:
        if wezel not in visited:
            # Jeśli funkcja wykryje, przerywamy
            if czy_ma_cykl(arr, wezel, visited):
                return True

    return False


def czy_spojny(arr):
    for apex in arr:
        # Twój dfs zwraca zbiór, więc od razu przypisujemy go do zmiennej
        odwiedzone = dfs(arr, apex)

        # Sprawdzamy, czy ten zbiór pokrywa cały graf
        if len(odwiedzone) == len(arr):
            return True

    return False

print(czy_spojny(lista_s))


