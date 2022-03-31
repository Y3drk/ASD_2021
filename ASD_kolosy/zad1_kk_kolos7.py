def if_prime(x):
    if x == 2 or x == 3:
        return True

    if (x % 2 == 0 and x != 2) or x == 1:
        return False

    licz = 3
    while licz <= x ** (1/2):
        if x % licz == 0:
            return False
        else:
            licz += 2

    return True

def preprocess(G):
    n = len(G)
    New = [[] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            if if_prime(j[0]) and (j[0] < i or i == 0):
                New[i].append(j)

    #print(New)
    return New


def babiarz(G,T,W):
    #gdyby krawedzie były posortowane to mielibysmy przynajmniej pewnosc, ze juz te krawedz wykorzystalismy i nie poszlibysmy dwa razy ta sama krawedzia
    # a tak to nie wiem gdzie sobie spaceruje cwaniak
    # visited nie przywalimy bo zepsuje zadanie, krawedzi tez nie mozemy usuwac bo pop jest liniowe

    # to potencjalnie bada wszystkie sciezki w grafie - jakis kosmos

    #przgeladamy wszystkie krawedzie i jesli dana krawedz i konczacy ja wierzchołek spełnia wszystkie założenia to tam idziemy
    results = []
    G1 = preprocess(G)
    from queue import PriorityQueue
    Q = PriorityQueue()
    Q.put((0, 0, [0],"Brun")) # (droga, wierzchołek, sciezka, kto był ostatnio odwiedzany)
    Q.put((0, 0, [0], "Blond"))
    while not Q.empty():
        d,v,tmp, last = Q.get()
        flag = False
        '''if_prime(u[0]) and (v > u[0] or v == 0)'''
        for u in G1[v]:
            if T[u[0]] != last and W - d - u[1] >= 0:
                Q.put((d + u[1],u[0],tmp + [u[0]],T[u[0]]))
                flag = True

        if not flag:
            results.append(tmp)

    #print(results)
    best = None
    best_len = 0
    for i in range(len(results)):
        if len(results[i]) > best_len:
            best = results[i]
            best_len = len(results[i])

    #print(best)
    return best

    #pamiętaj, że jesteś wspaniała/y :) <3

G1 = [[(1, 1), (2, 5), (3, 11), (4, 3)], [(0, 1), (3, 3), (5, 1), (6, 1)], [(0, 5), (3, 3), (5, 42)],
      [(2, 3), (1, 1), (0, 11)], [(0, 3)], [(2, 42), (1, 1)], [(1, 1)]]
T1 = ["Łysy", "Brun", "Brun", "Blond", "Blond", "Blond", "Blond"]
W1 = 47
odp1 = [0, 3, 2]

G2 = [[(11, 21), (8, 15), (1, 1), (2, 5), (3, 11), (4, 3)], [(0, 1), (3, 3), (5, 1), (6, 1)],
      [(0, 5), (3, 3), (5, 42)], [(2, 3), (1, 1), (0, 11)], [(0, 3)], [(2, 42), (1, 1)], [(1, 1)],
      [(4, 1), (8, 10), (5, 5)], [(0, 15), (7, 10)], [], [], [(0, 21), (7, 37)]]
T2 = ["Łysy", "Brun", "Blond", "Brun", "Blond", "Blond", "Brun", "Brun", "Blond", "Brun", "Brun", "Blond"]
W2 = 63
odp2 = [0, 11, 7, 5]

print(babiarz(G1, T1, W1) == odp1)
print(babiarz(G2, T2, W2) == odp2)
