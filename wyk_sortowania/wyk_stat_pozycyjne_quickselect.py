#ofc w tzw. przykładach elementarnych czyli szukaniu min i max wystarczy przejsc raz po tablicy
#nas interesuja ciekawsze przypadki

def partition_random(T, p, r):   #miedzy innymi stad nazwa algorytmu, że korzystamy z metod stosowanych w quicksorcie
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[
            j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quickselect(T,p,r,k):     #jestesmy w tablicy, szukamy elementu, który znajdowałby się na  k-tej pozycji w posortowanej tablicy, szukamy miedzy indeksami p i r
    if p == r:     #jest to funkcja rekurencyjna, wiec mamy ofc warunek końca
        return T[p]

    q = partition_random(T,p,r)  #odpalamy partition na zadanym obszarze,

    if q == k:    #jesli q == k to juz wiemy na pewno, że jestesmy na dobrej pozycji
        return T[q]

    elif k < q:     #w zalezności od położenia pivota wzgledem k wybieramy konkretne wywołanie, ucina to nam równiez rekurencje ogonowa
        return quickselect(T,p, q - 1, k)

    else:
        return quickselect(T, q + 1, r, k)


test = [1, 7, 10, 11, 8]
print(quickselect(test,0, len(test) - 1, 2))