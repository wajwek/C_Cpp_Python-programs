def bellman_ford(edges, n, start):
    distances = {i: float('inf') for i in range(n)}
    predecessors = {i: None for i in range(n)}
    distances[start] = 0
    for i in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u

    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return False, "Negative weight cycle detected!"

    return True, distances, predecessors

graph_edges = [
    (0, 1, 5),
    (0, 2, 8),
    (1, 2, -10),
    (1, 3, 2),
    (2, 3, 4)
]

success, distances, paths = bellman_ford(graph_edges, 4, 0)

if success:
    print("Shortest distances from vertex 0:", distances, paths)
else:
    print(distances)  # Will print cycle message
