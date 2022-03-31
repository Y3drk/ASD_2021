'''Dana jest dwuwymiarowa tablica NxN, w ktorej kazda komórka ma wartosc W reprezentujaca wode lub wartosc L resprezentujaca ląd.
Grupe komórek wody połączoną ze soba brzegami nazywamy jeziorem.
Napisz algorytm, który:
a) policzy ile jest jezior na mapie
b) poda wielkosc najwiekszego jeziora'''

# trzeba odp zmapowac jeziora na graf niespojny, ale bedziemy tez posługiwac sie sama mapa
# wykorzystamy algorytm DFS, trzeba uzupełnic DFS_visit o opcje, która zwróci licznik odwiedzonych pol


def lakes_into_graph(M):
    n = len(M)
    G = [[None]*n for _ in range(n)]


    for row in range(n):
        for col in range(n):
            if M[row][col] == 'W':

                if G[row][col] == None:
                    G[row][col] = []

                if row+1 < n and M[row+1][col] == 'W':
                    G[row][col] += [(row+1,col)]

                    if G[row+1][col] == None:
                        G[row+1][col] = []

                    G[row+1][col] += [(row,col)]

                if col + 1 < n and M[row][col+1] == 'W':
                    G[row][col] += [(row,col+1)]
                    if G[row][col+1] == None:
                        G[row][col+1] = []

                    G[row][col+1] += [(row,col)]

                if len(G[row][col]) == 0:
                    G[row][col] = 'solo'

    return G


def Lakes_count_and_measure_DFS(G,M):
    n = len(G)
    visited = [[False]*n for _ in range(n)]
    lakes, max_surface = 0, 0

    def Lakes_size_DFS_visit(G,vy,vx,size = 0):
        visited[vy][vx] = True
        for u in G[vy][vx]:
            if not visited[u[0]][u[1]]:
                size = Lakes_size_DFS_visit(G,u[0],u[1],size + 1)

        return size

    for row in range(n):
        for col in range(n):
            if M[row][col] == 'L':
                continue

            elif visited[row][col]:
                continue

            elif not visited[row][col] and  G[row][col] == 'solo':
                    lakes += 1
                    max_surface = max(max_surface,1)


            else:
                lakes += 1
                max_surface = max(max_surface,Lakes_size_DFS_visit(G,row,col))

    return lakes, max_surface


Map = [['L', 'W', 'L', 'L', 'L', 'L', 'L', 'L'],
       ['L','W','L','W','W','L','L','L'],
       ['L','L','L','W','W','L','W','L'],
       ['L','W','W','W','W','L','W','L'],
       ['L','L','W','W','L','L','L','L'],
       ['L','W','L','L','L','L','W','W'],
       ['W','W','L','W','W','L','W','L'],
       ['L','L','L','W','L','W','L','L']]

Graph = lakes_into_graph(Map)

for row in Graph:
    print(row)


result = Lakes_count_and_measure_DFS(Graph,Map)
print("Na mapie jest:",result[0],"jezior. Najwieksze z nich ma powierzchnie:",result[1])
