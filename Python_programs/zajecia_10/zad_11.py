def counter(tab): #gdzie tab to np.[[1,2,3], [2,2]]
    slownik = {}
    if not isinstance(tab, list):
        return print("Zły format danych")
    for lista in tab:
        if not isinstance(lista, list):
            return print("Zły format danych")
        lista = set(lista)
        for element in lista: # Jeśli elementu nie ma, daj 0, a potem dodaj 1, całkiem spoko
            slownik[element] = slownik.get(element, 0) + 1
    return print("W największej ilości zbiorów", max(slownik, key=slownik.get))
counter([[1,2], [3,1], [2, 1], [1, 3]])

        
            