def shift_tab(alphabet, pattern):
    shift = {}
    dist = {}
    for i in range(len(pattern)):
        dist[pattern[i]] = len(pattern) - 1 - i
    for i in range(len(alphabet)):
        if alphabet[i] not in dist:
            shift[alphabet[i]] = len(pattern)
        else:
            shift[alphabet[i]] = dist[alphabet[i]]
    return shift

def boyer_moore_search(text, pattern, alphabet):
    shift = shift_tab(alphabet, pattern)
    text_p = len(pattern) - 1
    pattern_p = len(pattern) - 1
    while text_p < len(text):
        if text[text_p] == pattern[pattern_p]:
            pattern_p -= 1
            text_p -= 1
        else:
            dist_backwards = len(pattern) - pattern_p - 1

            text_p += max(dist_backwards + 1, shift[text[text_p]])
            
            pattern_p = len(pattern) - 1
        if pattern_p == -1:
            return text_p + 1, text_p + len(pattern)
    return None

alphabet_presentation = "ABCDEFGH"
text_bm = "ABGHHAABGBDE"
pattern_bm = "ABGBD"

results_bm = boyer_moore_search(text_bm, pattern_bm, alphabet_presentation)

print("-" * 30)
print(f"Search text:     '{text_bm}'")
print(f"Searched pattern: '{pattern_bm}'")
print("-" * 30)

if results_bm:
    print(f"Success! Pattern found at indices: {results_bm}")
    margin = " " * results_bm[0]
    print(f"Match:            {margin}{pattern_bm}")
else:
    print("Pattern not found in the text.")
