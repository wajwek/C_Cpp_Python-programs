from collections import deque


def topological_sort(graph):
    # 1. Initialize in-degree dictionary (0 for each node initially)
    in_degree = {node: 0 for node in graph}

    # Count actual in-degrees
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # 2. Find nodes with no prerequisites (value 0)
    queue = deque([node for node in graph if in_degree[node] == 0])

    sorted_list = []

    # 3. Start processing the queue
    while queue:
        # Get node without prerequisites
        current = queue.popleft()
        sorted_list.append(current)

        # "Completed" the task, so its neighbors have one less prerequisite
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1

            # If neighbor lost all prerequisites, it's ready to execute!
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 4. Final check: did we manage to sort all nodes?
    # If the result list is shorter than the total number of nodes, it means
    # there was a cycle in the graph and topological sort is impossible.
    if len(sorted_list) == len(graph):
        return sorted_list
    else:
        return "Error: Cycle detected in the graph! This is not a DAG."

print()
# Our test graph - dressing representation:
# Socks(A), Shoes(B), Underwear(C), Pants(D)
# Dependencies: Socks -> Shoes | Underwear -> Pants -> Shoes
clothing_graph = {
    'Socks': ['Shoes', 'Pants'],
    'Underwear': ['Pants', 'Socks'],
    'Pants': ['Shoes'],
    'Shoes': []  # End of process for this path
}

result = topological_sort(clothing_graph)
print(f"Dressing order: {result}")
