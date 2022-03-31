'''Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N].
Jeżeli T[a][b] = 1 to wykonanie zadania a musi poprzedzać wykonanie zadania b.
W przypadku gdy T[a][b] = 2 zadanie b musi być wykonane wcześniej,
a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna.
Proszę zaimplementować funkcję tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami
zadań do wykonania.
Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem
jest tablica [1,0,2,3]'''

# podana tablica może reprezentowac DAG, wiemy, ze nie wystąpią cykle bo jest to sytuacja niemozliwa (np w C3 pierwsze dwie krawedzie narzucałyby koloejnosc 0->1->2,
# a z kolei krawedz z 2 do 0 wymagałaby kolejnosci 2-> 0 co nie ma sensu
# sortujemy go topologicznie i to jest nasza odpowiedz
# złożonosc to DFS na macierzy sasiedztwa czyli V^2


def tasks(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    list_of_tasks = []

    def DFS_visit(G,s):
        #print("jestesmy w:",s)
        nonlocal list_of_tasks
        visited[s] = True
        for u in range(len(G)):
            if not visited[u] and G[s][u] == 1:
                parent[u] = s
                DFS_visit(G,u)

        list_of_tasks += [s]
        return

    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return list_of_tasks[::-1]


T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]
print(tasks(T))