from zad1_testy_33 import runtests

# idea - modyfikujemy algorytm dijkstry, jesli znajedziemy nowa najkrótsza sciezke sciezke do danego wierzchołka, to otrzymuje on ilosc najkrótszych sciezek
# taka sama jak rodzic (poza pierwszym krokiem, jest to specjalny case, warunek brzegowy)
# z kolei gdy znajdziemy kolejna najkrótsza sciezke do danego wierzchołka, to do ilosci sciezek juz w nim zapisanych dodajemy ilosc sciezek rodzica

# złozonosc - czasowa jak alg. dijkstry O(ElogV) pamieciowa O(V)


def FAST_sciezka(G,s): # lista sasiedztwa, punkt poczatkowy
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    how_many = [0 for _ in range(n)]

    Q.put((0, s))  # (waga, wierzchołek)
    distance[s] = 0
    how_many[s] = 0  #dla uproszczenia implementacji, skoro z dupy zaczynamy w tym wierzchołku to sposob jest tylko 1 - w testach jest inaczej i chuj mi na kurwe

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            if u == s:
                how_many[v] = 1 #specjalny case gdy wchodzimy gdzies pierwszy raz od startu
            else:
                how_many[v] = how_many[u] # gdy znajdujemy krótsza sciezkę, zamieniamy ilosc,bo siła rzeczy do tego wierzchołka prowadza nowe sciezki
            return True

        elif distance[v] == distance[u] + edge:
            how_many[v] += how_many[u]  #gdy znajdziemy kolejna taka sama najkrótsza sciezke do v , zwiekszamy ilosc o tyle ile najkrótszych sciezek dochodziło do u
            #ale nie potrzebujemy znowu wstawiac v do kolejki bo juz w niej jest z taka sama odlegloscia

        return False

    while not Q.empty():
        _, t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]:  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax(t, u[0], u[1]):
                        Q.put((distance[u[0]], u[0]))

    return how_many


test = [[(1,5),(2,2),(3,8)],[(3,3),(5,6)],[(1,3),(3,6),(4,3)],[(4,4),(5,3),(6,4)],[(0,1),(5,6),(6,8)],[(6,1)],[]]
print(FAST_sciezka(test,0))



runtests(FAST_sciezka)
