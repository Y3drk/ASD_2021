#Jędrzej Ziebura

# idea - do elementów tablicy dopiszemy sobie ich pierwotna pozycje, nastepnie posortujemy stabilnie tablice i sprawdzimy
# maksymalne przeniesienie kazdego elementu. Na tej podstawie, korzystajac z podanych warunków 1 i 2, wybierzemy k.

# złożoność - czasowa -> O(nlogn) { brak nam założen pozwalajacych posortowac tablice w czasie liniowym}
# pamięciowa -> O(n) - na zapamiętanie indeksów elementów przed posortowaniem.

from zad1testy import runtests


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x0 = T[r][0]
    x1 = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < x0:
            i += 1
            T[i], T[j] = T[j], T[i]

        elif T[j][0] == x0 and T[j][1] < x1:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


def chaos_index( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    for i in range(n):
        T[i] = [T[i],i]

    print(T)
    #sortowanie O(nlogn)
    quick_sort_mem2(T,0,n-1)

    print(T)
    maximal = -1
    for i in range(n):
        maximal = max(maximal, abs(i - T[i][1]))

    return maximal


runtests( chaos_index )


