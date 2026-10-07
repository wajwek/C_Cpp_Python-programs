def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** (1/2)) + 1, 1):
            if n % i == 0:
                return False
        return True

def next_prime(n):
    if n < 2:
        return 2
    else:
        i = n + 1
        while not is_prime(i):
            i += 1
        return i

print(next_prime(101235897691))
