def sortowanie(tab):
    flaga = True
    krok = 0
    while flaga:
        krok += 1
        flaga = False
        for i in range(len(tab) - krok):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                flaga = True

    return tab

T = [7,4,55,67,8,2,3,44,12,1,2,9]
T2 = [9,1,6,3,7]
print(sortowanie(T2))