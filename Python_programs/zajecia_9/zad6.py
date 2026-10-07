def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** (1/2)) + 1, 1):
            if n % i == 0:
                return False
        return True

def prime_generator(n):
    i = 0
    while i <= n:
        if is_prime(i):
            yield i
        i += 1
x = prime_generator(11)
for i in x:
    print(i)