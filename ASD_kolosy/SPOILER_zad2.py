from zad2testy import runtests

# idea - uzywamy pewnej modyfikacji BFS, z tym że liczymy koszt każdej ściezki osobno oraz używamy "sztucznych wierzchołków", aby uwzględnić wagę krawędzi
# startujemy BFS z kazdego wierzchołka, ktorego litera zaczyna dany wyraz i jesli po przejsciu odp liczby wierzchołków osiagniemy ostatnią litere słowa, to
# sprawdzamy czy suma wag krawedzi po których przeszła sciezka jest najmnijeszym dotychczasowym wynikiem

# złożonośc moze mocno odwalić przez te sztuczne wierzchołki ktore podbijaja BFS (ale polecenie nie każe jej szacowac XD)
# pamieciowa -> O(n^2 + n) + obsługa kolejki(naraz maksymalnie n-1 wierzchołków -> O(4n-4) ~= O(n^2)
# czasowa -> O(km(V+E)) gdzie k to liczba wierzchołków startowych, a m to srednia waga krawedzi (tak mniej wiecej bo jestem głąbem i nie umiem dokładniej)
# moze to V + E da sie jakos ograniczyc przez liczbe liter w słowie, ale nie sądzę
#(błagam 0.5 pkt za starania :))

def let( ch ): return ord(ch) - ord("a")

def letters( G, W ):
    # tu prosze wpisac swoje rozwiazanie
    n = len(G[0])
    L = G[0]
    E = list_of_edges_to_adj_arr(G[1],n)
    from queue import Queue
    best = float('inf')
    starters = []
    for i in range(n):
        if G[0][i] == W[0]:
            starters += [i]

    for j in starters:
        Q = Queue()
        Q.put((j, 1, 0,-1))

        while not Q.empty():
            u, ucost, upos, total = Q.get()
            total += 1
            ucost -= 1

            if ucost > 0:
                Q.put((u, ucost, upos, total))

            else:
                if upos == len(W) - 1 and W[upos] == G[0][u]:
                    if best > total:
                        best = total

                    break

                upos += 1
                for v in range(n):
                    if L[v] == W[upos] and E[u][v] != 0:
                        Q.put((v, E[u][v], upos, total))

    return best
    

def list_of_edges_to_adj_arr(E,n):   # O(E)
    A = [[0]*n for _ in range(n)]
    for i in range(len(E)):
        A[E[i][0]][E[i][1]] = E[i][2]
        A[E[i][1]][E[i][0]] = E[i][2]

    return A

runtests( letters )
    
    
