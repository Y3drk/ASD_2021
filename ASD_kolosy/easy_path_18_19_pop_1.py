'''1. Mamy nieskierowany graf G=(V,E) reprezentowany przez listę sąsiadów/ Proszę
zaimplementować funkcję, która otrzyma na wejściu graf G i zwróci długość najdłuższej
“łatwej” ścieżki , gdzie łatwa ścieżka to taka, w której każdy stopień <= 2. Proszę skrótowo
wyjaśnić ideę algorytmu i oszacować złożoność obliczeniową i pamięciową.'''

# oznaczamy wierzchołki o wyzszysch stopniach jakos visited zeby nigdy do nich nie wejsc
# (1) odpalamy BFS'a dla wszystkich wierzchołków stopnia 1 oraz dla wszystkich wierzchołków stopnia 2 sasiadujacych z wierzchołkami stopnia wyzszego
# stad zbieramy najlepszy wynik
# (2) jeszcze raz przejdziemy odpalajac dla pozostałych wierzchołków stopnia drugiego ktore zostałyby w jakims cyklu


def BFS(G,s, Marked):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = Marked
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)           #krok startowy, "wrzucenie kamienia"
    visited[s] = True
    distance[s] = 0

    while not Q.empty():   #"rozchodzenie sie fali"
        u = Q.get()
        for v in G[u]:  #sprawdzamy wszystkich dotychczas nieodwiedzonych sasiadów wierzchołka sciagnietego z kolejki
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    return visited, max(distance)


def DFS(G, s, Marked): #w wiekszosci implementacji nie wskazujemy konkretnego wierzchołka od którego zaczynamy
    n = len(G)
    visited = Marked
    parent = [None for _ in range(n)]

    time = 0

    def DFS_visit(G,s):
        nonlocal time
        time += 1
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        return

    DFS_visit(G,s)
    #print(time)

    return visited,time


def if_somsiad_duzy(T,v):
    for u in T[v]:
        if len(T[u]) > 2:
            return True

    return False


def easy_path(T):
    n = len(T)
    Marked = [False for _ in range(n)]
    best = 0
    for i in range(n):
        if len(T[i]) > 2:
            Marked[i] = True

    #print(Marked)
    for j in range(n): #(1)
        if not Marked[j] and (len(T[j]) == 1 or (len(T[j]) == 2 and if_somsiad_duzy(T,j))):
            Marked, res = BFS(T,j,Marked)
            best = max(best,res)

    #print(Marked)
    for l in range(n): #(2)
        if not Marked[l] and len(T[l]) == 2:
            Marked, res = DFS(T, l, Marked)
            best = max(best, res)

    #print(Marked)
    return best


T1 = [[1], [2, 0, 8, 4], [3, 1], [2], [1], [6], [7, 5], [6, 8], [1, 7]]
print("Git" if easy_path(T1) == 3 else "chuj nie dziala") # 3


T2 = [[1], [2, 0, 9, 12, 13], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6, 12, 13], [9, 7], [10, 8, 1, 12], [11, 9], [10], [7, 9, 1], [1, 7]]
print("Git" if easy_path(T2) == 4 else "chuj nie dziala") # 4

T3 = [[1,6],[0,2],[1,3], [2,4],[3,5],[4,6],[5,0], []]
print(easy_path(T3))