def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** (1/2)) + 1, 1):
            if n % i == 0:
                return False
        return True
x = int(input("Podaj liczbę: "))
if is_prime(x):
    print("Ta liczba jest pierwsza")
else:
    print("Ta liczba NIE jest pierwsza")