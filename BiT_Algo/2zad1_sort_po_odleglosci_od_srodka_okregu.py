'''Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim równomiernie rozłożone,
 tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru.
Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn. d = sqrt(x2 + y2).'''

#chcemy utrzymac to samo pole pierscieni czyli musimy mądrze znormalizowac kubełki

import math


def insert_sort(T):
    n = len(T)
    for i in range(1, n):
        tmp = T[i]
        j = i - 1
        while (j >= 0) and (tmp[2] < T[j][2]):
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = tmp

    return T


def distance(point):
    x, y = point
    return math.sqrt(x**2 + y**2)


def bucket_sort_circle_k(T,k):
    n = len(T)
    B = [[] * n for _ in range(n)]

    for i in range(n):
        T[i] += [distance(T[i])]
        print("add check:",T[i])   #spr poprawnosc dodawania distance
        B[int(n*(T[i][2]**2) / k**2)] += [T[i]]
        print("----")
        print("Bucket check:")
    for j in range(len(B)): #spr poprawnosci wrzucania do bucketów
        print(B[j])
    print("----")
    for j in range(n):
        if B[j] != []:
            insert_sort(B[j])
    T = []
    for k in range(n):
        if B[k] != []:
            T += B[k]

    return T


test = [[0,1],[2,3],[4,3],[1,4],[3,0],[1,1],[4,4],[0,2]]
print(bucket_sort_circle_k(test,8))

