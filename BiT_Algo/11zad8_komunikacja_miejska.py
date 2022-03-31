'''Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana.
Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata.
Od tej kwoty jest jednak odejmowany całkowity koszt poniesiony od początku podróży (jeśli jest ujemny, po prostu nic się nie płaci).
'''

'''Mając dane:
graf połączeń w dowolnej reprezentacji (nieskierowany, ważony)
numery stacji początkowej i docelowej

Oblicz minimalny koszt przejechania tej trasy.
'''

# idea - zapłacimy dokładnie tyle ile kosztuje najdłusza krawedz na danej sciezce
# stad - odpalamy dijkstre tyle ze w kolejce przechowujemy najwieksza wage danej sciezki i wg tego samego kryterium wykonujemy relaksacje


def MPK(G, s,k):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    max_edges = [float('inf') for _ in range(n)]

    Q.put((0,s))  # (waga, wierzchołek)
    max_edges[s] = 0

    def relax_max_edge(u, v, edge):
        if max_edges[v] > max(max_edges[u],edge):
            max_edges[v] = max(max_edges[u],edge)
            parent[v] = u
            return True

        return False

    while not Q.empty():
        _,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax_max_edge(t,u[0],u[1]):
                        Q.put((max_edges[u[0]],u[0]))

    return parent,max_edges[k]


def print_path(p,ind):
    if p[ind] != None:
        print_path(p,p[ind])

    print(ind,end=' ')

test = [[(1,100),(3,120)],[(0,100),(2,110)],[(1,110),(4,70)],[(0,120),(4,150)],[(2,70),(3,150)]]
start = 0
stop = 4
res = MPK(test,start,stop)
print("Sciezka:")
print_path(res[0],stop)
print()
print("Koszt:",res[1])