test = [3,12,15,12,34,3, 1, 7]
length = len(test)
def bubble_sort(tab, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tab[j + 1] < tab[j]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab
print(bubble_sort(test, length))
# złożoność n^2