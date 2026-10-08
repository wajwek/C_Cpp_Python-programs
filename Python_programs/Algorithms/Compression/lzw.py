def lzw_encode(text):
    # Create dictionary where '#' is 0, 'A' is 1, 'B' is 2 ... 'Z' is 26
    dictionary = {'#': 0}
    for i in range(26):
        letter = chr(ord('A') + i)
        dictionary[letter] = i + 1

    # New phrases that the algorithm learns will get indices from 27 upwards
    next_code = 27

    # W - our currently built, known sequence
    W = text[0]

    result = []

    # Go through the text, starting from the second character (K)
    for K in text[1:]:
        WK = W + K  # Concatenate what we know (W) with the new letter (K)

        # If this chunk is already in the dictionary, expand W and continue
        if WK in dictionary:
            W = WK
        # If it's not in the dictionary:
        else:
            # 1. Output the code for our known W
            result.append(dictionary[W])

            # 2. Add new chunk WK to the dictionary (learn it!)
            dictionary[WK] = next_code
            next_code += 1

            # 3. Start building a new sequence, W becomes letter K
            W = K

    # At the very end we must "push out" the last sequence W from memory
    if W:
        result.append(dictionary[W])

    return result, dictionary


# === TEST DATA ===
text_to_compress = "TOBEORNOTTOBEORTOBEORNOT#"

# Run compression
compressed_data, generated_dictionary = lzw_encode(text_to_compress)

print(f"Original text: {text_to_compress}")
print(f"Character count: {len(text_to_compress)}")
print("-" * 40)
print(f"Compressed codes (numbers):")
print(compressed_data)
print("-" * 40)
print("New phrases added to dictionary during reading:")
# Print only new codes (from 27 upwards)
for phrase, code in generated_dictionary.items():
    if code >= 27:
        print(f"Code {code}: '{phrase}'")
