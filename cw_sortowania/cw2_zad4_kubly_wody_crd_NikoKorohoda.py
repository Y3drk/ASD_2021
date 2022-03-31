'''Rozwiązanie O(nlogn)(narzucone przez pkt 2.)

1.Przekształcić dane wejściowe (współrzędne pojemników) na struktury: (wysokość - jak wysoko znajduje się to “wydarzenie”;szerokość;typ - początek / koniec)
2.Posortować po wysokości
3.Tak długo jak obecnie wymagana ilość wody nie przekracza dostępnej wykonywać punkty 4. oraz 5.
4.Obecnie wymagana ilość wody += obecnie rozważana szerokość (suma wszystkich już rozważonych szerokości “początków” minus suma wszystkich już rozważonych
szerokości  “końców”) *różnica wysokości między obecnie rozważanym wydarzeniem a ostatnio rozważanym
5.Jeśli obecnie rozważane wydarzenie to “koniec” to zwiększ rozwiązanie o 1
6.Rozwiązanie to rozwiązanie.
7.O kurwa to działa < 3

def wlej_wode(A, w):
    cnt = 0
    curr_szerokosc = 0
    last_wysokosc = 0
    i = 0
    while i < len(A):    # (2)
        w = w - (A[i][0] - last_wysokosc) * curr_szerokosc
        if w >= 0:
            if A[i][2] == koniec:
                cnt += 1
        else:
            break

        if A[i][2] == poczatek:
            curr_szerokosc += A[i][1]
        else:
            curr_szerokosc -= A[i][1]
        i += 1
    return cnt'''

poczatek = 0
koniec = 1


# zakladam ze dane sa na poczatku w postaci (x1,y1,x2,y2), gdzie y1 < y2


def zmien_dane(A):  # (1)
    nowa = []
    for elem in A:
        szerokosc = abs(elem[0] - elem[2])
        nowa.append([elem[1], szerokosc, poczatek])
        nowa.append([elem[3], szerokosc, koniec])
    return nowa

def lanie_wody(buckets,limit):
    counter, last_height, curr_width, i = 0, 0, 0, 0
    while i < len(buckets):
        limit -= (buckets[i][0] - last_height) * curr_width
        if limit >= 0: #warunek konca
            if buckets[i][2] == koniec:
                counter += 1
        else:
            break

        if buckets[i][2] == poczatek:
            curr_width += buckets[i][1]
        else:
            curr_width -= buckets[i][1]

        last_height = buckets[i][0]
        i += 1

    return counter


def mergesort(T):  #przysposobiony

    n = len(T)
    if n > 1:
        mid = n // 2
        left = T[:mid]
        right = T[mid:]
        mergesort(left)
        mergesort(right)

        j, k = 0, 0
        guard_l, guard_r = 10**3, 10**3
        left += [[guard_l]]
        right += [[guard_r]]
        for i in range(n):
            if left[j][0] <= right[k][0]:
                T[i] = left[j]
                j += 1
            else:
                T[i] = right[k]
                k += 1
    return T

dane = [(1,0,4,3),(5,1,9,5),(7,2,12,6)]
wlasciwe_dane = zmien_dane(dane)
mergesort(wlasciwe_dane)
print(wlasciwe_dane)
print(lanie_wody(wlasciwe_dane, 40))