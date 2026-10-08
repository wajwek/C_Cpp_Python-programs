import random

def task1_sum():
    """Task 1: Prompt for two integers and display their sum."""
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Sum:", a + b)

def task2_parity():
    """Task 2: Check if an integer is odd or even."""
    a = int(input("Enter a: "))
    if a % 2 != 0:
        print("odd")
    else:
        print("even")

def task3_comparison():
    """Task 3: Compare two numbers."""
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    else:
        print("a = b")

def task4_range_print():
    """Task 4: Print range from 0 to a-1."""
    a = int(input("Enter a: "))
    for n in range(a):
        print(n)

def task5_even_numbers():
    """Task 5: Print even numbers up to 100."""
    for i in range(100):
        if i % 2 == 0:
            print(i)

def task6_arithmetic_sum():
    """Task 6: Calculate arithmetic sum from 1 to a."""
    a = int(input("Enter a: "))
    total = (1 + a) * a / 2
    print("Sum:", total)

def task7_character_count():
    """Task 7: Count occurrences of a character in a word."""
    word = input("Enter word: ")
    char = input("Enter character to count: ")
    print(word.count(char))

def task8_max_of_three():
    """Task 8: Find the maximum of three numbers."""
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    print("Maximum:", max(a, b, c))

def task9_guess_number():
    """Task 9: Random number guessing game."""
    secret = random.randint(1, 20)
    guess = int(input("Guess the number (1-20): "))
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")

def task10_tree(height):
    """Task 10: Print an ASCII Christmas tree."""
    if height > 0:
        star_count = 1
        for i in range(height):
            print(" " * (height - i) + "*" * star_count)
            star_count += 2
        print(" " * height + "*")

def iterative_addition_loop():
    """Cumulative self addition loop demonstration."""
    a = int(input("Enter base number: "))
    b = a
    for _ in range(a):
        print(a + b)
        a += b

if __name__ == "__main__":
    task10_tree(5)
