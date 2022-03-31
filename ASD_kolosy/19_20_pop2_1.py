'''Mówimy, że punkt (x, y) słabo dominuje punkt (x
′
, y′
) jeśli x ≤ x
′
oraz y ≤ y
′
(w szczególności
każdy punkt słabo dominuje samego siebie). Dana jest tablica P zawierająca n punktów. Proszę
zaimplementować funkcję dominance(P), która zwraca tablicę S taką, że:
1. elementami S są indeksy punktów z P,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje,
3. S zawiera minimalną liczbę elementów.
Przykład. Dla tablicy:
P = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3) ]
# 0 1 2 3 4
wynikiem jest, między innymi:
S = [ 1, 4, 2 ]'''

# tworzymy tablice new, wypełniona zerami i Tablice i o strukturze [x i y danego punktu, indeks punktu w P]
# sortujemy quickiem tablice I po xach w pierwszej kolejnosci a po ykach w drugim priorytecie
# przechodzimy forem od najmniejszego xa (pakujemy ten punkt do S) i wpisujemy go jako ostatni. Sprawdzamy jakie punkty sa dominowane przez ten punkt i skipujemy je
# jesli trafimy na punkt nie dominowany przez naszego "lasta" to pakujemy go do S oraz ustawiamy go jako nowego lasta
# tak do wyczerpania
# złozonosc przeszukiwania jest O(n)
#

def partition_random_for_2_cryt(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x1 = T[r][0]
    x2 = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < x1:
            i += 1
            T[i], T[j] = T[j], T[i]

        elif T[j][0] == x1 and T[j][1] <= x2:
            i += 1
            T[i], T[j] = T[j], T[i]


    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random_for_2_cryt(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1


        else:
            quick_sort_mem2(T, q + 1, r)

            r = q - 1


def dominance(P):
    n = len(P)
    New = [[0]*3 for _ in range(n)]
    for i in range(n):
        New[i][0] = P[i][0]
        New[i][1] = P[i][1]
        New[i][2] = i

    quick_sort_mem2(New, 0, n -1)
    print(New)

    last = New[0]
    S = [New[0][2]]
    for i in range(1,n):
        if last[1] <= New[i][1]:
            continue
        else:
            S += [New[i][2]]
            last = New[i]

    return S

test = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3), (10,0), (1,2), (2,3)]
print(dominance(test))