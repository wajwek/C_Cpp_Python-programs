import heapq

graph_edges = [
    (0, 1, 5),
    (0, 2, 8),
    (1, 2, 2),
    (1, 3, 9),
    (2, 3, 4)
]


def neighbour_list(arr):
    tmp = {}
    
    # Krok 1: Znajdź wszystkie wierzchołki (początkowe i docelowe)
    wszystkie_wierzcholki = set()
    for tup in arr:
        wszystkie_wierzcholki.add(tup[0])
        wszystkie_wierzcholki.add(tup[1])
    
    # Krok 2: Zainicjuj listę sąsiedztwa dla każdego wierzchołka
    for v in wszystkie_wierzcholki:
        tmp[v] = []
    
    # Krok 3: Dodaj krawędzie
    for tup in arr:
        # Uwaga: Ten kod zakłada, że graf jest SKIEROWANY. 
        # (Jeśli nieskierowany, musisz dodać drugą linijkę dla kierunku powrotnego)
        tmp[tup[0]].append([tup[1], tup[2]])
    
    return tmp


n_list = neighbour_list(graph_edges)

# Wyświetlenie pełnej listy sąsiedztwa
print("Pełna lista sąsiedztwa (zawiera wszystkie wierzchołki):")
for wierzcholek in sorted(n_list.keys()):
    print(f"  {wierzcholek}: {n_list[wierzcholek]}")
print()

def dijkstra(arr, start):
    dist = {}
    for apex in arr:
        dist[apex] = float('inf')
    dist[start] = 0
    parent = {start: None}
    kopiec = [(0, start)]
    while kopiec:
        w, u = heapq.heappop(kopiec)
        if w > dist[u]:
            continue
        for v, d in arr.get(u, []):
            new_d = dist[u] + d
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(kopiec, (dist[v], v))
                parent[v] = u
    paths ={}
    for cur in arr:
        if dist[cur] != float('inf'):
            apex = cur
            paths[cur] = [apex]
            apex = parent[apex]
            while apex is not None:
                paths[cur].append(apex)
                apex = parent[apex]
            paths[cur] = paths[cur][::-1]
    print(paths)

dystanse = dijkstra(n_list, 0)
print(dystanse)

def lista_s(arr):
    lista = {}
    for u, v, w in arr:
        print(u, v, w)
        if u not in lista:
            lista[u] = [tuple([v, w])]
        else:
            lista[u].append(tuple([v, w]))
        if v not in lista:
            lista[v] = []
    return lista

x = lista_s(graph_edges)
print(x)

def dijikstra_v2(arr, start, end):
    dist = {}
    odwiedzone = set()

    for apex in arr:
        dist[apex] = float('inf')
    dist[start] = 0

    while True:
        u = None
        najmniejszy_dystans = float('inf')

        for wezel, dystans in dist.items():
            if wezel not in odwiedzone and dystans < najmniejszy_dystans:
                najmniejszy_dystans = dystans
                u = wezel

        if u is None:
            break

        if u == end:
            return dist[u]

        odwiedzone.add(u)

        for v, waga in arr.get(u, []):
            nowy_dystans = dist[u] + waga
            if nowy_dystans < dist[v]:
                dist[v] = nowy_dystans
    return float('inf')

print(dijikstra_v2(x, 0, 3))

def dijikstra_v3(arr, start):
    dist = {}
    for apex in arr:
        dist[apex] = float('inf')
    dist[start] = 0
    visited = set()
    while True:
        u = None
        minimalna_w = float('inf')
        for v, d in dist.items():
            if v not in visited and d < minimalna_w:
                minimalna_w = d
                u = v
        if u is None:
            break
        visited.add(u)
        for v, w in arr.get(u, []):
            new_d = dist[u] + w
            if new_d < dist[v]:
                dist[v] = new_d
    return dist

print(dijikstra_v3(x, 0))





