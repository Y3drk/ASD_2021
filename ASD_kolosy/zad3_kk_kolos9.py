from zad3_testy_kk_kolos9 import run_tests

def gorszy_mag(G) -> list:
    """miejsce na Twoją implementację!"""

    # idea -
    # A) ustaw mincost (koszt najtańszego cyklu) na nieskończoność,
    # zainicjuj pustą tablice C_parent, która w kroku (C), będzie słuzyła do wypisania znalezionego minimalnego cyklu
    # oraz pusta tablice best_edge, która zapamięta odpowiednią krawędź {u,v}
    # B) dla kazdej krawedzi wykonaj:
    # 1) "usuń krawędź" grafu {u,v}
    # 2) za pomocą algorytmu Dijkstry znajdź najkrótsza scieżkę z u do v nie uzywając ww. krawedzi jesli takowa istnieje
    # 3) jesli ww. scieżka istnieje sprawdź czy cykl skaładający się z tej ściezki + "usunietej" krawedzi jest "tańszy" (suma wag jest mniejsza) od przechowywanego minimalnego cyklu
    # jesli tak to dokonaj podmiany pól mincost, C_parent, best_edge
    # C) po przeanalizowaniu wszystkich krawędzi, na podstawie tablicy C_parent wypisz znaleziony cykl

    # złożoność -> pamięciowa O(V) - na tablice C_parent oraz tablice pomocnicze używane wewnętrznie w alg. Dijkstry + O(1) na pozostałe zmienne tj. mincost. Pamięć zużyta na reprezentacje wejscia pomijam, gdyż jest narzucona z zał.
    # -> czasowa - O(E*V^2) - ponieważ dla każdej krawędzi włączamy alg. Dijkstry, który w implementacji dla macierzowej repr. grafu ma zł. O(V^2)

    def Dijkstra_4_adjmatrix(G,
                             s):  # z zastosowaniem tablicy jako kolejki dla macierzy sasiedztwa. Wg Cormena O(V^2 + E) ~= O(V^2)
        n = len(G)
        Queue = [float('inf') for _ in range(n)]
        processed = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        distance = [float('inf') for _ in
                    range(n)]  # niepotrzebne bo queue ~= distance de facto, ale zachowamy dla porzadku

        Queue[s] = 0
        distance[s] = 0

        def relax(u, v, edge):
            if distance[v] > distance[u] + edge:
                distance[v] = distance[u] + edge
                parent[v] = u
                return True  # przyda sie do wkładania wierzchołków do kolejki

            return False

        def get_vert():  # wyciagnięcie wierzchołka z kolejki O(V)
            n = len(Queue)
            key = n
            best = float('inf')
            for i in range(n):
                if not processed[i] and best > Queue[i]:
                    best = Queue[i]
                    key = i

            return key, best

        while True:
            v, flag = get_vert()
            if flag == float('inf'):  # warunek zakonczenia przetwarzania
                break

            else:
                processed[v] = True
                for u in range(n):
                    if G[v][u] != 0 and not processed[u] and relax(v, u, G[v][u]):
                        Queue[u] = distance[u]

        return parent, distance

    def get_cycle(Parents, beg, end):
        Cycle = [end]

        while end != beg:
            Cycle += [Parents[end]]
            end = Parents[end]

        return Cycle

    n = len(G)
    mincost = float('inf')
    C_parent = []
    curr_edge = None
    best_edge = []

    for u in range(n):
        for v in range(u + 1,n):  # aby nie analizować jednej krawędzi 2 razy, gdyż z zał. wynika, że graf jest nieskierowany
            if G[u][v] != 0:
                curr_edge = G[u][v]
                G[u][v] = 0  # "usuwanie krawędzi" (ofc potem ją przywrócimy *, stąd "")

                potential_C_p, distances = Dijkstra_4_adjmatrix(G, u)

                if distances[v] + curr_edge < mincost:
                    mincost = distances[v] + curr_edge
                    C_parent = potential_C_p
                    best_edge = [u, v]

                G[u][v] = curr_edge  # (*)

    if len(C_parent) > 0:
        print(mincost)
        print(get_cycle(C_parent, best_edge[0], best_edge[1]))
        return get_cycle(C_parent, best_edge[0], best_edge[1])

    else:
        return []
# tu umieść swoją implementację
pass

run_tests(gorszy_mag)
