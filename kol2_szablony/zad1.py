from zad1testy import runtests

#skorzystamy z funkcji f(i,p) = maksymalna ilosc studentów w ciagu legalnych budynków  konczacych sie w itym budynku, nie przekraczajaca kosztu p
# f(0,p) = { h(b0 - a0) jesli w0 < p lub 0 wpp }
# f(i,0) = 0 bo nie ma nic za darmo
# f(i,p) = max (po legalnych sasiadach i takich, że bsasiad < ai ) { f(sasiad, p - wi) + hi(bi - ai) jesli p - wi >= 0}
# w tablicy P zapisujemy jaki był ostatni budynek przed i-tym, tak bedziemy budowac odpowiedź


def select_buildings(T, p):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    for i in range(n):
        #         0        1      2       3     4
        T[i] = [T[i][1],T[i][2],T[i][0],T[i][3],i]

    T.sort()   #O(nlogn)
    print(T)

    G = buildings_to_graph(T)   #przekształcenie T na graf skierowany O(n^2)
    F = [[-1]*(p+1) for i in range(n)]
    P = [-1 for i in range(n)]

    for i in range(n):
        F[i][0] = 0

    for j in range(T[0][3],p+1):
        F[0][j] = T[0][2]*(T[0][1] - T[0][0])

    for i in range(1,n):
        for j in range(1,p+1):
            F[i][j] = F[i - 1][j]



    #for p in range()

    return []


def buildings_to_graph(T):
    n = len(T)
    G = [[0]*n for i in range(n)]
    for b in range(n):
        for a in range(a,n):
            if T[b][1] < T[a][0]:
                G[b][a] = 1

    return G


runtests( select_buildings ) 
