from copy import deepcopy


def min_cycle( G ):
  """miejsce na Twoją implementację!"""
    #idea -
    # A) ustaw mincost (koszt najtańszego cyklu) na nieskończoność,
    # zainicjuj pustą tablice C_parent, która w kroku (C), będzie słuzyła do wypisania znalezionego minimalnego cyklu
    # oraz pusta tablice best_edge, która zapamięta odpowiednią krawędź {u,v}
    # B) dla kazdej krawedzi wykonaj:
    # 1) "usuń krawędź" grafu {u,v}
    # 2) za pomocą algorytmu Dijkstry znajdź najkrótsza scieżkę z u do v nie uzywając ww. krawedzi jesli takowa istnieje
    # 3) jesli ww. scieżka istnieje sprawdź czy cykl skaładający się z tej ściezki + "usunietej" krawedzi jest "tańszy" (suma wag jest mniejsza) od przechowywanego minimalnego cyklu
    # jesli tak to dokonaj podmiany pól mincost, C_parent, best_edge
    # C) po przeanalizowaniu wszystkich krawędzi, na podstawie tablicy C_parent wypisz znaleziony cykl

    #złożoność -> pamięciowa O(V) - na tablice C_parent oraz tablice pomocnicze używane wewnętrznie w alg. Dijkstry + O(1) na pozostałe zmienne tj. mincost. Pamięć zużyta na reprezentacje wejscia pomijam, gdyż jest narzucona z zał.
    # -> czasowa - O(E*V^2) - ponieważ dla każdej krawędzi włączamy alg. Dijkstry, który w implementacji dla macierzowej repr. grafu ma zł. O(V^2)

  def Dijkstra_4_adjmatrix(G, s):  #z zastosowaniem tablicy jako kolejki dla macierzy sasiedztwa. Wg Cormena O(V^2 + E) ~= O(V^2)
      n = len(G)
      Queue = [float('inf') for _ in range(n)]
      processed = [False for _ in range(n)]
      parent = [None for _ in range(n)]
      distance = [float('inf') for _ in range(n)]  # niepotrzebne bo queue ~= distance de facto, ale zachowamy dla porzadku

      Queue[s] = 0
      distance[s] = 0

      def relax(u, v, edge):
          if distance[v] > distance[u] + edge:
              distance[v] = distance[u] + edge
              parent[v] = u
              return True  # przyda sie do wkładania wierzchołków do kolejki

          return False

      def get_vert():   #wyciagnięcie wierzchołka z kolejki O(V)
          n = len(Queue)
          key = n
          best = float('inf')
          for i in range(n):
              if not processed[i] and best > Queue[i]:
                  best = Queue[i]
                  key = i

          return key, best

      while True:
          v, flag = get_vert()
          if flag == float('inf'):  # warunek zakonczenia przetwarzania
              break

          else:
              processed[v] = True
              for u in range(n):
                  if G[v][u] != - 1 and not processed[u] and relax(v, u, G[v][u]):
                      Queue[u] = distance[u]

      return parent, distance


  def get_cycle(Parents, beg, end):
      Cycle = [end]

      while end != beg:
          Cycle += [Parents[end]]
          end = Parents[end]

      return Cycle

  n = len(G)
  mincost = float('inf')
  C_parent = []
  curr_edge = None
  best_edge = []

  for u in range(n):
      for v in range(u + 1, n): #aby nie analizować jednej krawędzi 2 razy, gdyż z zał. wynika, że graf jest nieskierowany
          if G[u][v] != -1:
              curr_edge = G[u][v]
              G[u][v] = -1  # "usuwanie krawędzi" (ofc potem ją przywrócimy *, stąd "")

              potential_C_p, distances = Dijkstra_4_adjmatrix(G,u)

              if distances[v] + curr_edge < mincost:
                  mincost = distances[v] + curr_edge
                  C_parent = potential_C_p
                  best_edge = [u,v]

              G[u][v] = curr_edge #(*)

  if len(C_parent) > 0:
      return get_cycle(C_parent,best_edge[0], best_edge[1])

  else:
      return []
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]


G3 = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],   #[5, 6, 8, 2]
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

G4 = [
[-1, 0, -1, -1],
[0, -1, 3, 2],
[-1, 3, -1, 1],
[-1, 2, 1, -1]
]

LEN = 7

GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
print(cycle[1:]+[u])
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
