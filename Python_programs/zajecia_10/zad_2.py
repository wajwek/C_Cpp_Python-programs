def odl3d(a, b):
    x1 = a[0]
    x2 = b[0]
    y2 = a[1]
    y1 = b[1]
    z2 = a[2]
    z1 = b[2]
    d = float(((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**(1/2))
    return d
print(odl3d((1,2,3),(2,1,0)))