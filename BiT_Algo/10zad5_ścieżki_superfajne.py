'''Dany jest graf ważony G.
Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo ścieżką między v i u, ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc, szukamy najkrótszych ścieżek w sensie liczby krawędzi wśród najkrótszych ścieżek w sensie wagowym).
Podaj algorytm, który dla danego wierzchołka startowego s znajdzie superfajne ścieżki do pozostałych wierzchołków.'''


# idea - nadupcamy dijkstre tylko w kolejke wrzucamy krotki (waga dojscia do v, ilosc krawedzi do v, v), aby priorytetyzowac sciezki o mniejszej
# ilosci krawedzi w przypadku równych wag


def extra_nice_paths(G, s):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [[float('inf'),float('inf')] for _ in range(n)]

    Q.put((0,0,s))  # (waga, ileosc krawedzi, wierzchołek)
    distance[s][0] = 0
    distance[s][1] = 0

    def relax(u, v, edge):
        if distance[v][0] > distance[u][0] + edge:
            distance[v][0] = distance[u][0] + edge
            distance[v][1] = distance[u][1] + 1
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        elif distance[v][0] == distance[u][1] and distance[v][1] > distance[u][1] + 1:
            distance[v][0] = distance[u][0] + edge
            distance[v][1] = distance[u][1] + 1
            parent[v] = u
            return True


        return False

    while not Q.empty():
        _,_,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax(t,u[0],u[1]):
                        Q.put((distance[u[0]][0],distance[u[0]][1],u[0]))

    return parent,distance

#          0                  1                     2               3                  4                 5
test = [[(1,1),(5,2)],[(0,1),(3,5),(4,2),(5,1)],[(3,2),(5,6)],[(1,5),(2,3),(4,3)],[(1,2),(3,3)],[(0,2),(1,1),(2,6)]]
res = extra_nice_paths(test,0)
print("Parents:",res[0],"distances:",res[1])