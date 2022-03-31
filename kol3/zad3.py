#Jędrzej Ziebura

# A) Włączamy na zadanym grafie algorytm Floyda-Warshalla O(V^3)
# B) Znając wszystkie najkrótsze ścieżki, sprawdzamy ile jest wierzchołków, dla których istnieja scięzki spełniające warunki 1 i 2 O(V^2)
# C) Tworzymy nową macierz reprezentujaca graf dwudzielny (pary B, G -> kazda nalezy do innego zbioru)... Jesli dana para wierzchołków została wybrana w podpunkcie
# B to wpisujemy w macierzy miedzy nimi krawędź o wadze 1
# D) dodajemy superźródło SS, w które łaczymy z wierzchołkami B i superujście SU, z kolei połączone z wierzchołkami G.
# Wagi krawedzi łączących SU i SS z grafem ustalamy jako 1.
# Na tak powstałej macierzy właczamy algorytm Edmonds-Karpa, który znajdzie ilość skojarzeń w tak zadanym grafie, a to znowu jest nasza odpowiedź,
# bo kazdy wierzchołek może być tylko w jednej parze, czyli sprawdzamy  w ten sposób warunek 3.

# złożoność:
# pamieciowa -> macierz reprezentująca nowy graf = O(V^2)
# czasowa -> wszystko "przykrywa" alg. Edmondsa-Karpa O(VE^2), bez niego pesymistyczną złożonośc wyznaczałby alg. Floyda-Warshalla O(V^3)


#dodatkowo, w alg FW mozemy zrezygnowac z weryfikacji bo mamy założenie o dodatniej wadze krawedzi
#zakładam, ze możemy zniszczyć wejsciową macierz. Mozna oczywiscie tego uniknąc tworząc jej kopię w czasie O(V^2)

from zad3testy import runtests
from zad3EK    import edmonds_karp


def FW(G):
    n = len(G)

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if G[u][v] > G[u][t] + G[t][v]:
                    G[u][v] = G[u][t] + G[t][v]

    return G


def BlueAndGreen(T, K, D):
    n = len(T)

    #przerobienie T na potrzeby mojej implementacji FW
    for i in range(n):
        for j in range(n):
            if i != j and T[i][j] == 0:
                T[i][j] = float('inf')
                T[j][i] = float('inf')

    FW(T)  #(A)

    New = [[0]*(n+2) for _ in range(n+2)] #nowa macierz, ostatnie dwa wiersze to odp SS i SU

    for v in range(n):
        for u in range(n):
            if T[v][u] >= D and ((K[v] == 'G' and K[u] == 'B') or (K[v] == 'B' and K[u] == 'G')): #(B)
                New[v][u] = 1


    #(C)
    SS = n
    SU = n + 1
    for v in range(n):
        if K[v] == 'B':
            New[SS][v] = 1

        if K[v] == 'G':
            New[v][SU] = 1

    flow = edmonds_karp(New,SS,SU) #(D)
    # tu prosze wpisac wlasna implementacje
    return flow

runtests( BlueAndGreen ) 
