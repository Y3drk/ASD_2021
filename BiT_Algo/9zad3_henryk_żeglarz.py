'''Żeglarz Henryk mieszka na wysepce pewnego archipelagu. Wszystkie wyspy w tym archipelagu są tak małe, że można je reprezentować jako punkty w przestrzeni R2.
Pozycje wszystkich wysp dane są jako ciąg W = ((x1, y1), … , (xn, yn)). Henryk mieszka na wyspie(x1, y1), ale chce się przeprowadzić na wyspę (xn, yn).
Normalnie, każdego dnia może przepłynąć na wyspę znajdującą się w odległości najwyżej Z (w sensie standardowej odległości euklidesowej),
ale może także każdego dnia przepłynąć odległość do 2Z, pod warunkiem, że cały następny dzień będzie odpoczywał.
Henryk musi zawsze nocować na jakiejś wyspie.
Proszę zaproponować wielomianowy algorytm, który oblicza ile minimalnie dni Henryk potrzebuje, żeby dostać się na swoją docelową wyspę
(lub stwierdza, że to niemożliwe).'''

#idea - preprocesujemy punkty na graf, moze byc na postac macierzowa, 0 oznacza brak krawedzi, czyli d((x1,y1),(x2,y2)) > 2Z, 1 to krawedz krótka czyli d((x1,y1),(x2,y2)) <= Z,
# a 2 to krawedz długa czyli  2Z >= d((x1,y1),(x2,y2)) > Z.
#potem odpalamy BFS, z tym że symulujemy wage krawedzi, wstawiajac do kolejki krotki (wierzchołek,licznik) i za kazdym wyciagnieciem z kolejki zmniejszamy licznik
# i przetwarzamy wierzchołek tylko wtedy gdy licznik wyniesie 0.


def preprocess_isles(W,Z):
    from math import sqrt
    n = len(W)
    Graph = [[0]*n for i in range(n)]
    for w1 in range(n):
        for w2 in range(w1 + 1,n):
            if (sqrt((W[w2][0] - W[w1][0])**2 + (W[w2][1] - W[w1][1])**2)) <= Z:
                Graph[w1][w2], Graph[w2][w1] = 1,1
            elif (sqrt((W[w2][0] - W[w1][0])**2 + (W[w2][1] - W[w1][1])**2)) <= 2*Z:
                Graph[w1][w2], Graph[w2][w1] = 2,2
            else:
                Graph[w1][w2], Graph[w2][w1] = 0, 0

    return Graph


def sailing_for_new_home_BFS(G):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    days = [-1 for _ in range(n)]
    Q = Queue()

    Q.put((0,1))
    visited[0] = True

    while not Q.empty():   #tutaj takie zaznaczanie visited działa przez założenia, bo i tak nie damy rade byc w danym miejscu szybciej wiec mozemy od razu zaznaczyc visited i parenta
        u,udays = Q.get() #ale tak dla normalnego wazonego BFS'a tak nie bedzie
        days[u] += 1
        udays -= 1
        #print("Płyniemy do :",u)
        if udays > 0:
            Q.put((u,udays))
        else:
            for v in range(n):
                if not visited[v] and G[u][v] != 0:
                    #print("mozemy dopłynac do:",v)
                    visited[v] = True
                    parent[v] = u
                    days[v] = days[u]
                    Q.put((v,G[u][v]))

    #print(days)
    return days[n-1]

#        0      1    2     3     4      5    6      7     8       9
test = [(1,0),(1,1),(3,1),(7,5),(6,9),(4,2),(2,1),(3,7),(8,8),(18,18)]
Z = 4
G = preprocess_isles(test,Z)
#for row in G:
    #print(row)

print(sailing_for_new_home_BFS(G))


