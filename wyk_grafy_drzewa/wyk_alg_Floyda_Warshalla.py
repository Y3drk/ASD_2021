# konwencja : graf jest skierowany, a reprezentujemy go macierzowo,
# W to macierz wag krawedzi grafu (czyli de facto jego ww. reprezentacja) , a P[u][v] = poprzednik v na najkrótszej scieżce do u


def kopia(tab):
    n = len(tab)
    kopia = [[0] * n for _ in range(n)]
    for w in range(n):
        for k in range(n):
            kopia[w][k] = tab[w][k]

    return kopia


def print_selected_path(P,ind,stop):
    if ind != stop:
        print_selected_path(P,P[stop][ind],stop)

    print(ind,end=' ')


def FW(G):
    n = len(G)
    S = kopia(G)  # niekoniecznie potrzebne, robimy kopie aby nie zniszczyc wyjsciowej reprezentacji grafu
    P = [[None] * n for _ in range(n)]


    for u in range(n):  # inicjalizacja tablicy parentów
        for v in range(n):
            if G[u][v] != float('inf') and u != v:
                P[u][v] = u

    # wlasciwy algorytm
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]


    # weryfikacja - poszukiwanie cyklu ujemnego
    for x in range(n):
        for y in range(x + 1, n):
            if S[x][y] + S[y][x] < 0:
                return False, None, None

    return True, S, P


test = [[0, 10, 3, float('inf'), float('inf'), float('inf'), float('inf')],
        [float('inf'), 0, float('inf'), float('inf'), float('inf'), 5, 1],
        [float('inf'), float('inf'), 0, float('inf'), 1, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), 0, float('inf'), 8, float('inf')],
        [float('inf'), -4, float('inf'), -20, 0, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 16],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]]

test_pod_wyjebke = [[float('inf'), 10, 3, float('inf'), float('inf'), float('inf'), float('inf')],
                    [float('inf'), float('inf'), 8, float('inf'), float('inf'), 5, 1],
                    [float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), float('inf')],
                    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8, float('inf')],
                    [float('inf'), -88, float('inf'), -20, float('inf'), float('inf'), float('inf')],
                    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 16],
                    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]]

res = FW(test)

if res[0]:
    for rowd in res[1]:
        print(rowd)
    print("-----")

    for rowp in res[2]:
        print(rowp)

    print("-----")
    print("A sciezka od:",0,"do",6,"to:")
    print_selected_path(res[2],6,0)
    print()

else:
    print(res[0])


T = [
[0, 1, 1, float('inf'), 1],
[1, 0, float('inf'), 1, float('inf')],
[1, float('inf'), 0, float('inf'), 1],
[float('inf'), 1, float('inf'), 0, 1],
[1, float('inf'), 1, 1, 0],
]

res = FW(T)
for row in res[1]:
    print(row)
