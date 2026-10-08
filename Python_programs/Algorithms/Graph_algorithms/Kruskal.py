graph_edges = [
    (0, 1, 5),
    (0, 2, 8),
    (1, 2, 2),
    (1, 3, 9),
    (2, 3, 4)
]

def adjacency_list(arr):
    tup = {}
    for edge in arr:
        tup.setdefault(edge[0], []).append([edge[1], edge[2]])
        tup.setdefault(edge[1], []).append([edge[0], edge[2]])
    return tup

def edge_sorting(arr):
    return arr.sort(key=lambda x: x[2])

def quicksort_edges(arr):
    # Base case: empty list or list with one element is already sorted
    if len(arr) <= 1:
        return arr

    # Choose pivot (for simplicity we take the middle element)
    pivot = arr[len(arr) // 2]
    pivot_weight = pivot[2]  # We care about the weight at the 3rd position (index 2)

    # Divide the list into three smaller lists relative to the pivot weight
    left = [x for x in arr if x[2] < pivot_weight]
    middle = [x for x in arr if x[2] == pivot_weight]
    right = [x for x in arr if x[2] > pivot_weight]

    # Recursively sort the left and right side, then concatenate (+) into one list
    return quicksort_edges(left) + middle + quicksort_edges(right)

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(x, y, parent):
    parent_x = find(parent, x)
    parent_y = find(parent, y)
    if parent_x != parent_y:
        parent[parent_y] = parent_x
        return True
    return False

def kruskal(arr):
    parent = {}
    for tup in arr:
        parent[tup[0]] = tup[0]
        parent[tup[1]] = tup[1]
    sorted_arr = quicksort_edges(arr)
    mst = []
    for u, v, w in sorted_arr:
        if union(u, v, parent):
            mst.append(tuple([u, v, w]))
    print(mst)
kruskal(graph_edges)
