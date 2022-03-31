'''1. Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
możliwa sekwencja ruchów spełniająca:
- każdy ruch kończy się zbiciem skoczka
- sekwencja kończy się gdy zostanie jeden skoczek.'''

# idea - łaczymy krawedziami skoczki, tworzac z nich graf, puszczamy Dfsa od losowego skoczka,
# jesli uda sie odwiedzić wszystkie skoczki to sciągamy je w malejącej kolejnosci czasu przetworzenia

def knigth_moves(row,col,n):
    moves = [(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2)]
    res = []
    for move in moves:
        if 0 <= row + move[0] <= n - 1 and  0 <= col + move[1] <= n - 1:
            res.append((row + move[0],col + move[1]))

    return res


def make_graf(S):
    n = len(S)
    num_of_knights = 0
    where_knights = []
    for row in range(n):
        for col in range(n):
            if S[row][col] == 1:
                num_of_knights += 1
                where_knights.append((row,col))

    Graph = [[] for _ in range(num_of_knights)]

    for k1 in range(num_of_knights):
        tmp = knigth_moves(where_knights[k1][0],where_knights[k1][1],n)
        for move in tmp: #stała ilosc
            for k2 in range(k1 + 1, num_of_knights): # O(n^2)
                if move == where_knights[k2]:
                    Graph[k1].append(k2)

    return Graph


def DFS_knights(G): #w wiekszosci implementacji nie wskazujemy konkretnego wierzchołka od którego zaczynamy
    n = len(G)
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]

    time = 0 #umowny/wirtualny czas, potrzebny nie tyle w samym DFS co w jego licznych zastosowaniach

    def DFS_visit(G,s):
        nonlocal time
        time += 1
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        time += 1
        return

    DFS_visit(G,0)

    return visited


def knights(S):
    G = make_graf(S)
    #print(G)
    res = DFS_knights(G)
    #print(res)
    for knight in res:
        if not knight:
            return False

    return True



T_good = [[0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,1,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,1,0],]

T_bad = [[1,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,1,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,1,0],]

print(knights(T_good))
print("----")
print(knights(T_bad))
print("----")




