'''Dana jest dwuwymiarowa tablica NxN, w ktorej kazda komórka ma wartosc W reprezentujaca wode lub wartosc L resprezentujaca ląd.
Grupe komórek wody połączoną ze soba brzegami nazywamy jeziorem.
Napisz algorytm, który:
c) zakładajac ze pola M[0][0] i M[n-1][n-1] sa lądem sprawdź czy można przejsc miedzy nimi droga ladowa zakładajac ze mozna chodzic tylko w bok i w dół\
d) znajdź najkrótsza sciezke miedzy tymi punktami i wypisz indeksy pol tej sciezki '''


# idea - do znajdywania najkrótszej sciezki świetnie nadaje sie BFS z odpowiednio ustawioną tablica distance
# do wypisywania sciezki przyda sie tablica parent

# tym razem to jeziora nas nie obchodza wiec przerobimy lad na graf

def land_into_graph(M):
    n = len(M)
    G = [[None]*n for _ in range(n)]

    '''for elem in G:
        print(elem)
    print("----")'''

    for row in range(n):
        for col in range(n):
            if M[row][col] == 'L':

                if G[row][col] == None:
                    G[row][col] = []

                if row+1 < n and M[row+1][col] == 'L':
                    G[row][col] += [(row+1,col)]

                    if G[row+1][col] == None:
                        G[row+1][col] = []

                    G[row+1][col] += [(row,col)]

                if col + 1 < n and M[row][col+1] == 'L':
                    G[row][col] += [(row,col+1)]
                    if G[row][col+1] == None:
                        G[row][col+1] = []

                    G[row][col+1] += [(row,col)]

                if len(G[row][col]) == 0:
                    G[row][col] = 'solo'

    return G


def if_Land_path_and_shortest_BFS(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    parent = [[None]*n for _ in range(n)]
    distance = [[-1] * n for _ in range(n)]
    Q = Queue()

    Q.put(s)
    distance[s[0]][s[1]] = 0

    while not Q.empty():
        uy,ux = Q.get()
        for v in G[uy][ux]:
            if distance[v[0]][v[1]] == -1:
                distance[v[0]][v[1]] = distance[uy][ux] + 1
                parent[v[0]][v[1]] = (uy,ux)
                Q.put(v)

    if distance[n-1][n-1] != -1:
        return distance[n-1][n-1],parent

    else:
        return False,False


def print_path(Parent):
    n = len(Parent)
    y,x = n - 1, n - 1
    while y != 0 or x != 0:
        print((y,x),end=', ')
        y, x = Parent[y][x]

    print((0,0))

    return



Map = [['L', 'W', 'L', 'L', 'L', 'L', 'L', 'L'],
       ['L','W','L','W','W','L','L','L'],
       ['L','L','L','W','W','L','W','L'],
       ['L','W','W','W','W','L','W','L'],
       ['L','L','W','W','L','L','L','L'],
       ['L','W','L','L','L','L','W','W'],
       ['W','W','L','W','W','L','W','L'],
       ['L','L','L','W','L','L','L','L']]

Graph = land_into_graph(Map)

'''for row in Graph:
    print(row)'''

result = if_Land_path_and_shortest_BFS(Graph,(0,0))

if result[0] == False:
    print("Nie ma ścieżki miedzy ww. punktami")
else:
    print("Scieżka ta istnieje i długosc najkrótszej mozliwej takiej ściezki to:",result[0],"a szła ona po polach:",end='')
    print_path(result[1])
