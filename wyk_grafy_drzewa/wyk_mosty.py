# def. mostem nazywamy krawedz w grafie spojnym nieskierowanym, której usuniecie rozspójnia graf
# TW. krawedz e jest mostem wtw. gdy nie leży na żadnym cyklu prostym
#def. cykl prosty - droga zamknieta, czyli żaden wierzchołek poza pierwszym/ostatnim nie wystepuje w cyklu dwa razy

#Algorytm działania:
# (1) i (2) dzieją sie jednoczesnie
# (1) Wykonaj DFS i dla każdego wierzchołka v nalezacego do  V zapisuj czas odwiedzenia d(v)
# (2) dla kazdego wierzchołka obliczamy low(v) = min{ d(v), min d(u) (jesli sa krawedzie wsteczne), min low(w) gdzie w jest dzieckiem v w drzewie DFS) }
# (3) mosty to krawedzie {v, p(v)}, gdzie d(v) = low(v)

def bridges_in_G_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visit_time = [float('inf') for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    bridges = []
    time = 0


    def DFS_visit(G, s):
        nonlocal time, visit_time, low, bridges
        time += 1
        visit_time[s] = time
        low[s] = time
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G, u)

            if visited[u] and parent[s] != u:   #krawedz wsteczna -> prowadzi do odwiedzonego wierzchołka, ale jest nieużyta
                low[s] = min(low[s],low[u])

        for w in G[s]:    #funkcja low dla dzieci s w drzewie DFS
            if parent[w] == s:
                low[s] = min(low[s],low[w])

        if visit_time[s] == low[s] and parent[s] != None:   #sprawdzenie czy mamy most
            bridges += [[s,parent[s]]]
        return

    DFS_visit(G, 0)   # graf jest spojny wystarczy DFS odpalić raz

    return bridges


#        a=0   b=1      c=2     d=3       e=4     f=5    g=6   h=7
test = [[1,4], [0,2], [1,3,4], [3,5,6], [0,2,7], [3,6], [3,5], [4]]
print("Mosty w grafie testowym to:",bridges_in_G_DFS(test))



