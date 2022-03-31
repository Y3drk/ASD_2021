'''Napisz algorytm sprawdzajacy czy graf nieskierowany posiada cykl'''

# jak wykrywac cykl : jesli przeszukujac sasiadów danego wierzchołka v znajdziemy taki wierzchołek u, który był odwiedzony wczesniej,
# a nie jest rodzicem v to mamy cykl.


def has_cycle_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]

    def DFS_aux(G,s):
        #print("starter:",s)
        visited[s] = True

        result = False
        for u in G[s]:
            #print("checking:",u)
            if not visited[u]:
                parent[u] = s
                result = DFS_aux(G,u) or result

            elif visited[u] and parent[s] != u: 
                #print("znaleziono cykl na podstawie wierzchołków:",s,u,parent[u])
                return True

        return result

    answer = False
    for u in range(n):
        if not visited[u]:
            #print("wbitka dla u:",u)
            answer = answer or DFS_aux(G,u)
            #print('-----')

    return answer


test = [[1],[0,2],[1,3],[2,4,5],[3,5],[3,4]]
print(has_cycle_DFS(test))

