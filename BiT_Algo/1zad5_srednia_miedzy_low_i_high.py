# inne zadania sa w asd
'''Proszę zaimplementować funkcję:
double AverageScore(double A[], int n, int lowest, int highest);
Funkcja ta przyjmuje na wejściu tablicę n liczb rzeczywistych (ich rozkład nie jest znany, ale wszystkie są parami różne)
 i zwraca średnią wartość podanych liczb po odrzuceniu lowest najmniejszych oraz highest największych.
 Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność czasową (oraz bardzo krótko uzasadnić to oszacowanie).'''


def partition(T, l, r, ind):    #przerobione tak aby mogło przyjmowac indeks elementu którego chcemy przyjąc za pivota
    x = T[ind]
    T[ind], T[r] = T[r], T[ind]
    i = l - 1
    for j in range(l, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quickselect(T,p,r,k): #przystosowany by zwracac obecny indeks połozenia tej liczby
    if p == r:
        return p

    q = partition(T,p,r,r)

    if q == k:
        return q

    elif k < q:
        return quickselect(T,p, q - 1, k)

    else:
        return quickselect(T, q + 1, r, k)


def Average_score(T,lowest,highest):
    n = len(T)

    lowest = quickselect(T,0,n-1,lowest - 1)
    #print(lowest, T[lowest])

    q = partition(T,0,n-1,lowest)
    #print(T)

    highest = quickselect(T,0,n-1, n - highest)
    #print(highest, T[highest])
    _ = partition(T,q,n-1,n - highest)
    #print(T)
    suma, cnt = 0, 0
    for i in range(lowest + 1,highest):
        suma += T[i]
        cnt += 1
        #print(T[i])

    #print(suma, cnt)
    return suma / cnt


test = [2,6,7,8,15,23,40,1,9,3]
lowest, highest = 3, 3
print(Average_score(test,lowest,highest))