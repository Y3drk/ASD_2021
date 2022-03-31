'''Rozwiązanie
O(n ^ 2)
1.Stworzyć dwie tablice: posortowaną po x i posortowaną po y - O(nlogn). *Osobiscie uwazam ze wystarczyłoby posortowac tylko po x
2.Dla każdego przedziału: policzyć przedziały, które zaczynają się później i kończą się wcześniej.
3.Wyznaczyć przedział, który ma najwięcej takich przedziałów.

Rozwiązanie
O(n ^ 2)
1.Posortować przedziały po pierwszej współrzędnej.
2.Umieścić informacje o rozpoczęciu i zakończeniu przedziałów na osi x.
3.Stworzyć strukturę, w której węzeł będzie reprezentował przedział.
4.Przechodząc w sposób ciągły po osi x, aktualizować strukturę.'''

#rozwiazanie gorsze czyli to pierwsze, ale tez łatwiejsze


def biggest_interval(T):
    n = len(T)
    biggest, lght = None, 0
    quicksort(T)
    #print(T)
    for interval_base in range(n):
        counter = 0
        for interval_compared in range(n):
            if T[interval_compared][1] <= T[interval_base][1] and T[interval_compared][0] >= T[interval_base][0] and interval_compared != interval_base:
                counter += 1
                #print(T[interval_compared])

        if counter > lght:
            biggest = interval_base
            lght = counter
        #print("----")
    #print(lght)
    return T[biggest]


def quicksort(T):
    stos = []
    stos.append((0 , len(T) - 1))
    while len(stos) > 0:
        l, p = stos.pop()

        i, j = l, p
        x = T[(l + p) // 2][0]

        while i <= j:
            while T[i][0] < x:
                i += 1
            while T[j][0] > x:
                j -= 1

            if i <= j:
                T[j], T[i] = T[i], T[j]
                i += 1
                j -= 1

        if l < j:
            stos.append((l,j))

        if i < p:
            stos.append((i,p))

    return T

#rozwiazanie z cwiczen prof faliszewskiego , działanie na trójkach (nr przedziału, wspł, poczatek/koniec)


import random


def partition(T, l, p):
    a = random.randint(l, p)
    pivot = T[a][1]
    T[a], T[p] = T[p], T[a]
    j = l
    for i in range(l, p):
        if T[i][1] <= pivot:
            T[i], T[j] = T[j], T[i]
            j += 1
    T[p], T[j] = T[j], T[p]
    return j


def iter_quicksort_mem(T):
    S = []
    l, p = 0 , len(T) - 1
    S.append((l,p))
    while len(S) > 0:
        l,p = S.pop()
        if l < p:
            q = partition(T,l,p)
            if q - l < p - q:
                S.append(((q + 1, p)))
                S.append((l, q - 1))
            else:
                S.append((l, q - 1))
                S.append((q + 1, p))


def triples(T):    #tu powstaja nam nasze trójki
    new = []
    for i in range(len(T)):
        new.append((i,T[i][0],0))
        new.append((i, T[i][1],1))

    return new


def biggest_interwal_fal(T,lght):
    n = len(T)
    iter_quicksort_mem(T)
    begs, ends = 0, 0
    scores = [0 for _ in range(lght)]
    for i in range(n):
        if T[i][2] == 0:
            begs += 1
            scores[T[i][0]] -= begs
        if T[i][2] == 1:
            ends += 1
            scores[T[i][0]] += ends

    maxi = -1
    curr = None
    for j in range(lght):
        if scores[j] > maxi:
            maxi = scores[j]
            curr = j

    return curr


def launcher(T):
    lght = len(T)
    New = triples(T)
    ind = biggest_interwal_fal(New,lght)
    return T[ind]

#mozliwe ze tutaj troche oszukuje i robie cos w stylu tablicy asocjacyjnej, ktorej prof. Faliszewski nie chciał, ale innego pomysłu nie mam

test = [[1,2],[7,10],[8,23],[2,4],[6,9],[7,8],[7,9]]
print(biggest_interval(test))
print(launcher(test))