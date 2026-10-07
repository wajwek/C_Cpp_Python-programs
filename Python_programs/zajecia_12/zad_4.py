def file_stats(filename):
    try:
        with open(filename, 'r') as file:
            char_counter = 0
            word_counter = 0
            line_counter = 0
            for line in file.readlines():
                line_counter += 1
                words = line.strip().split( )
                word_counter += len(words)
                for word in words:
                    char_counter += len(word)
            file.close()
            return tuple(["Linie: " + str(line_counter), "Słowa: " + str(word_counter), "Znaki: " + str(char_counter)])
    except Exception as e:
        print("Błąd", e)
print(file_stats("test.txt"))