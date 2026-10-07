# --- POMOCNICZA MATEMATYKA ---
def ccw(A, B, C):
    """Sprawdza ułożenie (skręt) 3 punktów. Zwraca True jeśli zakręcają w lewo."""
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def przecinaja_sie(s1, s2):
    """Krótki i sprytny sposób na wykrycie przecięcia dwóch odcinków."""
    if not s1 or not s2: return False
    A, B, C, D = s1[0], s1[1], s2[0], s2[1]
    # Odcinki się przecinają, jeśli ich końce leżą po przeciwnych stronach siebie nawzajem
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def pobierz_y(s, x):
    """Liczy aktualną wysokość Y odcinka dla danej pozycji X miotły."""
    (x1, y1), (x2, y2) = s
    return y1 if x1 == x2 else y1 + (y2 - y1) * (x - x1) / (x2 - x1)


# --- ALGORYTM SHAMOSA-HOEYA (wersja zwięzła) ---
def shamos_hoey(odcinki):
    # Tworzymy zdarzenia: (Współrzędna X, typ_zdarzenia, odcinek)
    # typ 0 -> Początek (Insert), typ 1 -> Koniec (Delete)
    zdarzenia = []
    for s in odcinki:
        zdarzenia.extend([(s[0][0], 0, s), (s[1][0], 1, s)])
    zdarzenia.sort()  # Zamiatamy od lewej do prawej

    T = []  # Stan miotły (zwykła lista zamiast drzewa dla uproszczenia)
    for x, typ, s in zdarzenia:
        if typ == 0:  # LEWY KONIEC: Insert(T, s)
            T.append(s)
            T.sort(key=lambda od: pobierz_y(od, x))  # Posortuj wg Y w aktualnym X

            idx = T.index(s)
            nad = T[idx - 1] if idx > 0 else None
            pod = T[idx + 1] if idx < len(T) - 1 else None

            # Czy Above(T, s) lub Below(T, s) przecina s?
            if przecinaja_sie(nad, s) or przecinaja_sie(pod, s): return True

        else:  # PRAWY KONIEC: Delete(T, s)
            idx = T.index(s)
            nad = T[idx - 1] if idx > 0 else None
            pod = T[idx + 1] if idx < len(T) - 1 else None

            # Czy Above(T, s) i Below(T, s) przecinają się?
            if przecinaja_sie(nad, pod): return True
            T.remove(s)

    return False


# --- TEST ---
if __name__ == '__main__':
    # Uwaga: punkty w krotkach podajemy zawsze od lewej do prawej (x1 <= x2)!
    odcinki = [
        ((20, 20), (80, 80)),  # S1
        ((10, 50), (40, 50)),  # S3 (tarcza)
        ((30, 80), (90, 20))  # S2
    ]
    print("Czy jakiekolwiek odcinki się przecinają?", shamos_hoey(odcinki))