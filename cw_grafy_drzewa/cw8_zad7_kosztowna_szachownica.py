'''Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.
'''

# idea - BFS z trikiem implementacyjnym, do kolejki wrzucamy krotki w postaci (wierzchołek, licznik) gdzie poczatkowo, licznik == wartosc pola,
# za kazdym razem gdy wyciagamy wierzchołek z kolejki zmniejszamy licznik o 1 i dopoki jest >0 wkładamy wierzchołek z powrotem do kolejki, co
# idealnie zsymuluje nam koszta jakie musimy poniesc aby dosjc do pola G[n-1][n-1]


def expensive_path(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [[False]*n for _ in range(n)]
    parent = [[None]*n for _ in range(n)]
    cost = [[0]*n for _ in range(n)]
    Q = Queue()

    r,c = s
    Q.put((r,c,G[r][c]))
    visited[r][c] = True

    '''for row in G:
        print(row)'''

    while not Q.empty():
        r,c,cnt = Q.get()
        cost[r][c] += 1
        cnt -= 1

        if cnt > 0:
            Q.put((r,c,cnt))
        else:
            for i in range(-1, 2, 2):
                if r + i > -1 and r + i < n and not visited[r + i][c]:  # góra / dół
                    cost[r + i][c] = cost[r][c]
                    visited[r + i][c] = True
                    parent[r + i][c] = [r, c]
                    Q.put((r + i, c, G[r + i][c]))

                if c + i > -1 and c + i < n and not visited[r][c + i]:  # lewo / prawo
                    visited[r][c + i] = True
                    cost[r][c + i] = cost[r][c]
                    parent[r][c + i] = [r, c]
                    Q.put((r, c + i, G[r][c + i]))



    '''print("last")
    for row in cost:
        print(row)'''

    return cost[n-1][n-1]



test = [[1,2,1,3,5,5],
        [3,1,5,2,1,5],
        [3,1,3,2,4,4],
        [2,2,5,1,3,4],
        [2,3,1,2,3,4],
        [4,3,2,1,1,8]]

print(expensive_path(test,(0,0)))

