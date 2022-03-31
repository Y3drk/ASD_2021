'''Pewien znany profesor zaprosił Cię na spotkanie w Magicznym Mieście.
W mieście tym niektóre drogi mogą być uczęszczane tylko przez ludzi poniżej 30 roku życia (w tym Ciebie),
inne tylko przez ludzi w wieku od 30 lat (w tym profesora). Są też drogi, które mogą być uczęszczane przez każdego.
Każda z dróg ma określoną długość, wyrażoną dodatnią liczbą naturalną, może być jedno- lub dwukierunkowa.
Drogi te łączą możliwe lokalizacje spotkania. Wśród nich wyróżniamy mieszkanie Twoje i mieszkanie profesora.
Profesor prosi Cię, byś wybrał takie miejsce na spotkanie, aby łączna droga, którą musicie pokonać Ty i profesor była jak najmniejsza.
Jeżeli jest więcej niż jedno takie miejsce, podaj je wszystkie. Jeżeli takie miejsce nie istnieje, algorytm również powinien to stwierdzić.
'''

#idea - odpalamy dijkstre z mieszkania naszego i profesora ignorujac odpowiednie sciezki, nastepnie sumujemy dystanse i szukamy najmniejszej sumy
# jesli min suma to inf to taka sciezka nie isntieje

#graf reprezentujemy jako liste sasiedztwa, sciezki ogolne oznaczamy 0, dla młodych 1, dla straszych 2

def Dijkstra_ignoring(G, s, ignore):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    Q.put((0,s))  # (waga, wierzchołek)
    distance[s] = 0

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]] and u[2] != ignore:
                    if relax(t,u[0],u[1]):
                        Q.put((distance[u[0]],u[0]))

    return distance


def meet_the_professor(G,m,p):
    d1, d2 = Dijkstra_ignoring(G,m,2), Dijkstra_ignoring(G,p,1)
    res = [0 for _ in range(len(d1))]
    for i in range(len(res)):
        res[i] = d1[i] + d2[i]

    mini = float('inf')
    for j in range(len(res)):
        mini= min(mini,res[j])

    if mini == float('inf'):
        print("Nie istnieje sciezka umozliwiajaca spotkanie")
        return False

    else:
        ODP = []
        for k in range(len(res)):
            if res[k] == mini:
                ODP.append(k)

        return ODP

#        0                                   1              2                  3                     4                           5               6                         7
test = [[(1,5,1),(2,5,1),(3,5,1)],[(0,5,1),(4,2,2)],[(0,5,1),(4,10,0)],[(0,5,1),(6,10,0)],[(1,2,2),(2,10,0),(7,15,2)],[(6,5,1),(6,9,2),(7,2,2)],[(3,10,0),(5,9,2),(5,5,1)],[(5,2,2),(4,15,2)]]
print(meet_the_professor(test,0,7))