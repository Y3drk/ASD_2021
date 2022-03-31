'''W Krakowie w godzinach szczytu są korki, dlatego kierowcom bardziej zależy na czasie niż na realnej odległości między dwoma punktami.
Mamy mapę Krakowa, między skrzyżowaniami na ulicach są zaznaczone odległości i czasy przejazdu. W Krakowie (jak wszyscy wiemy ;) ) są ulice jedno- i dwukierunkowe.
Kierowcy potrzebują aplikacji, która pomoże im znajdować drogi, które pozwalają dotrzeć ze skrzyżowania A do B w jak najkrótszym czasie,
a spośród tych o najmniejszym czasie wybiera i zwraca najkrótszą pod względem odległości.
Mamy przetworzyć Q zapytań w postaci (skrzyżowanieA, skrzyżowanieB) i na każde z nich odpowiedzieć parą (czas, dystans) najlepszej drogi.
Wszystkie zapytania odnoszą się do tego samego grafu.
Jakie rozwiązanie daje najlepszą klasę złożoności w każdym z poniższych przypadków?
Q = O(1), E = O(V) - Dijkstra
Q = O(1), E = O(V^2) - Dijkstra
Q = O(V), E = O(V) - Dijkstra
Q = O(V), E = O(V^2) - Floyd-Warshall
'''

#idea - zmieniamy relaksacje aby dla takich samych czasów wybierało sciezke krótsza.
# W zależności od gestosci grafu oraz ilosci zapytan uzywamy algorytmu dijkstry lub Floyda Warshalla

#zrobimy sb tylko disjkstre
#zał. graf reprezentujemy jako liste sasiedztwa

def traffic_jams_in_Cracow(G, s):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = [float('inf') for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    Q.put((0,0,s))  # (czas,odległosc, wierzchołek)
    distance[s] = 0
    time[s] = 0

    def relax(u, v, edge_time, edge_distance):
        if time[v] > time[u] + edge_time:
            time[v] = time[u] + edge_time
            distance[v] = distance[u] + edge_distance
            parent[v] = u
            return True

        elif time[v] == time[u] + edge_time and distance[v] > distance[u] + edge_distance:
            time[v] = time[u] + edge_time
            distance[v] = distance[u] + edge_distance
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,_,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax(t,u[0],u[1],u[2]):
                        Q.put((time[u[0]],distance[u[0]],u[0]))

    return parent,distance,time

#               0              1             2                     3                           4                     5
test = [[(1,10,2),(4,7,3)],[(2,1,10)],[(1,1,10),(4,2,5)],[(2,3,4),(4,10,2),(5,5,4)],[(0,7,3),(2,2,5),(3,10,2)],[(0,5,3),(4,6,3)]]
res = traffic_jams_in_Cracow(test,1)
print(res[0])
print(res[1])
print(res[2])