# ciche zał: graf nie spójny nie jest dwudzielny

# idea - korzystamy z Algorytmu BFS z drobnymi modyfikacjami
# "wrzucenie kamienia" nie daje nam zadnej kluczowej informacji, nic nie zmieniamy.
# dopiero potem możemy uzyskac informacje o braku dwudzielności grafu - jesli wierzchołki o tym samym parametrze d sa ze soba połaczone to graf nie jest dwudzielny
# dlaczego ? Wyobraźmy sb graf potencjalnie dwudzielny z wierzchołkami juz wstepnie uporzadkowanymi.
# Wrzucamy kamien po jednej stronie i fala rozchodzi sie na druga,
# jesli graf jest dwudzielny fala spokojnie przejdzie z powrotem na strone kamienia,
# ale jesli istnieją połączenia miedzy wierzchołkami z tej samej strony to dwudzielnosc sie psuje
# wiemy ze wierzchołki o tej samej parzystosci d na pewno sa po jednej stronie niezaleznie od konkretnej wartosci d,
# wiec sprawdzamy brak dwudzielnosci szukajac połaczeń między już odwiedzonymi wierzchołkami o tej samej parzystosci

#miejsce rozpoczecia nie ma znaczenia bo i tak chcemy przejsc po kazdym wierzchołku grafu


def if_bipartite(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)
    visited[s] = True
    distance[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:  #sprawdzamy wszystkich dotychczas nieodwiedzonych sasiadów wierzchołka sciagnietego z kolejki
            if not visited[v]: #jesli do tej pory tam nie dotarlismy to nie możemy o takim wierzchołku nic powiedziec, wiec normalnie go przetwarzamy
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

            elif distance[u] % 2 == distance[v] % 2: #połączone sa wierzchołki o tej samej parzystosci d, zatem graf nie moze byc dwudzielny
                return False

    for i in range(n):
        if visited[i] == False:  #specjalny case gdy graf nie jest spójny, zatem nie jest dwudzielny
            return False

    #jesli udało nam sie przejsc cały graf i nie odnaleźć połączenia psujacego dwudzielnosc to odp jest pozytywna
    return True



G1 = [[3,5],[3,4],[4],[0,1],[1,2],[0]]
print("test1:",if_bipartite(G1,0))
print("----")
G2 = [[3,5],[3,4,6],[4],[0,1,6],[1,2],[0],[1,3]]
print("test2:",if_bipartite(G2,0))
print("----")
G3arr = [[0, 0, 0, 0, 1],
     [0, 0, 1, 0, 1],
     [1, 0, 0, 0, 0],
     [0, 0, 1, 0, 1],
     [0, 1, 0, 1, 0]]

G3 = [[4],[2,4],[0],[2,4],[1,3]]
print("test3:",if_bipartite(G3,0))
print("----")

G4 = [[1, 3, 5], [0, 5], [4], [4, 0], [3, 2], [1, 0]]
print("test4:",if_bipartite(G4,0))
print("----")

G5 = [[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]
print("test5:",if_bipartite(G5,0))
print("----")