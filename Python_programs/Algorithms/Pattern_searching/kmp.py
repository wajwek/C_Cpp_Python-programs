def analyze_pattern(pattern):
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
    next_arr = analyze_pattern(pattern)
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

# Test data
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

# KMP function call
results = kmp_search(text, pattern)

# Display results
print("-" * 30)
print(f"Search text:     '{text}'")
print(f"Searched pattern: '{pattern}'")
print("-" * 30)

if results:
    print(f"Success! Pattern found at indices: {results}")

    for index in results:
        margin = " " * index
        print(f"Match:            {margin}{pattern}")
else:
    print("Pattern not found in the text.")
