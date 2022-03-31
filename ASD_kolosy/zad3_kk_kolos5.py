# pomysł (czy naprawde działa cholera wie)
# 0) jesli nasz garnacarz kogos zna to uaktualniamy wage krawedzi na 0 O(UE)
# (tak wiem ze złozonosc tam robi salto, ale pewnie mozna to jakos obejsc, a poza tym Falisz da tablice tablic co nie :(( )
# 1) odpalamy sobie Bellmana-Forda niczym sie nie przejmujac O(VE)
# 2) Analizujemy wyniki, wykonujac ponizsza petlę az albo poznamy wszystkich, albo skoncza nam sie pieniadze: O(całkowity obrót*V) - moze troche lepiej, ciezko okreslic
# A) jesli jakas sciezka ma ujemny koszt, to znaczy ze mozemy ja cała zebrac do naszych nowych znajomych i w dodatku dodac sobie kase
# co tez robimy, a bierzemy najmniejsza wartosc ujemna bo to daje szanse ze po drodze było wiecej ludzi, ale jesli to nie prawda to nic nie szkodzi,
# bo te wieksze wartosci ujemne tez predzej czy pozniej zbierzemy.
# B) potem szukamy najwiekszego kosztu dodatniego aby nie przekraczał pieniedzy, które mamy i z niego sb zbieramy nowych kolegów
# 2.3) jezeli zostały nam jakies wierzchołki z ujemnym kosztem to znowu zadziała nam krok A
# i tak w koło macieju - ogólnie złożonosc pseudowielomianowa, elo :))

# ano i załozenie - NIE MA UJEMNYCH CYKLI W GRAFIE

def BF_4_adjlist(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    #relaksacje
    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u

    for i in range(n - 1):
        for u in range(n):
            for v,edge in G[u]:
                relax(u,v,edge)


    return distance,parent


def szukaj_znajomosci(G,U,h):
    n = len(G)
    # juz ustawienie tych krawedzi na 0 robi ci pokurwienie w mózgu |U| * E
    for person in U:
        for u in G:
            #print(u)
            xd = len(u)
            for v in range(xd):
                if u[v][0] == person:
                    u.append((u[v][0],0))

            for v in range(xd):
                if u[v][0] == person and u[v][1] != 0: # tak wiem ze złożonosc odwala to jest robocze, bo krotki
                    u.pop(v)

    tmp = [False for _ in range(n)]
    tmp[0] = True
    flag = True
    pitos = 12*h
    wow = BF_4_adjlist(G,0)
    best_ind = None

    while pitos >= 0 and flag:
        flag = False

        best = 0
        for i in range(n):
            if pitos >= wow[0][i] > best and not tmp[i]:
                best = wow[0][i]
                best_ind = i

        insert_path(wow[1],tmp,best_ind)
        pitos -= wow[0][best_ind]


        best = float('-inf')
        for i in range(n):
            if 0 > wow[0][i] > best and not tmp[i]:
                best = wow[0][i]
                best_ind = i

        if best != float('-inf'):
            pitos -= wow[0][best_ind]
            insert_path(wow[1],tmp,best_ind)


        for i in range(n):
            if not tmp[i]:
                flag = True
                break

    res = 0
    for i in range(1,len(tmp)):
        if tmp:
            res += 1

    res -= len(U)
    #print(tmp)
    print(wow[0])
    print(wow[1])

    # napisz tu k0z4k implementacje
    return res


def insert_path(P,T,ind):
    while not T[ind]:
        T[ind] = True
        ind = P[ind]


G = [[(7, 10), (1, 10)],
               [(2, 10), (4, 70)],
               [(3, 10)],
               [(4, -10010)],
               [(5, 5)],
               [(6, 5), (9, 2)],
               [(7, 5)],
               [(8, 50)],
               [(9, 5)],
               [(10, 5)],
               [(11, 2)],
               []]
U = []
hajs = 2
odp=2

print(szukaj_znajomosci(G,U,hajs))

from zad3testy_kk_kolos5 import runtests
runtests(szukaj_znajomosci)

#BIG BŁĄD !!! SAM POMYSŁ GIT, ALE ODZYSKIWANIE WYNIKU W DUPE