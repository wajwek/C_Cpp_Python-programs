graph_edges = [
    (0, 1, 5),
    (0, 2, 8),
    (1, 2, 2),
    (1, 3, 9),
    (2, 3, 4)
]

def n_list(arr):
    tup = {}
    for edge in arr:
        tup.setdefault(edge[0], []).append([edge[1], edge[2]])
        tup.setdefault(edge[1], []).append([edge[0], edge[2]])
    return tup

def edge_sorting(arr):
    return arr.sort(key=lambda x: x[2])

def quicksort_edges(arr):
    # Warunek kończący: pusta lista lub z jednym elementem jest już posortowana
    if len(arr) <= 1:
        return arr

    # Wybieramy pivot (dla uproszczenia bierzemy środkowy element)
    pivot = arr[len(arr) // 2]
    pivot_waga = pivot[2]  # Interesuje nas waga na 3. miejscu (indeks 2)

    # Dzielimy listę na trzy mniejsze względem wagi pivota
    left = [x for x in arr if x[2] < pivot_waga]
    middle = [x for x in arr if x[2] == pivot_waga]
    right = [x for x in arr if x[2] > pivot_waga]

    # Rekurencyjnie sortujemy lewą i prawą stronę, a potem sklejamy (+) w jedną listę
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


