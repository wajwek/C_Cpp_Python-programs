test = [1, 2, 3, 7, 8, 9, 15, 34]
n = len(test)

def Binary_search(tab, wanted, n):
    l = 0
    r = n - 1
    while tab[l] != wanted:
        middle = (l + r) // 2
        if tab[middle] < wanted:
            l = middle + 1
        else:
            r = middle - 1
    return tab[l], l
print(Binary_search(test, 8, n))