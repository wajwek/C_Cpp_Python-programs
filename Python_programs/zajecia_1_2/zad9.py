import random
x = int(random.randint(1, 20))
b = int(input("Podaj liczbe:"))

if b > x:
    print("za duza")
elif b < x:
    print("za mala")
else:
    print("trafiona")