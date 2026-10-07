def shift_tab(alphabet, pattern):
    shift = {}
    dist = {}
    for i in range(len(pattern)):
        dist[pattern[i]] = len(pattern) - 1 - i
    for i in range(len(alphabet)):
        if alphabet[i] not in dist:
            shift[alphabet[i]] = len(pattern)
        else:
            shift[alphabet[i]] = dist[alphabet[i]]
    return shift

def boyer_moore_search(text, patten, alphabet):
    shift = shift_tab(alphabet, patten)
    text_p = len(patten) - 1
    patten_p = len(patten) - 1
    while text_p < len(text):
        if text[text_p] == patten[patten_p]:
            patten_p -= 1
            text_p -= 1
        else:
            dist_backwards = len(patten) - patten_p - 1 #Bo nawet bez cofania zadeklarowane pattern_p dałoby dodatni wynik

            text_p += max(dist_backwards + 1, shift[text[text_p]]) #zabezpieczenie przed brakiem przesunięcia
            # chcemy się przesunąć o 1 od początkowego text_p albo o shift z miejsca przerwania, jeśli pójdziemy dalej niż oryginalny text_p

            patten_p = len(patten) - 1
        if patten_p == -1: #Odejmujemy 1 po sprawdzeniu więc wynik dla ostatniego to 0 - 1 = -1
            return text_p + 1, text_p + len(patten) #Bo wcześniej odjęliśmy 1 po sprawdzeniu
    return None

alfabet_prezentacji = "ABCDEFGH"
tekst_bm = "ABGHHAABGBDE"
wzorzec_bm = "ABGBD"

wyniki_bm = boyer_moore_search(tekst_bm, wzorzec_bm, alfabet_prezentacji)

print("-" * 30)
print(f"Przeszukiwany tekst: '{tekst_bm}'")
print(f"Szukany wzorzec:     '{wzorzec_bm}'")
print("-" * 30)

if wyniki_bm:
    print(f"Sukces! Wzorzec znaleziono na indeksach: {wyniki_bm}")
    margines = " " * wyniki_bm[0]
    print(f"Dopasowanie:          {margines}{wzorzec_bm}")
else:
    print("Nie znaleziono wzorca w tekście.")