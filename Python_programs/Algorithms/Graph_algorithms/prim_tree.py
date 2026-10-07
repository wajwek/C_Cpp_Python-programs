def prim(graph, start_node):
    visited = []
    mst = []

    # Zaczynamy od wierzchołka startowego
    visited.append(start_node)

    # Dopóki nie odwiedzimy wszystkich wierzchołków
    while len(visited) < len(graph):
        smallest_cost = None
        smallest_from = None
        smallest_to = None

        # Szukamy najtańszej krawędzi wychodzącej z visited
        for node in visited:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    cost = graph[node][neighbor]

                    if smallest_cost is None or cost < smallest_cost:
                        smallest_cost = cost
                        smallest_from = node
                        smallest_to = neighbor

        # Jeśli nie znaleźliśmy żadnej nowej krawędzi,
        # to graf może być niespójny
        if smallest_to is None:
            break

        # Dodajemy nowy wierzchołek i krawędź do MST
        visited.append(smallest_to)
        mst.append((smallest_from, smallest_to, smallest_cost))

    return mst


# Przykładowy graf
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

result = prim(graph, 'A')
print("Minimalne Drzewo Rozpinające:", result)
