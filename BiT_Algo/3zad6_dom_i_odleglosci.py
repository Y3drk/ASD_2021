'''Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi, w którym z nim należy wybudować dom,
 tak aby suma euklidesowych odległości od tego punktu do wszystkich pozostałych była minimalna.
 Należy zwrócić również tę sumę. Algorytm powinien być jak najszybszy.'''

#worth noting rozwiazania
# - dla nieposortowanych sam punkt - quickselect elementu srodkowego
# - dla posortowanych sam punkt - n//2 indeks jesli n nieparzyste, wpp, liczymy sume dla dwóch srodkowcyh punktów i wybieramy ten o mniejszej sumie

#nasze rozwiazanie - dla nieposortowanych, gdzie zwracamy i punkt, i sume
#1 - sortujemy tablice
#2 - tworzymy dwie tablice - sumy odległosci od lewej i sumy od prawej
#3 - idac liniowo zapamietujemy punkt z najmniejsza suma odległosci i tą sume

def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
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


def build_a_house(T):
    n = len(T)
    quick_sort_mem2(T,0,n - 1)
    L = [0 for i in range(n)]
    R = [0 for i in range(n)]

    for i in range(1,n):
        L[i] = L[i - 1] + i *(T[i] - T[i - 1])

    for i in range(n -2, -1, -1):
        R[i] = R[i + 1] + (n - 1 -i)*(-T[i] + T[i + 1])   #stworzenie tablic sum odległości

    #print(L)
    #print(R)

    minimal = 10**6
    place = None

    for i in range(n):
        sm = R[i] + L[i]
        if sm < minimal:
            minimal = sm
            place = i

    return place,T[place],minimal


test_1_np = [0, 1, 2, 3, 4, 5, 6]
test_2_p = [0, 1, 2, 3, 4, 5, 6, 7]
print("test_1_np")
print(build_a_house(test_1_np))
print("test_2_p")
print(build_a_house(test_2_p))



