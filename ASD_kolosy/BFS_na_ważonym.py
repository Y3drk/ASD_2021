# ma sens tylko dla małych wag (i z góry okreslonej górnej granicy, najlepiej jak najmniejszych)

# implementacja dla repr. listy sasiedztwa ale zmiany sa proste

# opłaca sie w takiej sytuacji bardziej od dijkstry bo masz V^2*stała
def BFS_for_weighted(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put((s, 0, 0, None))              #krokti (wierzchołek, waga pozostała, waga całkowita, krawedzi, skad przyszlismy)

    while not Q.empty():
        u, e, tot, prev = Q.get()
        #print(u, e, tot, prev)
        e -= 1
        if e > 0:
            Q.put((u, e, tot, prev))
        else:
            #print("wbijamy do",u,"z",prev)
            if not visited[u]:
                if u != s:
                    parent[u] = prev
                    distance[u] = distance[prev] + tot
                    visited[u] = True

                elif u == s:
                    distance[u] = 0
                    visited[u] = True

                for v in G[u]:
                    if not visited[v[0]]:
                        Q.put((v[0], v[1], v[1], u))

    return visited,distance,parent


def get_path(P,ind):
    tmp = []
    while ind != None:
        tmp.append(ind)
        ind = P[ind]

    return tmp[::-1]

T0 = [[(1,1),(2,3)],[(0,1),(2,1), (3,6)],[(0,3),(1,1),(3,2),(4,10)],[(1,6),(2,2),(4,1),(5,5)],[(2,10),(3,1),(5,2)],[(3,5),(2,4)]]
s = 0
t = 5
res = BFS_for_weighted(T0,s)
#print(res[0])
print(res[1][t])
#print(res[2])
print(get_path(res[2],t))

print("----")
T1 = [[(1,1),(2,2)],[(4,4)],[(3,1)],[(4,1)],[]]
res1 = BFS_for_weighted(T1,0)
odp1 = [0, 2, 3, 4]
#print(res1[0])
print(res1[1][4])
#print(res1[2])
print(get_path(res1[2],4))

print("----")
T2 = [[[1, 4], [7, 8]], [[0, 4], [2, 8], [7, 11]], [[1, 8], [3, 7], [5, 4], [8, 2]], [[2, 7], [4, 9], [5, 14]], [[3, 9], [5, 10]], [[2, 4], [3, 14], [4, 10], [6, 2]], [[5, 2], [7, 1], [8, 6]], [[0, 8], [1, 11], [6, 1], [8, 7]], [[2, 2], [6, 6], [7, 7]]]
res2 = BFS_for_weighted(T2,0)
#print(res2[0])
print(res2[1][8])
#print(res2[2])
print(get_path(res2[2],8))
odp2 =[0, 1, 2, 8]



