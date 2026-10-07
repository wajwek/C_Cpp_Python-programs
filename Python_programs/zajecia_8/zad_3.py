def zad_3():
    print("Podaj 5 temperatur:")
    tmp = []
    for i in range(5):
        x = input(str(i + 1) +  ". TMP: ")
        tmp.append(int(x))
    tmp[:] = [x * (9/5) + 32 for x in tmp]
    print("Średnia: ", sum(tmp)/5)
zad_3()