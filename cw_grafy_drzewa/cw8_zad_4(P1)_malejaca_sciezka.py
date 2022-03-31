'''Zadanie 4. (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
{1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.'''

# ciche zał, graf jest skierowany (chociaz jest to bardziej szczegół implementacyjny, reprezentowany macierzowo
# idea - przechodzimy DFS'em po grafie, ale zamiast oznaczac wierzchołki jako odwiedzone, usuwamy krawedzie

def decreasing_path(G,s,t):
    n = len(G)
    previous = [0] * n
    flag = False

    def DFS_visit(G, s, last):
        nonlocal t,flag
        if s == t:
            flag = True


        for e in range(previous[s], n):
            if G[s][e] < last and G[s][e] != 0:
                #G[s][e] = float('inf') #oznacza usunieta krawędź
                previous[s] = e + 1
                #print(previous)
                #print("idziemy z:",s,"do:",e)
                #print("----")
                DFS_visit(G, e, G[s][e])


    DFS_visit(G, s, float('inf'))

    return flag

        #0  #1  #2 #3 #4 #5 #6 #7
test = [[0, 10, 0, 0, 0, 0, 6, 0], #0
        [0, 0, 9, 0, 0, 0, 0, 0],  #1
        [0, 0, 0, 8, 0, 0, 0, 0],  #2
        [0, 0, 0, 0, 7, 0, 2, 0],  #3
        [0, 0, 0, 0, 0, 9, 0, 0],  #4
        [0, 0, 0, 0, 0, 0, 0, 0],  #5
        [0, 0, 0, 0, 0, 0, 0, 5],  #6
        [0, 0, 0, 0, 0, 0, 0, 0]]  #7

print(decreasing_path(test,0,7))