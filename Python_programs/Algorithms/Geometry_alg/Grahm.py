import math

def graham_scan(points):
    # Krok 1: Znajdź punkt o najmniejszej współrzędnej y.
    # W przypadku remisu, wybieramy punkt o najmniejszej współrzędnej x.
    p0 = min(points, key=lambda p: (p[1], p[0]))

    # Funkcja pomocnicza: Oblicza kąt biegunowy względem p0
    def polar_angle(p):
        return math.atan2(p[1] - p0[1], p[0] - p0[0])

    # Funkcja pomocnicza: Oblicza kwadrat odległości od p0
    # (przydatne przy punktach leżących na tej samej prostej z p0)
    def distance(p):
        return (p[0] - p0[0])**2 + (p[1] - p0[1])**2

    # Krok 2: Posortuj punkty względem kąta.
    # Pomijamy p0 w sortowaniu. Jeśli kąty są identyczne, wybieramy punkt dalszy.
    sorted_points = sorted([p for p in points if p != p0], key=lambda p: (polar_angle(p), distance(p)))

    # Funkcja wyznaczająca kierunek skrętu (iloczyn wektorowy)
    # Zwraca wartość dodatnią dla skrętu w lewo, ujemną dla prawego, a 0 jeśli są współliniowe
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    # Krok 3: Użyj stosu do budowy otoczki
    stack = [p0]
    if not sorted_points: return stack
    stack.append(sorted_points[0])

    for p in sorted_points[1:]:
        # Usuwaj punkty ze stosu, dopóki tworzą one "skręt w prawo" (lub linię prostą)
        # Chcemy mieć zawsze "skręt w lewo", który gwarantuje wypukłość
        while len(stack) > 1 and cross_product(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

# Przykład z zadania
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
result = graham_scan(points)
print(result)