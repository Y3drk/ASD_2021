'''Zadanie 4. (szachuję) Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami.
Każde miasto jest otoczone murem i ma tylko dwie bramy—północną i południową. Z każdej bramy prowadzi
dokładnie jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też
być połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicji
Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić algorytm, który
stwierdza czy odpowiednia trasa gońca istnieje'''

# pomysł z superoazami, wystaczy, że odpowiednio je stworzymy, nie potrzebujemy nawet nowego grafu bo wiemy ze miasta spełniaja wkw na istnienie cyklu eulera
# jesli stopnie superoaz sa parzyste to trasa istnieje

# superoazy stworzymy w nastepujacy sposob, bedziemy właczac DFS idacy tylko po oazach i dla kazdego właczenia dfs bedziemy oznaczac odwiedzone wierzchołki innym numerem.
# oazy oznaczone jednym numerem stworza jedna super oaze, potem dla kazdej superoazy, wpiszemy do niej te krawedzie ktore łaczyły miasta z jej składowymi
# nastepnie pozostanie tylko sprawdzenie parzystosci stopni
# I to tablica ideantyfikujaca miasta/oazy - oaza == True, miasto == False


def super_oasis(G,I):
    n = len(G)
    marker = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    which_so = [-1 for _ in range(n)]


    def DFS_visit(G,s,marker):
        visited[s] = True
        for u in G[s]:
            if not visited[u] and I[u]:
                parent[u] = s
                DFS_visit(G,u, marker)

        which_so[s] = marker

        return

    for u in range(n):
        if not visited[u] and I[u]:
            DFS_visit(G,u,marker)
            marker += 1

    Supers = [[] for _ in range(marker)]
    #print(which_so)

    for i in range(n):
        if I[i]:
            for j in range(len(G[i])):
                if not I[G[i][j]]:
                    Supers[which_so[i]].append(G[i][j])

    #print(Supers)
    for oasis in Supers:
        #print(len(oasis))
        if len(oasis) % 2 == 1:
            return False

    return True

#          0       1       2      3        4      5      6       7     8     9       10     11      12      13      14       15        16        17       18       19
test = [[10,16],[10,19],[7,11],[18,19],[12,14],[13,15],[7,8],[2,6,8],[6,9],[8,10],[0,1,9],[2,12], [4,11,19], [5,14], [4,13], [5,16,18],[0,15,17],[16,18], [3,15,17], [1,3,12]]

I = [False,False,False,False,False,False, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

print(super_oasis(test,I))
