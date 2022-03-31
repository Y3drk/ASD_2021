# dotyczy grafu skierowanego
# def : mowimy, że wierzchołki należa do tej samej spojnej składowej, jesli istnieja sciezki skierowane z u do v oraz z v do u w grafie G

# algorytm znajduje takie sss

# działanie :
# 1) wykonujemy DFS zapisujac w wierzchołkach czas ich przetworzenia
# 2) odwracamy kolejnosc krawedzi
# 3) wykonujemy DFS w kolejnosci malejacych czasów przetworzenia


def strongly_connected_integrants_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    process_times = [0 for _ in range(n)]
    SSS = [-1 for _ in range(n)]
    time = 0
    counter = 0

    def DFS_visit(G,s):
        nonlocal time, process_times,counter
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                SSS[u] = counter
                DFS_visit(G,u)

        time += 1
        process_times[s] = time
        SSS[s] = counter
        return

    for u in range(n):    #(1)
        if not visited[u]:
            DFS_visit(G,u)

    print(process_times)
    turned_edges = turn_edges(G)  #stworzymy aleternatywna reprezentacje #(2)
    order = []
    for i in range(n):
        visited[i] = False
        order += [[process_times[i],i]]

    order.sort()
    print(order)
    for u in range(n-1,-1,-1):    #(3)
        if not visited[order[u][1]]:
            counter += 1
            #print("Odpalamay dla wierzchołka:",o)
            DFS_visit(turned_edges,order[u][1])

    return SSS


def turn_edges(G):   # O(V + E)
    n = len(G)
    Turned = [[] for i in range(n)]
    for v1 in range(n):
        for v2 in range(len(G[v1])):
            Turned[G[v1][v2]] += [v1]

    return Turned



#         a=0   b=1  c=2  d=3 e=4 f=5   g=6 h=7 i=8   j=9 k=10
test = [[1,4],[2,3],[0,7],[4],[5],[3,6],[3],[9],[6,7],[10],[8]]
print(strongly_connected_integrants_DFS(test))
