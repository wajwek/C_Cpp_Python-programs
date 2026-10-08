def slownik(tab):
    tab = tab.split(",")
    dir = {}
    for x in tab:
        if x.count(":") != 1:
            print("Niepoprawny format danych")
            return False
        x = x.split(":")
        dir[x[0]] = x[1]
    print(dir)
slownik("ab:1,cd:23,qw:q")