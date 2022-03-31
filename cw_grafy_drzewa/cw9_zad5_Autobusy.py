'''Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów.
Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
(najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
dostali się z A do B.
'''


#idea - 1) trójki zmieniamy na graf
# 2) odpalamy dijkstra z kopcem maximum w ramach priority queue,
# 3) trase mamy z parentów, a ilosc grupek to K // finalna wartosc z tablicy size jesli K%size[y] == 0 lub (K // size) + 1 wpp


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2


def heapify_max(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l][0] > T[m][0]:
        m = l
    if r < n and T[r][0] > T[m][0]:
        m = r

    if m != i:
        T[i],T[m] = T[m], T[i]
        heapify_max(T,n,m)


def reverse_heapify_max(T, i):
    p = parent(i)
    m = i
    if p >= 0 and T[p][0] < T[i][0]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_max(T,m)


def insert_to_heap_max(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_max(T,n-1)


def print_path(p,ind):
    if p[ind] != None:
        print_path(p,p[ind])

    print(ind,end=' ')


def Tourists_problem(G, s):
    n = len(G)
    Q = []
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    size = [0 for _ in range(n)]

    Q.append((0,s))  # (waga, wierzchołek)
    size[s] = float('inf')

    def relax_flow(u, v, edge):
        if size[v] < min(size[u],edge):
            size[v] = min(size[u],edge)
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while len(Q) > 0:
        _,t = Q[0]
        Q[0], Q[len(Q)-1] = Q[len(Q)-1], Q[0]
        Q = Q[:len(Q)-1]
        heapify_max(Q,len(Q),0)

        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax_flow(t,u[0],u[1]):
                        insert_to_heap_max(Q,(size[u[0]],u[0]))

    return parent,size


#             0             1                     2                   3                     4            5
test = [[(1,5),(2,10)],[(0,5),(2,2),(4,7)],[(0,10),(1,2),(3,5)],[(2,5),(4,3),(5,10)], [(3,4),(5,3)],[(3,10),(4,3)]]
K = 12
stop = 5


res = Tourists_problem(test,0)
#print(res[0],res[1])
if (K % res[1][stop] == 0):
    print(K // res[1][stop])
else:
    print((K // res[1][stop]) + 1)

print_path(res[0],stop)
