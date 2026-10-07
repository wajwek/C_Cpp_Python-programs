def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab
print(insertion_sort([2,3,2,4,1,5,6,2,1]))