def count_vowels(word):
    vowels = ["a", "e", "y", "i", "u", "o"]
    counter = 0
    for char in word:
        if char.lower() in vowels:
            counter += 1
    return counter
print(count_vowels("kajak"))
