def rabin_karp_search(text, pattern, b=256, p=101):
    '''
    b - base of the number system, in our case ASCII
    p - prime number used for modulo
    hash_p - calculated hash for our pattern, const
    hash_t - calculated hash for currently compared fragment
    h - coefficient of the first letter in the pattern for hash, b^(m-1) mod p
    '''

    n = len(text)
    m = len(pattern)
    results = []
    hash_p = 0
    hash_t = 0
    h = 1
    for i in range(m - 1):
        h = (h * b) % p
    for i in range(m):
        hash_p = (b * hash_p + ord(pattern[i])) % p
        hash_t = (b * hash_t + ord(text[i])) % p
    for i in range(n - m + 1): # we want to check the last hash which was calculated previously, now we won't calculate a new one because the if won't pass
        if hash_p == hash_t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                results.append(i)
        if i < n - m: # if there is still a new letter to load, calculate the next hash, that's why we check if it's not the last forbidden element when we would go out of bounds
            hash_t = (b * (hash_t - ord(text[i]) * h) + ord(text[i + m])) % p
            if hash_t < 0:
                hash_t = hash_t + p
    return results


text_rk = "W SZCZEBRZESZYNIE CHRZASZCZ BRZMI W TRZCINIE"
pattern_rk = "RZ"

results_rk = rabin_karp_search(text_rk, pattern_rk)

print("-" * 50)
print(f"Searched text: '{text_rk}'")
print(f"Searched pattern: '{pattern_rk}'")
print("-" * 50)

if results_rk:
    print(f"Success! Pattern found at indices: {results_rk}")
    for index in results_rk:
        margin = " " * index
        print(f"Match:                {margin}{pattern_rk}")
else:
    print("Pattern not found in the text.")
