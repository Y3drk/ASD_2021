'''Dana jest tablica punktów (structy z intami x, y). Punkt 1 dominuje 2 gdy x1 > x2 i y1 > y2.
Zaimplementuj algorytm znajdujący liczność najmniejszego zbioru, takiego że wybrane punkty dominują
wszystkie niewybrane. W 1-2 zdaniach opisz jego działanie i oszacuj złożoność obliczeniową.'''

# sort po obu współrzednych]
# przejscie od najmniejszego i sprawdzenie dominowania, poniewaz relacja jest przechodnia to nie wydarzy sie sytuacja ze odznaczony punkt dominowałby cos co nie
# zostanie zaznaczone.


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


def dominance(T):
    n = len(T)
    quick_sort_mem2(T,0,n-1)
    S = []
    Marked = [False for _ in range(n)]
    ind = 0
    while ind < n:
        if Marked[ind]:
            ind += 1

        else:
            S.append(T[ind])
            for i in range(ind + 1,n):
                if T[ind][0] <= T[i][0] and T[ind][1] <= T[i][1]:
                    Marked[i] = True

            ind += 1

    return S


T0 = [(1,1),(2,2)]
odp = (1,1)
print(dominance(T0))

T1 = [(4,3),(7,8),(9,9),(1,3),(3,9),(4,5),(9,8),(10,0)]
odp = [(1,3),(10,0)]
print(dominance(T1))
