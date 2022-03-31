'''Dany jest spójny graf nieskierowany G = (V,E). Proszę
zaproponować algorytm, który znajdzie taką kolejność usuwania
wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie
przestaje być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie
dotykające go krawędzie).'''


# idea - raz włączamy DFS, za każdym razem gdy przetworzymy dany wierzchołek dodajemy go do listy usuniętych wierzchołków.

# Dlaczego to działa ?
# Jesli przetworzylismt dany wierzchołek oznacza to, że już wczesniej odwiedzilismy wszystkich jego sąsiadów, a jesli to zrobilismy to znaczy,
# ze można dojsć do nich w inny sposób niż przez rozważany wierzchołek. Zatem jesli usuniemy jego i krawędzie z niego wychodzące, nadal zachowamy spójność grafu

def stil_connected_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]
    del_list = []

    def DFS_visit(G,s):
        nonlocal del_list
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        del_list += [s]
        return

    DFS_visit(G,0)
    #ystarczy jedno odpalenie bo graf jest spójny

    return del_list


test = [[1,2],[0,6],[0,3,5,6],[2,4],[3,5],[2,4,6,7],[1,2,5],[5,8],[7,9,10],[8,10],[8,9,11],[10]]
print(stil_connected_DFS(test))