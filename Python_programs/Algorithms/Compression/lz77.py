def lz77_compress(data):
    compressed = []
    cursor = 0
    # Size of history buffer (window) in which we look for repetitions
    window_size = 3

    while cursor < len(data):
        best_match_length = 0
        best_match_distance = 0

        # Limit search to the size of the history buffer
        start_history = max(0, cursor - window_size)

        # Look for the longest repeating sequence in history
        for i in range(start_history, cursor):
            length = 0
            # While characters in history and input buffer match
            while (cursor + length < len(data) and
                   data[i + length] == data[cursor + length]):
                length += 1

            # If we found a longer match, save it
            if length > best_match_length:
                best_match_length = length
                best_match_distance = cursor - i

        # Determine the next character after the matched fragment
        if cursor + best_match_length < len(data):
            next_char = data[cursor + best_match_length]
        else:
            next_char = ''  # End of data

        # Save result in format: (distance, length, next_char)
        compressed.append((best_match_distance, best_match_length, next_char))

        # Move cursor by match length and this one extra character
        cursor += best_match_length + 1

    return compressed


# Example from the task
data = "ABCABCA"
result = lz77_compress(data)
print("Compressed data:", result)
