from copy import deepcopy


def max_extending_path(G, s, t):
    """miejsce na Twoją implementację!"""

    # 1) algorytm jest modyfikacja algorytmu Dijkstry
    #   a) używamy kopca maximum jako priority queue
    #   b) zamiast tablicy distance uzywamy flow, która oznacza maksymalną przepustowosc z jaką mozemy dotrzec od s do danego wierzchołka
    #       wartoscia flow kazdego wierzchołka jest min{flow[parent[v]],(parent[v],v)}
    #   c) modyfikujemy relaksacje tak aby, poprawnie uaktualniała wartosc flow (wybierała najwiekszą mozliwa opcje)

    # złożoność - czasowa -> taka sama jak algorytmu Dijkstry O(ElogV),
    # pamieciowa -> O(E) maksymalny koszt pamieciowy obsługi kolejki + koszt przechowywania reprezentacji grafu o(V+E)

    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def parent(i):
        return (i - 1) // 2

    def heapify_max(T, n, i):
        l = left(i)
        r = right(i)
        m = i
        if l < n and T[l][0] > T[m][0]:
            m = l
        if r < n and T[r][0] > T[m][0]:
            m = r

        if m != i:
            T[i], T[m] = T[m], T[i]
            heapify_max(T, n, m)

    def reverse_heapify_max(T, i):
        p = parent(i)
        m = i
        if p >= 0 and T[p][0] < T[i][0]:
            m = p

        if m != i:
            T[m], T[i] = T[i], T[m]
            reverse_heapify_max(T, m)

    def insert_to_heap_max(T, el):
        T += [el]
        n = len(T)
        reverse_heapify_max(T, n - 1)

    def get_path(p, ind):
        tmp = []
        while p[ind] != None:
            tmp.append(ind)
            ind = p[ind]

        tmp.append(ind)

        return tmp[::-1]

    def find_path(G, s):
        n = len(G)
        Q = []
        processed = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        flow = [0 for _ in range(n)]

        Q.append((0, s))  # (waga, wierzchołek)
        flow[s] = float('inf')

        def relax_flow(u, v, edge):
            if flow[v] < min(flow[u], edge):
                flow[v] = min(flow[u], edge)
                parent[v] = u
                return True

            return False

        while len(Q) > 0:
            _, t = Q[0]
            Q[0], Q[len(Q) - 1] = Q[len(Q) - 1], Q[0]
            Q = Q[:len(Q) - 1]
            heapify_max(Q, len(Q), 0)

            if processed[t]:
                continue
            else:
                processed[t] = True
                for u in G[t]:  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                    if not processed[u[0]]:
                        if relax_flow(t, u[0], u[1]):
                            insert_to_heap_max(Q, (flow[u[0]], u[0]))

        return parent, flow

    res = find_path(G, s)

    if res[1][t] != 0:
        tmp = get_path(res[0], t)
        return tmp

    return []


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
s = 0
t = 3
C = 3

GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)

if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)

capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
