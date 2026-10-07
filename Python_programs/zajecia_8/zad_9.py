def zad_9(n):
    trojkat = [1]
    obecna = 1
    for i in range(n):
        nowa = obecna * (n - i) // (i + 1) 
        # wynika to z uproszczenia silni przy podzieleniu elementu i + 1 w n wierszu przez i w n wierszu
        # wtedy wychodzi nam wartość po *
        trojkat.append(nowa)
        obecna = nowa
    print(trojkat)
zad_9(4)

def zad_9_v2(n):
    old_row = [1]
    for j in range (n):
        new_row =[1]
        for i in range(1, len(old_row)):
            new_row.append(sum(old_row[i - 1:i + 1]))
        new_row.append(1)
        old_row = new_row
    print(new_row)
zad_9_v2(4)
    
    