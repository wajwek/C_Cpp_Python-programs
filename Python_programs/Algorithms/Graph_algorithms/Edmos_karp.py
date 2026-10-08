class Graph:
    def __init__(self, graph_matrix):
        # Initialize graph with adjacency matrix
        self.graph = graph_matrix
        self.ROW = len(graph_matrix)

    def bfs(self, source, sink, parent):
        # Array to track visited nodes
        visited = [False] * self.ROW

        # Queue for BFS
        queue = []
        queue.append(source)
        visited[source] = True

        # Standard BFS loop
        while queue:
            u = queue.pop(0)

            # Check all neighbors of node u
            for v, capacity in enumerate(self.graph[u]):
                # If neighbor is unvisited and edge still has capacity
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u  # SAVE THE TRAIL HERE!

                    # If we reached the sink, break - we found the shortest path
                    if v == sink:
                        return True

        # If queue is empty and we haven't reached the sink, no path exists
        return False

    def edmonds_karp(self, source, sink):
        # The 'parent' array will store our determined path
        parent = [-1] * self.ROW
        max_flow = 0

        # While BFS finds any augmenting path
        while self.bfs(source, sink, parent):

            # 1. PATH RECONSTRUCTION AND BOTTLENECK SEARCH STAGE
            path_flow = float("Inf")
            s = sink
            # Trace back from sink to source using the 'parent' array
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            # 2. RESIDUAL NETWORK UPDATE STAGE
            v = sink
            # Trace back again from sink to source, updating edges
            while v != source:
                u = parent[v]
                # Decrease capacity of the forward edge we traversed
                self.graph[u][v] -= path_flow

                # Increase capacity of the backward edge ("against the current")
                self.graph[v][u] += path_flow

                v = u

        return max_flow
