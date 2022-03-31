'''Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). Proszę zaproponować jak najszybszy algorytm, który znajduje ścieżkę z danego wierzchołka s do danego wierzchołka t taką, że:
1)Każda kolejne krawędź ma mniejszą wagę niż poprzednia
2)Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag'''


#alg Dijkstry ze wzgledu na krawedzie,
# 1) sortujemy krawedzie wychodzace z kazdego wierzchołka ze wzgledu na ich wage
# 2) każdy wierzchołek powinien posiadac licznik ilu krawedzi juz uzylismy, aby po kazdej krawedzi przejsc tylko raz
# 3) modyfikujemy relaksacje tak, aby kazda krawedz mniejsza od wejsciowej umiescic w kolejce (liczac od pozycji przechowywanej w strukturze z pkt 2)
# 4) tablica parent przechowuje (potencjalnie) dojscia z wszystkich mozliwych krawedzi w formie krotki:
# (odległosc od s do wierzchołka, waga krawedzi po ktorej przyszlismy, wierzchołek z którego przyszlismy)

# zł: O(ElogE)

def get_path(p, ind, prev,d, tmp): #O(E) - do tablicy parentów dodamy kazda krawedz max. raz i odzyskujac sciezke przejdziemy po kazdej dodanej krawedzi tez tylko raz
    #print(".....")
    #print(ind, prev, d, tmp)
    if len(p[ind]) != 0:
        for i in range(len(p[ind])):
            #print(p[ind][i][0], d - prev)
            if p[ind][i][0] == d - prev:
                tmp = get_path(p,p[ind][i][2],p[ind][i][1],p[ind][i][0],tmp + [ind])
                break

    return tmp


def Decreasing_path(G, s, t):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    parent = [[] for _ in range(n)]

    for i in range(n):   #(1)
        G[i].sort(key = lambda x: x[1])

    ind = [0 for _ in range(n)]  #(2)

    Q.put((0,float('inf'),s))

    def relax(u, prev, d):  # (3)
        while ind[u] < len(G[u]) and G[u][ind[u]][1] < prev:
            Q.put((d + G[u][ind[u]][1],G[u][ind[u]][1],G[u][ind[u]][0]))
            parent[G[u][ind[u]][0]].append((d + G[u][ind[u]][1],G[u][ind[u]][1],u))
            ind[u] += 1

    while not Q.empty():
        d, prev, u = Q.get()

        if u == t:
            break

        relax(u,prev,d)

    #print(parent)
    best = parent[t][0][0]
    if best != float('inf'):
        path = [t]
        path = get_path(parent,parent[t][0][2],parent[t][0][1],parent[t][0][0],path)
        path += [s]
        #print(path)
    else:
        path = []

    return path[::-1], best


test = [[(1, 5), (2, 8)], [(0, 5), (2, 3), (3, 9), (4, 4)], [(0, 8), (1, 3), (3, 2), (4, 2)],
        [(1, 9), (2, 2), (4, 3), (5, 1)], [(1, 4), (2, 2), (3, 3), (5, 6)], [(3, 1), (4, 6)]]
t = 5
s = 0
res = Decreasing_path(test, s, t)
print("Długosc sciezki od", s, "do", t, ":", res[1])
print("Sciezka:",res[0])
print("----")

G1 = [
    [[2, 100], [1, 4]],  # 0
    [[0, 4], [4, 3]],   # 1
    [[3, 200], [0, 100], [4, 4]],   # 2
    [[2, 200], [4, 3]],  # 3
    [[2, 4], [1, 3], [3, 3]]  # 4
]

res1 = Decreasing_path(G1, 0, 3)
print("Długosc sciezki od", 0, "do", 3, ":", res1[1])
print("Sciezka:",res1[0])


