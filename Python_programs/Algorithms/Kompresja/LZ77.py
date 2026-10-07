def lz77_compress(data):
    compressed = []
    cursor = 0
    # Rozmiar bufora historii (okna), w którym szukamy powtórzeń
    window_size = 3

    while cursor < len(data):
        best_match_length = 0
        best_match_distance = 0

        # Ograniczamy przeszukiwanie do rozmiaru bufora historii
        start_history = max(0, cursor - window_size)

        # Szukamy najdłuższego powtarzającego się ciągu w historii
        for i in range(start_history, cursor):
            length = 0
            # Dopóki znaki w historii i w buforze wejściowym się zgadzają
            while (cursor + length < len(data) and
                   data[i + length] == data[cursor + length]):
                length += 1

            # Jeśli znaleźliśmy dłuższe dopasowanie, zapisujemy je
            if length > best_match_length:
                best_match_length = length
                best_match_distance = cursor - i

        # Określamy kolejny znak po dopasowanym fragmencie
        if cursor + best_match_length < len(data):
            next_char = data[cursor + best_match_length]
        else:
            next_char = ''  # Koniec danych

        # Zapisujemy wynik w formacie: (przesunięcie, długość, kolejny znak)
        compressed.append((best_match_distance, best_match_length, next_char))

        # Przesuwamy kursor o długość dopasowania i ten jeden dodatkowy znak
        cursor += best_match_length + 1

    return compressed


# Przykład z zadania
dane = "ABCABCA"
wynik = lz77_compress(dane)
print("Skompresowane dane:", wynik)