import random

def zad_5():
    matrix = []
    for i in range(3):
        tmp = [int(random.randint(0, 100)), int(random.randint(0, 100)), int(random.randint(0, 100))]
        matrix.append(tmp)
    matrix[2][2] = sum([matrix[x][0] for x in range(3)]) + sum([matrix[x][1] for x in range(3)]) + sum([matrix[x][2] for x in range(2)])
    print(matrix)
    print(" ")
    for j in range(3):
        print(matrix[j])
    print(sum([matrix[x][2] for x in range(3)]))
zad_5()
