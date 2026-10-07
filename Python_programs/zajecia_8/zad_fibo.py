licznik = 0

def fibo(n):
    global licznik
    licznik += 1
    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def fibo_iteracyjnie(n):
    tab = [1, 1]
    if n <= 1:
        return tab[n]
    else:
        for i in range(n - 2):
            tab.append(sum(tab[i:i+2]))
        return tab[n - 1]

def fibo_iteracyjnie_v2(n):
    if n <= 2:
        return 1
    else:
        a = 1
        b = 1
        c = 0
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c

print(fibo_iteracyjnie_v2(10)) 

x = fibo(10)
print(x, "liczba wywołań:", licznik)

print(fibo_iteracyjnie(10))
