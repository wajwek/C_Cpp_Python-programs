test = [9,2,15,8,34,3, 1, 7]
n = len(test)
def heapify(tab, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and tab[left_child] > tab[largest]:
        largest = left_child
    if right_child < n and tab[right_child] > tab[largest]:
        largest = right_child
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, n, largest)
def heap_sort(tab, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n , i)
    for i in range(n - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)
    return tab
print(heap_sort(test, n))