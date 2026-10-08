def count_primes_up_to(n: int) -> int:
    """Count prime numbers in the range [2, n]."""
    prime_count = 0
    for num in range(2, n + 1):
        if num == 2:
            prime_count += 1
        else:
            has_divisor = False
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    has_divisor = True
                    break
            if not has_divisor:
                prime_count += 1
    return prime_count

def decimal_to_binary(n: int) -> str:
    """Convert a positive integer to binary string representation."""
    if n == 0:
        return "0"
    remainders = []
    while n >= 1:
        remainders.append(str(n % 2))
        n //= 2
    return "".join(reversed(remainders))

def is_perfect_number(n: int) -> bool:
    """Check if a number equals the sum of its proper positive divisors."""
    if n <= 1:
        return False
    divisor_sum = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            divisor_sum += divisor
        if divisor_sum > n:
            return False
    return divisor_sum == n

if __name__ == "__main__":
    upper_bound = 50
    print(f"Number of primes up to {upper_bound}: {count_primes_up_to(upper_bound)}")
    sample_num = 42
    print(f"{sample_num} in binary: {decimal_to_binary(sample_num)}")
    test_perfect = 28
    print(f"Is {test_perfect} perfect? {is_perfect_number(test_perfect)}")
