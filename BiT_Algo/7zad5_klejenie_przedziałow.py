'''Dany jest ciąg przedziałów postaci [a, b]. dwa przedziały można skleic wtw. , gdy mamaj dokładnie jeden punkt wspólny.
Napisz algorytm, który sprawdza czy da sie uzyskac przedział [x,y] poprzez klejenie przedziałow. '''

# lista przedziałow to de facto lista skierowanych krawdzie grafu, wybieramy dowolny algorytm przeszukujacy graf
# i sprawdzamy czy z punktu x da sie dotrzec do pkt y


def transform_to_adjacency_list_directed(T,n):
    G = [[]*n for _ in range(n)]

    for i in range(len(T)): #przepisanie do listy sasiedztwa O(n)
        G[T[i][0]] += [T[i][1]]

    return G


def can_glue_intervals_BFS(G,start,stop):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = Queue()

    Q.put(start)
    visited[start] = True

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                if v == stop:
                    return True
                else:
                    visited[v] = True
                    parent[v] = u
                    Q.put(v)

    return False



test = [[1,3],[2,3],[4,5],[5,7],[0,6],[6,7],[0,2],[3,4]]
maxi = -1


for i in range(len(test)):
    maxi = max(maxi, test[i][1])


Graph = transform_to_adjacency_list_directed(test,maxi + 1)
start = 0
stop = 7

#print(Graph)
print(can_glue_intervals_BFS(Graph,start,stop))




