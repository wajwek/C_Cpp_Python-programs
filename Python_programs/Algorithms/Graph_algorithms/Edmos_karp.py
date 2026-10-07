class Graph:
    def __init__(self, graph_matrix):
        # Inicjalizujemy graf macierzą sąsiedztwa
        self.graph = graph_matrix
        self.ROW = len(graph_matrix)

    def bfs(self, source, sink, parent):
        # Tablica do śledzenia odwiedzonych węzłów
        visited = [False] * self.ROW

        # Kolejka do BFS
        queue = []
        queue.append(source)
        visited[source] = True

        # Standardowa pętla BFS
        while queue:
            u = queue.pop(0)

            # Przeglądamy wszystkich sąsiadów węzła u
            for v, capacity in enumerate(self.graph[u]):
                # Jeśli sąsiad nieodwiedzony i krawędź ma jeszcze przepustowość
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u  # TUTAJ ZAPISUJEMY ŚLAD!

                    # Jeśli dotarliśmy do ujścia, przerywamy - mamy najkrótszą ścieżkę
                    if v == sink:
                        return True

        # Jeśli kolejka opustoszała, a nie dotarliśmy do ujścia, ścieżek brak
        return False

    def edmonds_karp(self, source, sink):
        # Tablica 'parent' przechowa naszą wyznaczoną ścieżkę
        parent = [-1] * self.ROW
        max_flow = 0

        # Dopóki BFS znajduje jakąkolwiek ścieżkę powiększającą
        while self.bfs(source, sink, parent):

            # 1. ETAP ODTWARZANIA ŚCIEŻKI I SZUKANIA WĄSKIEGO GARDŁA
            path_flow = float("Inf")
            s = sink
            # Cofamy się od ujścia do źródła za pomocą tablicy 'parent'
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            # 2. ETAP AKTUALIZACJI SIECI REZYDUALNEJ
            v = sink
            # Znowu cofamy się od ujścia do źródła, aktualizując krawędzie
            while v != source:
                u = parent[v]
                # Zmniejszamy przepustowość krawędzi, którą poszliśmy (w przód)
                self.graph[u][v] -= path_flow

                # Zwiększamy przepustowość krawędzi powrotnej ("pod prąd")
                self.graph[v][u] += path_flow

                v = u

        return max_flow