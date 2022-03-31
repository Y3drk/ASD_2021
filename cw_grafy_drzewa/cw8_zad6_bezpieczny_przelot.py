'''Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.'''

# pomysł - sortujemy krawedzie, i przechodzimy przez nie "oknem" od p do p + 2*t. Dla kazdego takiego "okna" jesli sa w nim s i t, sprawdzamy czy mozna
# z nich utworzyc sciezke

# zał: graf jest nieskierowany reprezentowany macierzowo



#OGOLNIE TROCHE SIE ZLOZONOSC PIERDOLI, MOZNA ZROBIC TO LEPIEJ NA PEWNO

def safe_flight(G,s,f,t):
    n = len(G)
    visited = [-1 for i in range(n)]
    Altitudes = []

    for i in range(n):   #wyciagniecie krawedzi z grafu
        for j in range(i+1,n):
            if G[i][j] != 0:
                Altitudes += [[G[i][j], i, j]]

    Altitudes.sort() #sortujemy krawedzie O(ElogE)
    #print(Altitudes)
    window = [[0]* n for i in range(n)]
    inside = [0 for _ in range(n)]
    tracker = 1
    flag = False

    def DFS_visit(G,s,f):
        nonlocal tracker,flag
        visited[s] = tracker
        #print(visited)
        if s == f:
            flag = True

        for u in range(n):
            #print(tracker, inside[u],visited[u],window[s][u],"dla u=",u)
            if inside[u] == tracker and visited[u] != tracker and window[s][u] == tracker:
                #print("jestesmy w wierzchołu:", s, "idziemy do:", u)
                DFS_visit(G,u,f)
                #print(".....")

        return

    for i in range(len(Altitudes)):
        #print(i)
        for j in range(i,len(Altitudes)):     #tutaj sie robi E^2 bo ja jestem głąbem, trzeba mądrze przesuwac okno a nie tak na pałe jak ja, ale i tak jest słabo bo w kazdej krawedzi trzeba zmieniac tracker
            if Altitudes[j][0] > Altitudes[i][0] + 2*t:
                #print("dalej nie mozemy dodawac")
                if inside[s] == inside[f] == tracker:
                    #print(inside)
                    #print(".....")
                    #for row in window:
                        #print(row)
                    #print("wywołujemy DFS")
                    #print("-----")
                    DFS_visit(G,s,f)
                    if flag:
                        return True

                tracker += 1
                #print("break")
                break

            #print("działamy sb")
            #print("j:", Altitudes[j][0], "|", j, "i:", Altitudes[i][0], "|", i, "limit:", Altitudes[i][0] + 2 * t,", tracker:", tracker)
            window[Altitudes[j][1]][Altitudes[j][2]] = tracker
            window[Altitudes[j][2]][Altitudes[j][1]] = tracker
            #print("dodano krawedz:", Altitudes[j][1], "--", Altitudes[j][2])
            inside[Altitudes[j][1]] = tracker
            inside[Altitudes[j][2]] = tracker

    return flag


test = [[0,7,20,0,30,0,0,0,0,0],
        [7,0,0,0,0,0,0,0,0,0],
        [20,0,0,15,0,100,0,0,0,0],
        [0,0,15,0,31,27,0,7,0,0],
        [30,0,0,31,0,10,0,0,0,0],
        [0,0,100,27,10,0,29,20,0,0],
        [0,0,0,0,0,29,0,28,50,0],
        [0,0,0,7,0,20,28,0,27,0],
        [0,0,0,0,0,0,50,27,0,15],
        [0,0,0,0,0,0,0,0,15,0]]

altitude = 5
print(safe_flight(test,0,8,5))
