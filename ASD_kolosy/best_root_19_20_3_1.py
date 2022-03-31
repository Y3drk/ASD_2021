'''ażdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0,l1, . . . ,ln−1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
mieć postać:
def best_root(L):
...
Przykład. Dla listy sąsiedztwa postaci:
L = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]
funkcja powinna zwrócić wartość 3.'''


# idea - odpalamy bfs z losowego wierzchołka i wynajdujemy najdalszy od niego
# z tego najdalszego odpalamy kolejnego bfsa który daje nam średnice (od poczatku do najdalszego wierzchołka) grafu na którym musi lezec "best root",
# jesli srednica ma nieparzysta ilosc to odp jest srodkowy wierzchołek, wpp musimy jeszcze raz przejsc bfsem od konca srednicy i szukac momentu w którym odległosci
# pokrywaja sie z drugim bfsem


def BFS(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
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

    return distance,parent


def get_diameter(P,ind):
    tmp =[ind]
    while P[ind] != None:
        ind = P[ind]
        tmp.append(ind)

    return tmp


def best_root(L):
    n = len(L)
    d, _ = BFS(L,0)
    ind = 0
    best = 0
    for i in range(n):
        if d[i] > best:
            best = d[i]
            ind = i

    d1, p1 = BFS(L,ind)

    ind = 0
    best = 0
    for i in range(n):
        if d1[i] > best:
            best = d1[i]
            ind = i
            #print(best, ind)

    #print(p1,d1)
    #print(ind)
    diam = get_diameter(p1,ind)
    #print(diam)

    if len(diam) % 2 == 1:
        return diam[len(diam) // 2]

    else:
        return diam[(len(diam) - 1)// 2]


L1 = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]

L2 = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ,7],
[ 4 ],
[5 ]]

print(best_root(L1))
print(best_root(L2))

#chyba jest git 

