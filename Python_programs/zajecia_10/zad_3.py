import math

def to_radian(x):
    return x * math.pi / 180
def haversine(lat, lon):
    delta_lat = lat[0] - lat[1]
    delta_lon = lon[0] - lon[1]
    r = 6371 # km
    a = math.sin(delta_lat/2)**2 + math.cos(lat[0]) * math.cos(lat[1]) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c
