'''Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.


Przykład Dla tablicy
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
funkcja islands(G1, 5, 2) powinna zwrócić wartość 13.'''

# idea - wyobrażamy sb to jako rozmanażanie grafu, ale tak implementacyjnie to rozmnazamy sb komórki distance, visited na 3, dla kazdego rodzaju
# transportu oraz wrzucamy do kolejki krotki (waga drogi, wierzchołek, transport) i bedziemy relaksowac tylko to pole distance z tym typem transportu
# ktorym wjechalismy i szukac wyjazdu z pozostałymi dwoma typami

#zal. przyjmuje repr. grafu jako liste sasiedztwa


def Islands(G, s,k):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [[False]*3 for _ in range(n)]
    parent = [[None]*3 for _ in range(n)]
    distance = [[float('inf')]*3 for _ in range(n)]



    Q.put((0,s,None))  # (waga, wierzchołek,transport) # none - start, 1 - most, 5-prom 8-samolot
    distance[s][0] = 0
    distance[s][1] = 0
    distance[s][2] = 0

    def relax(u, v, edge, trans, prev):
        if distance[v][trans] > distance[u][prev] + edge:
            distance[v][trans] = distance[u][prev] + edge
            parent[v][trans] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,t, m = Q.get()

        if m == 1:
           holder = 0

        elif m == 5:
            holder = 1

        elif m == 8:
            holder = 2

        else:
            holder = None

        if holder == None:
            processed[t][0], processed[t][1],processed[t][2] = True, True, True
            for u in G[t]:  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]][0] and u[1] != 1:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if u[1] == 5:
                        tmp = 1

                    else:
                        tmp = 2

                    if relax(t, u[0], u[1], tmp, 0):
                        Q.put((distance[u[0]][tmp], u[0], u[1]))
                        #print("wbitka z:", t, "do:", u[0], "po:", u[1], "a wczesniej smigalismy:", holder)

                elif not processed[u[0]][1] and u[1] != 5:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if u[1] == 1:
                        tmp = 0

                    else:
                        tmp = 2

                    if relax(t, u[0], u[1], tmp, 1):
                        Q.put((distance[u[0]][tmp], u[0], u[1]))
                        #print("wbitka z:", t, "do:", u[0], "po:", u[1], "a wczesniej smigalismy:", holder)

                elif not processed[u[0]][2] and u[1] != 8:  # jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if u[1] == 5:
                        tmp = 1

                    else:
                        tmp = 0

                    if relax(t, u[0], u[1], tmp, 2):
                        Q.put((distance[u[0]][tmp], u[0], u[1]))
                        #print("wbitka z:", t, "do:", u[0], "po:", u[1], "a wczesniej smigalismy:", holder)

        elif processed[t][holder]:
            continue

        else:
            processed[t][holder] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]][holder] and u[1] != m: #jesli transport wyjeżdżający jest inny niż ten, którym przybylismy
                    if u[1] == 1:
                        tmp = 0

                    elif u[1] == 5:
                        tmp = 1

                    else:
                        tmp = 2

                    if relax(t,u[0],u[1],tmp, holder):
                        Q.put((distance[u[0]][tmp],u[0],u[1]))
                        #print("wbitka z:", t, "do:", u[0], "po:", u[1], "a wczesniej smigalismy:", holder)

    '''for row in distance:
        print(row)'''

    best = float('inf')
    for i in range(3):
        if distance[k][i] < best:
            best = distance[k][i]

    if best < float('inf'):
        return best

    else:
        return None

#             0                  1                  2                      3                          4                   5                 6
test = [[(1,5),(2,1),(3,8)],[(0,5),(3,1),(5,8)],[(0,1),(3,8),(6,8)],[(0,8),(1,1),(2,8),(4,5),(6,1)],[(3,5),(5,1)],[(1,8),(4,1),(6,5)],[(2,8),(3,1),(5,5)]]
print(Islands(test,5,2))



#chyba działa.... WIECEJ TESTOW