'''Wieżowiec ma 100 pięter i n wind, nie ma natomiast schodów. Każda winda posiada listę pięter, do których dojeżdża i prędkość w sekundach na piętro.
Jesteśmy na piętrze i, chcemy się dostać na piętro j. Ile minimalnie sekund musimy spędzić w windach, aby tam dotrzeć?
'''

#idea - dostajemy kazda winde w postaci [(pietra na które dojedza winda), stała predkosc windy w sekundach na pietro]
# przerabiamy otrzymane dane na graf w postaci listy sasiedztwa i odpalamy na nim dijkstre z i


def Lifts_and_levels(G, s):
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
                if not processed[u[0]]:
                    if relax(t,u[0],u[1]):
                        Q.put((distance[u[0]],u[0]))

    return distance


def make_into_adjlist(D, l):
    G = [[] for _ in range(l + 1)] #jesli maks pietro to 8 to tak naprawde jest 8 pieter xdd
    for lift in D:
        for level in range(len(lift[0])-1):
            G[lift[0][level]].append((lift[0][level+1], (lift[0][level+1] - lift[0][level])*lift[1]))
            # zakładamy, że pietra w windach sa ułozone rosnaco
            # dodajemy krawedzie do grafu i nie przejmujemy sie potencjalnymi multikrawedziami, co prawda podbije to zlożoność, ale nie bedzie az tak źle
    return G


def solver(D,i,j,l):
    G = make_into_adjlist(D,l)
    res = Lifts_and_levels(G,i)
    return res[j]


#       0             1          2            3            4
D = [[[0,3,5],2], [[0,3],2], [[1,2,4],3], [[3,5],1], [[0,1,2,3,4,5],5]]
p = 5
i = 0
j = 5
print(solver(D,i,j,p))






