results = [
 ("Team A", 10), ("Team B", 12), ("Team C", 8),
 ("Team A", 5),  ("Team B", 8),  ("Team C", 10),
 ("Team A", 7),  ("Team B", 6),  ("Team C", 12)
]
def generate_raport(results):
    points = {}
    for krotka in results:
        points[krotka[0]] = points.get(krotka[0], 0) + krotka[1]
    points_avg = {}
    for team in points:
        avg = round(points[team]/3, 2)
        points_avg[team] = avg
    tab = []
    for result in results:
        if result[1] >= 10 and result[0] not in tab:
            tab.append(result[0])
    print(points)
    print(points_avg)
    print(tab)
generate_raport(results)