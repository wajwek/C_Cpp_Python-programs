pasma = {
  80: (3.500, 3.800),
  40: (7.000, 7.200),
  20: (14.000, 14.350),
  15: (21.000, 21.450),
  10: (28.000, 29.700)
}

def czy_w_pasmie(pasmo):
    for key in pasma:
        if pasma[key][0] <= pasmo <= pasma[key][1]:
            return print("Pasmo:", key)
    return print("Poza pasmem")
czy_w_pasmie(7)