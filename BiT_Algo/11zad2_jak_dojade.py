'''Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego,
który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d.
Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową.
Przykład Dla tablic
G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
funkcja jak dojade(G, P, 5, 0, 2) powinna zwrócić [0,3,2]. Dla tych samych tablic funkcja
jak dojade(G, P, 6, 0, 2) powinna zwrócić [0,1,2], natomiast jak dojade(G, P, 3, 0, 2)
powinna zwrócić None.'''

# znowu space/state graph lub zabawy implementacyjne z dijskstra, tym razem dla treningu walne sb space-state
# Sytuacja jest troche inna bo tym razem nie płacimy za paliwo i zawsze tankujemy do pelna --> graf jest mniej rozbudowany bo kazde miasto ze stacja pozostaje 1 wierzchołkiem
# wierzchołki beda zawierac infromacje dla kazdej krawedzi (wierzchołek, ile w nim paliwa, odleglosc)


def into_Space_State(G,P,capacity):
    n = len(G)
    SS_Graph = [[[]]*(capacity+1) for i in range(n)]

    for u in range(n):
        for fu in range(capacity + 1):
            tmp = []
            for v in G[u]:
                if P[v[0]]: #gdy miasto jest stacja
                    if fu - v[1] >= 0:
                        tmp.append((v[0],capacity,v[1]))  #jesli tylko mozemy dojechac to miasta ze stacja
                else:
                    for fv in range(capacity + 1):
                        if fu - v[1] == fv:  #jesli dojeżdzamy do danego wierzchołka, który nie jest stacja z idealnie taka iloscia paliwa jaka mamy wytypowana
                            tmp.append((v[0],fv,v[1]))

            SS_Graph[u][fu] = tmp

    return SS_Graph


def Dijkstra_4_Space_State_fucking_Graph(G, a, cap, P, b):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [[False]*(cap+1) for _ in range(n)]
    distance = [[float('inf')]*(cap+1) for _ in range(n)]
    parent = [[None]*(cap+1) for _ in range(n)]

    Q.put((0, cap, a))  # (odległosc ,ile paliwa, wierzchołek), nie opłaca sie startowac z mniejsza iloscia paliwa
    distance[a][cap] = 0

    def relax(u, fu, v, fv, edge):
        if distance[v][fv] > distance[u][fu] + edge:
            distance[v][fv] = distance[u][fu] + edge
            parent[v][fv] = u,fu
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,ft,t = Q.get()
        if processed[t][ft] == True:
            continue
        else:
            processed[t][ft] = True
            for u in G[t][ft]:         # u = (drugi wierzcholek krawedzi, ile paliwa zostanie, koszt krawedzi)
                if not processed[u[0]][u[1]]:
                    if relax(t,ft,u[0],u[1], u[2]):
                        Q.put((distance[u[0]][u[1]],u[1],u[0]))

    #for row in distance:
        #print(row)
    #print("-----")

    best = float('inf')
    b_ind = None
    for i in range(cap + 1):
        if best > distance[b][i]:
            best = distance[b][i]
            b_ind = i


    if best < float('inf'):
        return best, parent, b_ind

    else:
        return None, None, None


def get_path(P,indu,indc,tmp):
    if P[indu][indc] != None:
        #print(tmp, indu)
        tmp = get_path(P,P[indu][indc][0],P[indu][indc][1], tmp + [indu])

    return tmp


test = [[(1,6),(3,5),(4,2)],[(2,1),(3,2)],[],[(2,4)],[(2,8)]]
cap = 6
a = 0
b = 2
P = [True,True,False,True,False]
SS_G = into_Space_State(test,P,cap)

#for row in SS_G:
  # print(row)
#print("-----")
res = Dijkstra_4_Space_State_fucking_Graph(SS_G,a,cap,P,b)
print(res[0])
if res[0] != None:
    #for row in res[1]:
        #print(row)

    path = []
    path = get_path(res[1],b,res[2],path)
    path += [a]
    print(path[::-1])