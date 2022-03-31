'''otrzymujemy na wejsciu liste ludzi, ktorzy wzajemnie sie znaja, osoby sa ponumerowane od 0 do n-1
Pierwszego dnia osoba 0 przekazuje plotke wszystkim swoim znajomym. Drugiego dnia beda oni mogli przekazac ja wszystkim ich znajomym ktorzy jeszcze jej
nie usłyszeli itd itd
Napisz algorytm, który zwróci dzień, w ktorym najwiecej osob usłyszało plotke i ilosc osob, ktore tego dnia ja otrzymały'''

# idea - lista wzajemnych znajomosci to de facto lista krawedzi grafu, a osoby to wierzchołki. Plotka roznosi sie po takim grafie jak fala, wykorzystamt wiec BFS
# uzyjemy tablicy Day, która bedzie pełnic role zarówno role licznika dni, jak i tablicy visited w org wersji alg. przyda nam sie równiez tablica parent
# po przejsciu całego grafu cała potrzebna nam informacja bedzie po prostu w tablicy Day i odp po niej przechodzac wyciągniemy interesujace nas informacje

# ciche zał. powstały graf jest spójny, kazdy zna kogos komu móglby przekazac plotke
# liste znajomosci przerobimy na liste sasiedztwa


def transform_to_adjacency_list_indirected(T, n):
    G = [[]*n for _ in range(n)]

    for i in range(len(T)): #przepisanie do listy sasiedztwa O(n)
        G[T[i][0]] += [T[i][1]]
        G[T[i][1]] += [T[i][0]]

    '''for i in range(n): #sort dla porzadku wewnątrz listy sasiedztwa, raczej niekonieczne, O(V*eloge) ??? w najgorszym wypadku (graf pełny) O(V^2*logV)
        G[i].sort() #raczej nie powinno to miec znaczenia, wiec sprobujemy narazie bez tego
        '''
    #print(G)

    return G


def whsipers_BFS(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    parent = [None for _ in range(n)]
    Day = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)
    Day[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if Day[v] == -1:
                parent[v] = u
                Day[v] = Day[parent[v]] + 1
                Q.put(v)

    #print(Day)
    #pozostało tylko wyciagnąc informacje z  Day, maksymalna ilosc dni nie przekroczy długosci średnicy grafu,
    # która nigdy nie przekroczy n (przypadek gdy graf jest jedna sciezka)
    Counter = [0 for i in range(n)]
    # kosztuje nas to dodatkowe O(n) pamieci ale pozwala wykonac wyciaganie wyniku w czasie O(2n) - duzo lepszym niz O(n^2) gdybysmy oszczedzali pamiec
    for i in range(n):
        Counter[Day[i]] += 1

    #print(Counter)
    maxi = -1
    sup = n
    for j in range(len(Counter)):
        if Counter[j] > maxi:
            maxi = Counter[j]
            sup = j

    return sup, maxi


test = [(0,1),(0,2),(1,3),(1,4),(2,6),(2,7),(4,5),(6,7),(4,6)]
n = 8
Graph = transform_to_adjacency_list_indirected(test, n)
result = whsipers_BFS(Graph,0)
print("Najwiecej osob usłyszało plotke w dniu nr:",result[0],"a było to",result[1],"osob")


