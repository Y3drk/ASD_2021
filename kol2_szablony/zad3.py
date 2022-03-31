from zad3testy import runtests

# 1) Przekształcamy plamy ropy w niespojny graf
# 2) liczymy objetość kazdej plamy i umieszczamy ją w punktcie, gdzie na nia natrafilismy (jesli plama wypływała na 0 gdzies poźniej to tam
# umieszczamy 0. Jesli teraz wessiemy cała objętosc plamy to nie dosc, ze zyskujemy wiekszy zasieg to i zatrzymujemy sie mniej. Nie zajdzie
# sytuacja, że gdybysmy wessali ja cała to potem braknie nam paliwa bo przeciez juz będziemy je mieć w naszej cysternie.)

# 3) układamy dynamiczną funkcję f(i,j) = najmniejsza ilosc tankowań potrzebna aby dojechac na pozycje i majac j paliwa
# f(i,j) = min ( po k od 1 do i) { f(i-k,j - R[i] + k) }
# f(0, dla kazdego j od 0 do R[0]) = 1
# f(i, 0) = 1

# dodatkowo odpowiednio uzupełniamy tablice Route aby móc odzyskac miejsca gdzie sie zatrzymalismy

# czas działania jest narzucony przez funkcje f i wynosi O(n^3)


def plan(T):
    # tu prosze wpisac wlasna implementacje
    m = len(T[0])
    Road = preprocess(T)  #preprocessing na graf plus DFS w plamach oleju O(n^2 + O(V+E))
    been_there = [False for _ in range(m)]
    route = [0]
    been_there[0] = True
    fuel = Road[0]
    print(Road)
    while fuel < m - 1:
        pos = 1
        maxi = 0
        where = m
        print(fuel)
        while pos <= fuel:
            if been_there[pos] == False and Road[pos] > maxi:
                maxi = Road[pos]
                where = pos

            pos += 1

        been_there[where] = True
        route += [where]
        fuel += maxi

    print(route)

    return route


def preprocess(T):
    n = len(T)
    m = len(T[0])
    G = route_into_graph(T)
    R = [0 for _ in range(m)]
    visited = [[False]*m for _ in range(n)]

    '''for row in G:
        print(row)'''

    def stains_of_oil_DFS(G,T,vy,vx,size = 0):   #size sie źle nalicza
        visited[vy][vx] = True
        print("size 1 run:",size,vy,vx)
        for u in G[vy][vx]:
            if u[0] == vy and u[1] == vx:
                size = T[vy][vx]
                break

            elif not visited[u[0]][u[1]]:
                size = stains_of_oil_DFS(G,T,u[0],u[1],size + T[vy][vx])
                print(size,vy,vx)

        return size

    for col in range(m):
        if T[0][col] == 0 or visited[0][col]:
            continue

        else:
            R[col] = stains_of_oil_DFS(G,T,0,col)

    return R


def route_into_graph(T):
    n = len(T)
    m = len(T[0])
    G = [[None]*m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if T[row][col] > 0:

                if G[row][col] == None:
                    G[row][col] = []

                if row+1 < n and T[row+1][col] > 0:
                    G[row][col] += [(row+1,col)]

                    if G[row+1][col] == None:
                        G[row+1][col] = []

                    G[row+1][col] += [(row,col)]

                if col + 1 < n and T[row][col+1] > 0:
                    G[row][col] += [(row,col+1)]
                    if G[row][col+1] == None:
                        G[row][col+1] = []

                    G[row][col+1] += [(row,col)]

                if len(G[row][col]) == 0:
                    G[row][col] = [(row,col)]

    return G





runtests(plan)
