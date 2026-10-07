def zad_4():
    print("Podaj 10 liczb:")
    tmp = []
    for i in range(10):
        x = input()
        tmp.append(int(x))
    nowe = []
    for i in tmp:
        if i not in nowe:
            nowe.append(i)
    print(tmp)
    print(nowe)
zad_4()