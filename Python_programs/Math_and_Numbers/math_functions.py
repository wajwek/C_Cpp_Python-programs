from typing import Generator

def square(x: float) -> float:
    """Return the square of a number."""
    return x ** 2

def is_prime(n: int) -> bool:
    """Check if an integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(n: int) -> int:
    """Calculate the recursive sum of digits for a given integer."""
    n_abs = abs(n)
    if n_abs < 10:
        return n_abs
    return (n_abs % 10) + digit_sum(n_abs // 10)

def prime_generator(limit: int) -> Generator[int, None, None]:
    """Yield all prime numbers up to limit."""
    for i in range(limit + 1):
        if is_prime(i):
            yield i

def next_prime(n: int) -> int:
    """Return the smallest prime number strictly greater than n."""
    if n < 2:
        return 2
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def fast_power(base: int, exp: int) -> int:
    """Calculate base ** exp using divide-and-conquer exponentiation."""
    if exp < 0:
        return 0
    elif exp == 0:
        return 1
    if exp % 2 == 0:
        return fast_power(base * base, exp // 2)
    else:
        return base * fast_power(base, exp - 1)

if __name__ == "__main__":
    print("Square of 12:", square(12))
    print("Is 17 prime?", is_prime(17))
    print("Sum of digits for 11111:", digit_sum(11111))
    print("Primes up to 11:", list(prime_generator(11)))
    print("Next prime after 101235897691:", next_prime(101235897691))
    print("Fast power 1012^2:", fast_power(1012, 2))
