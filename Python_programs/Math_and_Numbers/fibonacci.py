call_counter = 0

def fibonacci_recursive(n: int) -> int:
    """Calculate n-th Fibonacci number recursively."""
    global call_counter
    call_counter += 1
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n: int) -> int:
    """Calculate n-th Fibonacci number using a list accumulator."""
    table = [1, 1]
    if n <= 1:
        return table[n]
    for i in range(n - 2):
        table.append(sum(table[i:i + 2]))
    return table[n - 1]

def fibonacci_iterative_constant_space(n: int) -> int:
    """Calculate n-th Fibonacci number using constant auxiliary space."""
    if n <= 2:
        return 1
    a, b, c = 1, 1, 0
    for _ in range(2, n):
        c = a + b
        a = b
        b = c
    return c

if __name__ == "__main__":
    n = 10
    print(f"fibonacci_iterative_constant_space({n}) = {fibonacci_iterative_constant_space(n)}")
    result_rec = fibonacci_recursive(n)
    print(f"fibonacci_recursive({n}) = {result_rec}, function calls: {call_counter}")
    print(f"fibonacci_iterative({n}) = {fibonacci_iterative(n)}")
