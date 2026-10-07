def bellman_ford(krawedzie, n, start):
    d = {i: float('inf') for i in range(n)}
    poprzednik = {i: None for i in range(n)}
    d[start] = 0
    for i in range(n - 1):
        for u, v, w in krawedzie:
            if d[u] != float('inf') and d[u] + w < d[v]:
                d[v] = d[u] + w
                poprzednik[v] = u

    for u, v, w in krawedzie:
        if d[u] != float('inf') and d[u] + w < d[v]:
            return False, "Wykryto cykl o ujemnej wadze!"

    return True, d, poprzednik

graph_edges = [
    (0, 1, 5),
    (0, 2, 8),
    (1, 2, -10),
    (1, 3, 2),
    (2, 3, 4)
]

sukces, dystanse, trasy = bellman_ford(graph_edges, 4, 0)

if sukces:
    print("Najkrótsze dystanse od wierzchołka 0:", dystanse, trasy)
else:
    print(dystanse)  # Wypisze komunikat o cyklu