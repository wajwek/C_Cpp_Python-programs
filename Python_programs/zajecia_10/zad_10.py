def lista_na_slownik(lista):
    unikaty = set(lista)
    slownik = {}
    for unikat in unikaty:
        tmp = []
        for i in range(len(lista)):
            if lista[i] == unikat:
                tmp.append(i)
        slownik[unikat] = tmp
    return slownik
print(lista_na_slownik([1, 2, 2, 3, 1]))
        