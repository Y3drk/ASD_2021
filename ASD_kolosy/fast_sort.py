from zad1testy_fastsort import runtests
import math

# przechodzimy po tablicy i logarytmujemy liczby logarytmem o podstawie a, zostaną nam same x, o których wiemy, że sa rozłożone równomiernie na [0,1]
# sortujemy te x'y za pomoca bucket sorta
# posortowane x'y traktujemy jak argument funkcji wykładniczej f(x)=a^x aby odzyskac pierwotne wartosci

# złożoność O(n)


def select_sort(T):            #do sortowania wewnątrz kubełków bucket sort uzywa innego sortowania. Cormen poleca select sorta wiec i ja go uzyje
    n = len(T)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if T[j] < T[mini]:
                mini = j

        T[mini], T[i] = T[i], T[mini]

    return T


def bucket_sort(T):
    n = len(T)
    B = [[] * n for _ in range(n)]

    maxi = -1
    for l in range(n):
        if T[l] > maxi:
            maxi = T[l]

    for i in range(n):
        B[int(n*T[i] / (maxi + 1))] += [T[i]]
    for j in range(n):
        if B[j] != []:
            select_sort(B[j])
    T = []
    for k in range(n):
        if B[k] != []:
            T += B[k]

    return T


def fast_sort(tab, a):
    n = len(tab)
    for i in range(n):
        tab[i] = math.log(tab[i],a)

    tab = bucket_sort(tab)

    for j in range(n):
        tab[j] = a**tab[j]

    return tab



runtests( fast_sort )
