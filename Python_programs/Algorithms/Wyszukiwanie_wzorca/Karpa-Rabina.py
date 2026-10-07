def rabin_karp_search(text, pattern, b=256, p=101):
    '''
    b - podstawa systemu liczbowego, w naszym przypadku ASCII
    p - liczba pierwsza używana do modulo
    hash_p - wyliczony hash dla naszego wzorca, const
    hash_t - wyliczony hash dla aktualnie porównywanego fragmentu
    h - współczynnik pierwszej litery we wzorze na hash, b^(m-1) mod p
    '''

    n = len(text)
    m = len(pattern)
    results = []
    hash_p = 0
    hash_t = 0
    h = 1
    for i in range(m - 1):
        h = (h * b) % p
    for i in range(m):
        hash_p = (b * hash_p + ord(pattern[i])) % p
        hash_t = (b * hash_t + ord(text[i])) % p
    for i in range(n - m + 1): #chce sprawdzic jeszcze ostatni hash który został wcześniej policzony, teraz juz nie bedziemy liczyc nowego bo if nie przejdzie
        if hash_p == hash_t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                results.append(i)
        if i < n - m: # jesli została nowa litera jeszcze do wczytania, wyliczam następny hash, dlatego sprawdzam czy to nie jest ostatni zakazany element kiedy wyszedlbym poza tablice
            hash_t = (b * (hash_t - ord(text[i]) * h) + ord(text[i + m])) % p
            if hash_t < 0:
                hash_t = hash_t + p
    return results


tekst_kr = "W SZCZEBRZESZYNIE CHRZASZCZ BRZMI W TRZCINIE"
wzorzec_kr = "RZ"

wyniki_kr = rabin_karp_search(tekst_kr, wzorzec_kr)

print("-" * 50)
print(f"Przeszukiwany tekst: '{tekst_kr}'")
print(f"Szukany wzorzec:     '{wzorzec_kr}'")
print("-" * 50)

if wyniki_kr:
    print(f"Sukces! Wzorzec znaleziono na indeksach: {wyniki_kr}")
    for indeks in wyniki_kr:
        margines = " " * indeks
        print(f"Dopasowanie:          {margines}{wzorzec_kr}")
else:
    print("Nie znaleziono wzorca w tekście.")