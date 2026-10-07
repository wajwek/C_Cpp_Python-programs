import math

def to_radian(x):
    return x * math.pi / 180
def haversine(lat, lon):
    delta_lat = to_radian(lat[0]) - to_radian(lat[1])
    delta_lon = to_radian(lon[0]) - to_radian(lon[1])
    r = 6371 # km
    a = math.sin(delta_lat/2)**2 + math.cos(to_radian(lat[0])) * math.cos(to_radian(lat[1])) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c

def trasa(tab): # Przyjmuje dane typu ((1, 2), (2, 1), (3, 1))
    suma = 0
    for i in range(1, len(tab)):
        t1 = [tab[i - 1][0], tab[i][0]]
        t2 = [tab[i - 1][1], tab[i][1]]
        suma += haversine(t1, t2)
    return suma
