'''W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają mieszkańcy.
struct Vertex {
bool shop; // true-sklep, false-dom
int* distances; // tablica odległości do innych wierzchołków
int* edges; // numery wierzchołków opisanych w distances
int edge; // rozmiar tablicy distances (i edges)
int d_store; // odległość do najbliższego sklepu
};
Zaimplementować funkcję distanceToClosestStore (int n, Vertex* village) uzupełniającą d_store dla tablicy Vertexów i oszacować złożoność algorytmu.
'''

#idea - odpalamy dijkstre wrzucajac wszystkie sklepy do kolejki z waga zero (*)
# troche przemodelujemy ta strukture, osobno bedziemy trzymac tablice shop, graf bedziemy reprezentowac jako liste sasiedztwa

# można to sobie wyobrażać tak jakbysmy zrobili ze wszystkich sklepów jeden supersklep i z niego odpalili dijkstre ale taki premoelling
# to troche przerost formy nad trescia


def shops_and_houses(G, shops):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    for i in range(n):   #(*)
        if shops[i]:
            Q.put((0,i))
            distance[i] = 0

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax(t,u[0],u[1]):
                        Q.put((distance[u[0]],u[0]))

    return distance

#             0 -dom         1-dom                      2-dom          3-dom        4-dom              5-dom          6-dom         7-dom         8-sklep             9-sklep       10-sklep     11-sklep
test0 = [[(1,2),(8,8)],[(0,2),(8,11),(10,7),(11,8)],[(9,10),(11,4)],[(11,16)],[(5,4),(7,1),(11,2)],[(4,4),(6,1)],[(5,1),(7,1)], [(4,1),(6,1)],[(0,8),(1,11),(9,5)],[(2,10),(8,5)], [(1,7)],[(1,8),(2,4),(3,16),(4,2)]]
shops0 = [False,False,False,False,False,False,False,False,True,True,True,True]
print(shops_and_houses(test0,shops0))


