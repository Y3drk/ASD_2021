
for i in range(0, 2 ** n):
    tab = [0 for i in range(n)]
    for j in range(n - 1, -1, -1):
        if i & 2 ** j:
            tab[j] = 1
        else:
            tab[j] = 0

