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
    # Convex hull with less than 3 points is simply those points
    if len(points) < 3:
        return points

    # 1. Find the starting point (leftmost, lowest in case of a tie)
    start_point = min(points, key=lambda p: (p[0], p[1]))
    hull = []

    current_point = start_point

    while True:
        hull.append(current_point)

        # 2. Choose any point as the first candidate for the next hull vertex.
        # Ensure the candidate is not our current point.
        next_point = points[0]
        if next_point == current_point:
            next_point = points[1]

        # 3. Search for the "rightmost" point relative to the line (current_point -> next_point)
        for r in points:
            if r == current_point or r == next_point:
                continue

            cp = cross_product(current_point, next_point, r)

            # If r is on the right side (right turn), r is a better candidate.
            # Replace next_point with r.
            if cp < 0:
                next_point = r

            # If collinear, choose the point that is further away.
            # This bypasses points lying flat on the hull edge.
            elif cp == 0:
                if distance_sq(current_point, r) > distance_sq(current_point, next_point):
                    next_point = r

        # 4. Move to the best found candidate
        current_point = next_point

        # 5. If we have wrapped around all points and returned to start, finish
        if current_point == start_point:
            break

    return hull


# --- Example usage ---
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
convex_hull = jarvis_march(points)

print("Hull points (in order):")
for p in convex_hull:
    print(p)
