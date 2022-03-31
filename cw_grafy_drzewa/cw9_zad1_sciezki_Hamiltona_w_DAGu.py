#ORGANIZACYNIE - zad4. to dijkstra tylko wagi krawedzi logarytmujemy, a zad7. mam zaklepane bicie

'''Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym.
Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
grafie skierowanym.
'''

#idea - sortujemy topologicznie wierzchołki. Wiemy, że do kazdego wierzchołka chcemy wejsc raz, a nie cofniemy się ani razu, bo to top sort.
# siłą rzeczy musimy iść do przodu, takze musimy ruszac sie o 1


def Sort(G):  # Topologiczny sort na macierzy sąsiedztwa
    def DFSVisit(G, n, v):
        nonlocal visited, res

        visited[v] = True
        for i in range(n):
            if not visited[i] and G[v][i] == 1:
                DFSVisit(G, n, i)

        res.append(v)

    n = len(G)
    visited = [False] * n
    res = []
    for v in range(n):
        if not visited[v]:
            DFSVisit(G, n, v)

    res.reverse()

    return res


def HamiltonPathInDag(G):
    TopSort = Sort(G)
    for i in range(len(G) - 1):
        a, b = TopSort[i], TopSort[i + 1]
        if G[a][b] == 0: return False

    print(TopSort)
    return True


G = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]