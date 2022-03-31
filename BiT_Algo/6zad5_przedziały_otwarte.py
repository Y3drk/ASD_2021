'''Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru, taki że:
1) jego rozmiar wynosi dokładnie k
2) przedziały są rozłączne
3) różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna.
Jeśli rozwiązanie nie istnieje, to algorytm powinien to stwierdzić. Algorytm powinien być w miarę możliwości szybki, ale przede wszystkim poprawny.
'''

# idea - Dla każdego przedziału znajdujemy inny przedział, taki że nie zachodzą na siebie i różnica między początkiem pierwszego i końcem drugiego jest minimalna.
# Następnie próbujemy spacerować po tak znalezionych sąsiadach i sprawdzamy, czy udało nam się przejść k przedziałów.


def partition_intervals(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]    #dokonujemy wyboru losowego elementu i zamieniamy go z ostatnim elementem

    x_time = T[r][0]
    x_type = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < x_time:
            i += 1
            T[i], T[j] = T[j], T[i]
        elif T[j][0] == x_time:
            if T[j][1] <= x_type:
                i + 1
                T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_intervals(T, p, r)
        if q - p <= r - q:   # zawsze wywołujemy quicksorta dla mniejszej czesci powstałej po podziale, a dla wiekszej czesci wracamy do poczatku pętli
            quick_sort_mem2(T, p, q - 1)
            p = q + 1 #i wywołujemy dla niej partition jeszcze raz

        else:
            quick_sort_mem2(T, q + 1, r)   #jak wyżej tylko tutaj mamy przypadek gdy prawa czesc jest mniejsza
            r = q - 1


def k_intervals(T,k):
    n = len(T)
    quick_sort_mem2(T,0, n - 1)
    Neighbours = [None for i in range(n)]
    print(T)

    for i in range(n):
        beg = T[i][0]
        fin = T[i][1]
        best = float('inf')
        ind_best = n
        for j in range(i + 1,n):
            if T[j][0] >= fin and T[j][1] - beg < best: #ciche zał: przedziały sa lewostronnie otwarte
                best = T[j][1] - beg
                ind_best = j

        Neighbours[i] = ind_best

    print(Neighbours)

    top = float('inf')
    top_intervals = None

    for i in range(n):
        tmp = [i]
        if Neighbours[i] != n:
            ind = Neighbours[i]
            while ind < n:
                tmp += [ind]
                ind = Neighbours[ind]

                if len(tmp) == k:
                    if T[tmp[len(tmp)- 1]][1] - T[tmp[0]][0] < top:
                        top = T[tmp[len(tmp)- 1]][1] - T[tmp[0]][0]
                        top_intervals = tmp
                        break

    if top_intervals == None:
        return False

    else:
        for interval in top_intervals:
            print(T[interval], end=', ')

        print()

    return top


test = [(0,6),(11,15),(4,8),(3,10),(12,18),(6,9),(14,20),(7,13)]
k = 3
print(k_intervals(test,k))

# WYDAJE SIE DZIALAC 