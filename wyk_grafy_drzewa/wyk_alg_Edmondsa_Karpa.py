def get_path(P,ind):
    tmp = []
    while ind != None:
        tmp.append(ind)
        ind = P[ind]

    return tmp


def BFS(G,s,t):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = Queue()
    narrow_throat = float('inf')

    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                visited[v] = True
                if G[u][v] < narrow_throat:
                    narrow_throat = G[u][v]
                parent[v] = u
                if v == t:
                    return parent, narrow_throat
                else:
                    Q.put(v)

    return parent, narrow_throat


def EK(G,s,t):
    flow = 0
    while True:
        P,f = BFS(G,s,t)
        #print(P,f)
        if P[t] == None:
            break

        #print(f)
        flow += f
        tmp = get_path(P,t)
        for i in range(1,len(tmp)):
            G[tmp[i-1]][tmp[i]] += f
            G[tmp[i]][tmp[i-1]] -= f

    return flow



#graf reprezentujemy macierzowo, niszczymy go w trakcie obliczania
#PRZETESTOWAC

G = [[0, 0, 5, 0, 0, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 4, 2, 0, 0, 0, 0, 0],
[0, 1, 4, 0, 1, 0, 2, 0, 0, 0],
[0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
[0, 2, 0, 0, 0, 0, 0, 5, 3, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(EK(G,0,9))

G1 = [[0,4,0,3,0,0],
     [0,0,2,2,0,0],
     [0,0,0,0,0,4],
     [0,0,2,0,2,0],
     [0,0,0,0,0,5],
     [0,0,0,0,0,0]]
print(EK(G1,0,5))

G2 = [[0, 3, 4, 0, 0, 0],
     [0, 0, 0, 2, 2, 0],
     [0, 2, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 0, 0]]
s2 = 0
t2 = 5
odp2 = 6
print(EK(G2,s2,t2))

G3 = [[0, 0, 0, 0, 2, 0, 7],
     [0, 0, 0, 2, 3, 0, 0],
     [2, 0, 0, 0, 0, 3, 0],
     [0, 0, 0, 0, 4, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 0],
     [0, 4, 5, 0, 0, 0, 0]]

s3 = 0
t3 = 4
odp3 = 8
print(EK(G3,s3,t3))