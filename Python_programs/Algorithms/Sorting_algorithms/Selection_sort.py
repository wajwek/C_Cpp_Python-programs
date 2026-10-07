test = [3,12,15,12,34,3, 1, 7]
n = len(test) # n - długość tablicy
def selection_sort(tab, array_len): # Wykona się 1 raz
    for i in range(array_len - 1): # Wykona się n razy
        min_index = i # Wykona się n - 1
        for j in range(i + 1, array_len): # Wykona się n - i razy, bo wiemy, że początek jest posortowany
            if tab[j] < tab[min_index]: # Wykona się n - i - 1 razy
                min_index = j # W zależności od warunku, nie więcej niż n - i - 1
        tab[min_index], tab[i] = tab[i], tab[min_index] # Wykona się n - 1
    return tab # Wykona się 1 raz
print(selection_sort(test, n))

""" Całościowa złożoność asymptotyczna to n^2 (n -> inf), 
bo  warunek w lininjce 7 będzie na początku porównywał n - 1 elementów, potem n - 2 itd.
co da nam ciąg arytmetyczny którego suma to (1/2)n^2 - (1/2)n"""



