def analize_pattern(pattern):
    next_arr = [0] * len(pattern)
    next_arr[0] = -1
    j = 0
    if len(pattern) > 1: next_arr[1] = 0
    for i in range(2, len(pattern)):
        while j > 0 and pattern[i - 1] != pattern[j]:
            j = next_arr[j]
        if pattern[i - 1] == pattern[j]:
            j += 1
        next_arr[i] = j
    return next_arr

def kmp_search(text, pattern):
    next_arr = analize_pattern(pattern)
    text_p = 0
    pattern_p = 0
    while text_p < len(text):
        if text[text_p] == pattern[pattern_p]:
            text_p += 1
            pattern_p += 1
        else:
            pattern_p = next_arr[pattern_p]
            if pattern_p == -1:
                text_p += 1
                pattern_p += 1
        if pattern_p == len(pattern):
            return text_p - pattern_p, text_p
    return None

# Nasze dane testowe
tekst = "ABABDABACDABABCABAB"
wzorzec = "ABABCABAB"

# Wywołanie funkcji KMP
wyniki = kmp_search(tekst, wzorzec)

# Wyświetlenie wyników w czytelny sposób
print("-" * 30)
print(f"Przeszukiwany tekst: '{tekst}'")
print(f"Szukany wzorzec:     '{wzorzec}'")
print("-" * 30)

if wyniki:
    print(f"Sukces! Wzorzec znaleziono na indeksach: {wyniki}")

    # Mały bonus: wypisanie tekstu z zaznaczonym miejscem znalezienia wzorca
    for indeks in wyniki:
        margines = " " * indeks
        print(f"Dopasowanie:          {margines}{wzorzec}")
else:
    print("Nie znaleziono wzorca w tekście.")