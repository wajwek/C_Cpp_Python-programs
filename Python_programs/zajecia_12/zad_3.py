def raport(filename):
    try:
        with open(filename, 'r') as file:
            m = float('inf')
            M = 0
            avg = 0
            counter = 0
            for line in file.readlines():
                digit = int(line)
                counter += 1
                if digit > M: M = digit
                if digit < m: m = digit
                avg += digit
            avg = round(avg/counter, 2)
            file.close()
            with open("raport", 'w') as raport:
                raport.write("Minimum: " + str(m) + '\n' + "Maximum: " + str(M) + '\n' + "Avg: " + str(avg))
                raport.close()
    except Exception as e:
        print("Błąd", e)
raport("test.txt")

