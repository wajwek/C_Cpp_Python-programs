test = [3, 12, 15, 12, 34, 3, 1, 7]
n = len(test) # n - array length
def selection_sort(tab, array_len): # Executes 1 time
    for i in range(array_len - 1): # Executes n times
        min_index = i # Executes n - 1
        for j in range(i + 1, array_len): # Executes n - i times, because the beginning is sorted
            if tab[j] < tab[min_index]: # Executes n - i - 1 times
                min_index = j # Depending on the condition, no more than n - i - 1
        tab[min_index], tab[i] = tab[i], tab[min_index] # Executes n - 1
    return tab # Executes 1 time
print(selection_sort(test, n))

""" Overall asymptotic complexity is n^2 (n -> inf), 
because the condition on line 7 will initially compare n - 1 elements, then n - 2, etc.
which gives an arithmetic sequence whose sum is (1/2)n^2 - (1/2)n """
