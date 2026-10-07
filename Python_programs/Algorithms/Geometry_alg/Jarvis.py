def cross_product(p1, p2, p3):
    """
    Oblicza iloczyn wektorowy (wyznacznik).
    Zwraca:
    > 0 : skręt w lewo
    < 0 : skręt w prawo
    == 0: punkty są współliniowe
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def distance_sq(p1, p2):
    """Oblicza kwadrat odległości między dwoma punktami (bez pierwiastka dla optymalizacji)."""
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


def jarvis_march(points):
    # Otoczka wypukła z mniej niż 3 punktów to po prostu te punkty
    if len(points) < 3:
        return points

    # 1. Znajdź punkt startowy (najbardziej wysunięty na lewo, w razie remisu najniżej)
    start_point = min(points, key=lambda p: (p[0], p[1]))
    hull = []

    current_point = start_point

    while True:
        hull.append(current_point)

        # 2. Wybieramy dowolny punkt jako pierwszego kandydata na kolejny wierzchołek otoczki.
        # Upewniamy się tylko, że kandydat to nie jest nasz obecny punkt.
        next_point = points[0]
        if next_point == current_point:
            next_point = points[1]

        # 3. Szukamy "najbardziej prawego" punktu względem linii (current_point -> next_point)
        for r in points:
            if r == current_point or r == next_point:
                continue

            cp = cross_product(current_point, next_point, r)

            # Jeśli r jest po prawej stronie (skręt w prawo), to r jest lepszym kandydatem.
            # Zastępujemy next_point punktem r.
            if cp < 0:
                next_point = r

            # Jeśli są współliniowe, wybieramy ten punkt, który jest dalej.
            # Dzięki temu omijamy punkty leżące płasko na krawędzi otoczki.
            elif cp == 0:
                if distance_sq(current_point, r) > distance_sq(current_point, next_point):
                    next_point = r

        # 4. Przesuwamy się na najlepszego znalezionego kandydata
        current_point = next_point

        # 5. Jeśli owinęliśmy wszystkie punkty i wróciliśmy na start, kończymy
        if current_point == start_point:
            break

    return hull


# --- Przykładowe użycie ---
punkty = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
otoczka = jarvis_march(punkty)

print("Punkty otoczki (w kolejności):")
for p in otoczka:
    print(p)