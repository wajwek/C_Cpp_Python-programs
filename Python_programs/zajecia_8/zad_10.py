def zad_10(ciag):
    length = 1
    mx = 0
    tmp = 0
    for i in range(len(ciag) - 1):
        if ciag[i] == ciag[i + 1]:
            length += 1
        else:
            if ln > mx:
                mx = ln
                tmp = ciag[i]
            ln = 1
    if ln > mx:
        mx = ln
        tmp = ciag[i]
    print(tmp, mx)
zad_10()