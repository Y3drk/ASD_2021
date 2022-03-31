#podzielniki liczby
import math
n = int(input("Podaj liczbę: "))
d = 1
e = 0
while d <= math.sqrt(n):
    if n % d == 0:
        print("UwU:",d)
        e= n // d
        d += 1
        if e == n or e == math.sqrt(n):
            e = 0
        else:
            print(e)
    else:
        d += 1
