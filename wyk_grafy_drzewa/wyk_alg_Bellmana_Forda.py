# zał. graf skierowany reprezentujemy jako liste sąsiedztwa

def BF_4_adjlist(G,s):
    n = len(G)
    #inicjalizacja
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    #relaksacje
    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u

    for i in range(n - 1):
        for u in range(n):
            for v,edge in G[u]:    #te dwie  petle to przejscie po wszystkich krawedziach
                relax(u,v,edge)

    # weryfikacja

    for u in range(n):
        for v,w in G[u]:
            if distance[v] > distance[u] + w:
                return False, None, None

    return True, distance, parent


test = [[(1,10),(2,3)],[(6,1),(5,5)],[(4,1)],[(5,8)],[(1,-4),(3,-20)],[(6,16)],[]]
test_pod_wyjebke = [[(1,10),(2,3)],[(6,1),(2,8),(5,5)],[(4,1)],[(5,8)],[(1,-88),(3,-20)],[(6,16)],[]]
res = BF_4_adjlist(test,0)
if res[0]:
    print(res[1],"\n",res[2])
else:
    print(res[0])
