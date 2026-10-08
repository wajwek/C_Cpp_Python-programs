def sum_of_squares(n: int) -> int:
    """Calculate the sum of squares of digits of a number."""
    total = 0
    while n > 0:
        total += pow(n % 10, 2)
        n //= 10
    return total

def is_happy(n: int) -> bool:
    """Determine whether a given number is a happy number."""
    seen = set()
    while n != 1:
        seen.add(n)
        n = sum_of_squares(n)
        if n in seen:
            return False
    return True

def analyze_happy_numbers_in_range():
    start = int(input("Enter range start: "))
    end = int(input("Enter range end: "))
    happy_numbers = []
    count = 0
    for i in range(start, end + 1):
        if is_happy(i):
            happy_numbers.append(i)
            count += 1
    print("Happy numbers:", happy_numbers)
    print("Count:", count)
    if happy_numbers:
        print("Maximum:", max(happy_numbers))
    total_in_range = end + 1 - start
    percentage = round((count / total_in_range) * 100, 2) if total_in_range > 0 else 0
    print(f"Percentage: {percentage}%")

if __name__ == "__main__":
    analyze_happy_numbers_in_range()
