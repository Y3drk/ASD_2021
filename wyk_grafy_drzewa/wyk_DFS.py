#wykładowa implementacja algorytmu DFS
# założenie : graf reprezentujemy jak listę sasiedztwa, a konkretnie jako liste list, parametry parent i visited sa realizowane jako osobne tablice, gdzie indeks
# jest identyfikatorem wierzchołka


def DFS(G): #w wiekszosci implementacji nie wskazujemy konkretnego wierzchołka od którego zaczynamy
    n = len(G)
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]

    time = 0 #umowny/wirtualny czas, potrzebny nie tyle w samym DFS co w jego licznych zastosowaniach

    def DFS_visit(G,s):
        nonlocal time
        time += 1
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        time += 1
        return

    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return visited,parent

# implementacja z uzyciem stosu
# złozonosc O(V+E) - źródło - geeks for geeks

def DFS_stack(G,s):  #????
    n = len(G)
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]
    Stack = []

    Stack.append(s)
    visited[s] = True

    while len(Stack) != 0:
        #print("Aktualny stos:",Stack)
        u = Stack.pop()
        #print("Wychodzimy z:",u)
        for v in G[u]:
            #print("sprawdzamy:",v)
            if not visited[v]:
                #print("przechodzimy przez:",v)
                visited[v] = True
                parent[v] = u
                Stack.append(v)

    return visited,parent


G = [[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]
result = DFS(G)
print("Done DFS wykładowy")
print("Visited:",result[0])
print("Parents:",result[1])
print("----")
result1 = DFS_stack(G,0)
print("Done DFS ze stosem")
print("Visited:",result1[0])
print("Parents:",result1[1])
print("----")
'''
G1 = [[1,2,3],[0,2,4],[0,1],[0],[1]]
result2 = DFS_stack(G1,0)
print("Done DFS ze stosem")
print("Visited:",result2[0])
print("Parents:",result2[1])'''

