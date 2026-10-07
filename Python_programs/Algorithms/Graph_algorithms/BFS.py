from collections import deque

graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],  # E łączy się z F
    'F': []
}

def bfs(graf, start):
    # Set (zbiór) przechowujący odwiedzone węzły, żeby nie wejść w nieskończoną pętlę
    odwiedzone = set()
    # Inicjujemy kolejkę węzłem startowym
    kolejka = deque([start])
    # Oznaczamy start jako odwiedzony
    odwiedzone.add(start)

    print("Kolejność BFS:")

    while kolejka:  # Dopóki kolejka nie jest pusta
        # Pobieramy pierwszy element z kolejki (First Out)
        wezel = kolejka.popleft()
        print(wezel, end=" ")

        # Sprawdzamy wszystkich sąsiadów aktualnego węzła
        for sasiad in graf[wezel]:
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)  # Zaznaczamy jako odwiedzony, by nie wrzucić go dwa razy
                kolejka.append(sasiad)  # Dodajemy sąsiada na koniec kolejki (In)

# Uruchomienie:
bfs(graf, 'A')
# Wynik zazwyczaj: A B C D E F

print()
def bfs_2(arr, start):
    visited = set()
    kolejka = deque([start])
    visited.add(start)
    while kolejka:
        apex = kolejka.popleft()
        for n in arr[apex]:
            if n not in visited:
                kolejka.append(n)
                visited.add(n)

    print("Odwiedzone: ", visited)
bfs_2(graf, 'A')
