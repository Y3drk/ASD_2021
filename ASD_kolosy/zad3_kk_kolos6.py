# wyspy z egzaminu z modyfikacja, ze na potencjalna destynacje wpływa także kierunek uniwersytecki z którego przyszlismy

# trik polega na tym, ze w pierwszym kroku jesli da sie pojsc na oba kierunki to powinnismy to zrobic. Potem nasza uczelniana przygoda jest juz podporzadkowana naszej
# przeszłosci

# moznaby zoptymalizowac  algorytm implementujac kolejke na tablicy, ale na to jest zbyt ciepło

# z tablica~kolejka złożonosc dijkstrowa tylko V = 3V ze wzgledu na srodki tranportu -> O(ElogV), bez tego jest gorzej

def chodziarz(T, G, A, B):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [[False] * 3 for _ in range(n)]
    parent = [[None] * 3 for _ in range(n)]
    distance = [[float('inf')] * 3 for _ in range(n)]

    if T[A][0]:
        Q.put((0, A, None, 0))  # (waga, wierzchołek,transport, kierunek) # none - start, 5 - most, 7-prom 11-samolot, None - start, 0 - infa, 1 - ceramiczka

    if T[A][1]:
        Q.put((0, A, None, 1))

    distance[A][0] = 0
    distance[A][1] = 0
    distance[A][2] = 0

    def relax(u, v, edge, trans, prev):
        if distance[v][trans] > distance[u][prev] + edge:
            distance[v][trans] = distance[u][prev] + edge
            parent[v][trans] = u
            return True  # przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _, t, m, uni = Q.get()

        if m == 5:
            holder = 0

        elif m == 7:
            holder = 1

        elif m == 11:
            holder = 2

        else:
            holder = None

        if uni == 1:
            uni = 0
        else:
            uni = 1

        if holder == None:
            processed[t][0], processed[t][1], processed[t][2] = True, True, True
            for u in range(n):  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u][0] and G[t][u] != 5 and G[t][u]  != 0 and T[u][uni]:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if G[t][u] == 7:
                        tmp = 1

                    else:
                        tmp = 2

                    if relax(t, u, G[t][u], tmp, 0):
                        Q.put((distance[u][tmp], u, G[t][u], uni))
                        #print("wbitka z:", t, "do:", u, "po:", G[t][u], "a wczesniej smigalismy:", holder, " bedziemy sie uczyc na",uni)

                elif not processed[u][1] and G[t][u] != 7 and G[t][u]  != 0 and T[u][uni]:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if G[t][u] == 5:
                        tmp = 0

                    else:
                        tmp = 2

                    if relax(t, u, G[t][u], tmp, 1):
                        Q.put((distance[u][tmp], u, G[t][u], uni))
                        #print("wbitka z:", t, "do:", u, "po:", G[t][u], "a wczesniej smigalismy:", holder," bedziemy sie uczyc na", uni)

                elif not processed[u][2] and G[t][u] != 11 and G[t][u] != 0 and T[u][uni]:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if G[t][u] == 7:
                        tmp = 1

                    else:
                        tmp = 0

                    if relax(t, u, G[t][u], tmp, 2):
                        Q.put((distance[u][tmp], u, G[t][u], uni))
                        #print("wbitka z:", t, "do:", u, "po:", G[t][u], "a wczesniej smigalismy:", holder,
                             # " bedziemy sie uczyc na", uni)

        elif processed[t][holder]:
            continue

        else:
            processed[t][holder] = True
            for u in range(n):  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u][holder] and G[t][u] != m and G[t][u]  != 0 and T[u][uni]:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy oraz jesli mozna pójsc na inny kierunek niz nasz wczesniejszy
                    if G[t][u] == 5:
                        tmp = 0

                    elif G[t][u] == 7:
                        tmp = 1

                    else:
                        tmp = 2

                    if relax(t, u, G[t][u], tmp, holder):
                        Q.put((distance[u][tmp], u, G[t][u], uni))
                        #print("wbitka z:", t, "do:", u, "po:", G[t][u], "a wczesniej smigalismy:", holder,
                             # " bedziemy sie uczyc na", uni)

    '''for row in distance:
        print(row)'''

    best = float('inf')
    for i in range(3):
        if distance[B][i] < best:
            best = distance[B][i]

    if best < float('inf'):
        return best

    else:
        return None


T = [(True, False), (True, True), (False, True), (True, True), (True, False)]
G = [[0, 5, 5, 0, 11],
     [5, 0, 7, 11, 0],
     [5, 7, 0, 7, 5],
     [0, 11, 7, 0, 0],
     [11, 0, 5, 0, 0]]
print(chodziarz(T, G, 0, 4), "?=?", 28)
