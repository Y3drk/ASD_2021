#Jędrzej Ziebura

# Opis Algorytmu:
# 1) Sortujemy przedziały po początkach -
# 2) jesli jakieś przedziały na siebie nachodzą to wspólną cześć przyznajemy temu o większym prawdopodobieństwie
# 3) wewnątrz przedziału robimy sufit z ci * n bucketów
# 4) kontynuujemy jak w bucket sorcie

# złożoność - O(n*k) - przez szukanie odpowiedniego przedziału

from zad3testy import runtests


def insert_sort(T):
    n = len(T)
    for i in range(1, n):
        tmp = T[i]
        j = i - 1
        while (j >= 0) and (tmp < T[j]):
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = tmp

    return T


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r][0]
    i = p - 1
    for j in range(p, r):
        if T[j][0] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem(T,p,r):
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:
            quick_sort_mem(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem(T, q + 1, r)
            r = q - 1


def SortTab(T,P):
    import math
    n = len(T)
    quick_sort_mem(P,0, len(P) - 1)
    for i in range(1,len(P)):
        if P[i - 1][1] > P[i][0]:  # zał. przedziały na siebie nachodzą, ale nie zawieraja sie w sobie
            first, sec = P[i - 1][1], P[i][0]
            if P[i - 1][2] > P[i][2]:
                P[i] = (first,P[i][1],P[i][2])

            else:
                P[i - 1] = (P[i -1][0], sec, P[i- 1][2])

    Buckets = []
    for i in range(len(P)):
        Buckets += [[] for _ in range(math.ceil(P[i][2]*n))]

    z = len(Buckets)
    for i in range(n):

        for j in range(len(P)):
            if P[j][0] <= T[i] <= P[j][1]:
                Buckets[int(z*T[i]/P[j][1])] += [T[i]]

    for j in range(n):
        if Buckets[j] != []:
            insert_sort(Buckets[j])
    T = []
    for k in range(n):
        if Buckets[k] != []:
            T += Buckets[k]

    return

runtests( SortTab )