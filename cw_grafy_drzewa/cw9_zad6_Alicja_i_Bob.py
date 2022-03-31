'''Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
poprawny).'''


# idea - rozbicie każdego wierzchołka na dwa i kazdej krawędzi na dwie. Przjescie dijkstrą.

# inne - podwójna tablica visited oraz distance dla boba i Alicji.


def Alice_and_Bob(G, s):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [[False, False] for _ in range(n)]
    parent = [[None, None] for _ in range(n)]
    distance = [[float('inf'), float('inf')] for _ in range(n)]
    # dla kazdej tablicy mamy osobne pola dla sytuacji gdy podróz zaczynał Bob i gdy zaczynała Alicja

    Q.put((0, s, 0, 1))  # (waga, wierzchołek, kto zaczął:Bob = 1, czy Alicja = 0, czy dodajemy wartosci tak=1, nie = 0)
    Q.put((0, s, 1, 0))
    distance[s][0] = 0
    distance[s][1] = 0

    def relax(u, v, edge, who, add):
        if add == 1:
            if distance[v][who] > distance[u][who] + edge:
                distance[v][who] = distance[u][who] + edge
                parent[v][who] = u
                return True  # przyda sie do wsadzania wierzchołków do kolejki

        else:
            if distance[v][who] > distance[u][who]:
                distance[v][who] = distance[u][who]
                parent[v][who] = u
                return True

        return False

    while not Q.empty():
        _, t, person, add = Q.get()

        if processed[t][person] == True:
            continue
        else:
            processed[t][person] = True
            for u in G[t]:  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]][person]:
                    if relax(t, u[0], u[1], person, add):
                        if add == 1:
                            Q.put((distance[u[0]][person], u[0], person, 0))
                        else:
                            Q.put((distance[u[0]][person], u[0], person, 1))

    return parent, distance


def print_path_BAs(p, ind, which):
    if p[ind][which] != None:
        print_path_BAs(p, p[ind][which], which)

    print(ind, end=' ')

'''
# TEST1
#              0                           1                        2                         3                       4                    5                 6                    7            8
test = [[(1, 6), (2, 1), (4, 8)], [(0, 6), (2, 5), (3, 4), (5, 7)], [(0, 1), (1, 5), (3, 8), (5, 1)],
        [(1, 4), (2, 8), (4, 1), (7, 8)], [(0, 8), (3, 1), (6, 9)], [(1, 7), (2, 1), (8, 10)], [(4, 9), (7, 5), (8, 3)],
        [(3, 8), (6, 5)], [(5, 10), (6, 3)]]
# res = Alice_and_Bob(test,0)
# end = 8
# print(res[0],"\n",res[1])

# TEST2
test1 = [[(1, 5), (2, 10)], [(0, 5), (2, 2), (4, 7)], [(0, 10), (1, 2), (3, 5)], [(2, 5), (4, 3), (5, 10)],
         [(3, 4), (5, 3)], [(3, 10), (4, 3)]]
end = 5
res = Alice_and_Bob(test1, 0)

if res[1][end][0] <= res[1][end][1]:
    print("Alicja")
    print(res[1][end][0])
    print_path_BAs(res[0], end, 0)
else:
    print("Bob")
    print(res[1][end][1])
    print_path_BAs(res[0], end, 1)

print()
print("-----")


t3 = [[(1, 1)], [(4, 3), (2, 2), (5, 8)], [(3, 2)], [(7, 1), (8, 8), (2, 2), (4, 5)], [(6, 2), (3, 5), (2, 1)], [],
      [(7, 1)], [(8, 6)], [(6, 1)]]
start = 0
target = 8
resB = Alice_and_Bob(t3, start)

if resB[1][target][0] <= resB[1][target][1]:
    print("Alicja")
    print(resB[1][target][0])
    print_path_BAs(resB[0], target, 0)
else:
    print("Bob")
    print(resB[1][target][1])
    print_path_BAs(resB[0], target, 1)


chuj = [[(1, 10), (2, 1), (4, 5)], [(0, 10), (2, 1), (3, 5)], [(0, 1), (1, 1)], [(1, 5)], [(0, 5)]]
z = 3
do = 4
resP = Alice_and_Bob(chuj,z)

print("\n ------")
if resP[1][do][0] <= resP[1][do][1]:
    print("Alicja")
    print(resP[1][do][0])
    print_path_BAs(resP[0], do, 0)
else:
    print("Bob")
    print(resP[1][do][1])
    print_path_BAs(resP[0], do, 1)
    #0  1  2  3  4   5  6  7
#G2 = [[0, 1, 0, 0, 0, 15, 0, 0],    #0
      #[0, 0, 5, 0, 0, 0, 0, 0],     #1
      #[0, 0, 0, 0, 7, 0, 110, 0],   #2
      #[0, 0, 0, 0, 0, 0, 0, 0],     #3
      #[0, 0, 7, 0, 0, 8, 100, 90],  #4
      #[0, 0, 0, 0, 8, 0, 0, 0],     #5
      #[0, 0, 0, 0, 0, 0, 0, 0],     #6
      #[0, 0, 0, 0, 0, 0, 7, 0]]     #7

#          0            1          2         3         4                        5     6   7
G2 = [[(1,1),(5,15)],[(2,5)],[(4,7),(6,110)],[],[(2,7),(5,8),(6,100),(7,90)],[(4,8)],[],[(6,7)]]
a2,b2 = 0,6
#odp2 = ("Alicja",8,[0,1,2,4,6])
res2 = Alice_and_Bob(G2,a2)

print("\n ------")
if res2[1][b2][0] <= res2[1][b2][1]:
    print("Alicja")
    print(res2[1][b2][0])
    print_path_BAs(res2[0], b2, 0)
else:
    print("Bob")
    print(res2[1][b2][1])
    print_path_BAs(res2[0], b2, 1)


#G4 = [[0, 100, 50, 0, 0], [0, 0, 12, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
G4 = [[(1,100),(2,50)],[(2,12)],[],[],[]]
a4,b4 = 0,4
#odp4 = (None,None,None)
res4 = Alice_and_Bob(G4,a4)

print("\n ------")

if res4[1][b4][0] != float('inf') or res4[1][b4][1] != float('inf'):
    if res4[1][b4][0] <= res4[1][b4][1]:
        print("Alicja")
        print(res4[1][b4][0])
        print_path_BAs(res4[0], b4, 0)
    else:
        print("Bob")
        print(res4[1][b4][1])
        print_path_BAs(res4[0], b4, 1)

else:
    print(None)


G1= [[0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 120],
    [-1, 0, 0, 0, 0, 0, 0, 0]]
    '''

G1 = [[(1,1)],[(2,2)],[(3,1)],[(4,2)],[(5,1)],[(6,2)],[(7,120)],[]]
a1,b1 = 0,7
#odp1 = ("Bob",6,[0,1,2,3,4,5,6,7])

res1 = Alice_and_Bob(G1,a1)

print("\n ------")

if res1[1][b1][0] != float('inf') or res1[1][b1][1] != float('inf'):
    if res1[1][b1][0] <= res1[1][b1][1]:
        print("Alicja")
        print(res1[1][b1][0])
        print_path_BAs(res1[0], b1, 0)
    else:
        print("Bob")
        print(res1[1][b1][1])
        print_path_BAs(res1[0], b1, 1)

else:
    print(None)