# rozdzielamy przedziały na krotki (punkt, czy poczatek(0) czy koniec(1)) i sortujemy niemalejaco wg punktów, nierosnaco wg stanów (p lub k). O(2nlog2n)
# potem przechodzimy linowo po tak posortowanej tablicy i jesli trafiamy na poczatek przedziału to zwiekszamy licznik i ustalamy nowy poczatek potnencjalnego
# podprzedziału. Jesli trafimy na koniec to sprawdzamy czy licznik >= 2 (czy "otworzylismy" conajmniej 2 przedziały ergo nie liczymy długosci jednego przedziału)
# i czy taki podprzedział poprawia nam wynik O(2n)

# złozonosc -> czasowa, narzucona przez sortowanie O(2nlog2n)
# pamieciowa -> O(n) na dodatkowa tablica trzymajaca krotki


def partition_random_twice(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]    #dokonujemy wyboru losowego elementu i zamieniamy go z ostatnim elementem

    x0 = T[r][0]
    x1 = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < x0:
            i += 1
            T[i], T[j] = T[j], T[i]

        elif T[j][0] == x0 and T[j][1] > x1:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random_twice(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


def intervals(T):
    n = len(T)
    New = []
    counter = 0
    beg = None

    for i in range(n):
        New.append((T[i][0], 0))
        New.append((T[i][1], 1))

    quick_sort_mem2(New,0,len(New)-1)

    best = 0
    interval = (None, None)

    for j in range(len(New)):
        if New[j][1] == 0:
            counter += 1
            beg = New[j][0]

        if New[j][1] == 1:
            if counter >= 2:
                if best < New[j][0] - beg:
                    best = New[j][0] - beg
                    interval = (beg, New[j][0])

            counter -= 1

    return interval


T1 = [(1,5),(1,3),(4,6),(7,8),(8,10),(12,15)]
print(intervals(T1),(1,3))
T2 = [(10,11),(9,10),(8,9),(1,2),(2,3),(6,7),(1,3),(11,15),(12,15)]
print(intervals(T2),(12,15))
T3 = [(0,10),(1,3),(3,7),(7,11),(10,11)]
print(intervals(T3),(3,7))
