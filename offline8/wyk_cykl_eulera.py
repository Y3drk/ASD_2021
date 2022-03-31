from copy import deepcopy


def euler( G ):
  """miejsce na Twoją implementację!"""
  n = len(G)
  Cycle = []
  #sprawdzenie czy graf spełnia wkw na istnienie cyklu eulera
  for v1 in range(n):
      counter = 0
      for v2 in range(n):
          if G[v1][v2] == 1:
              counter += 1

      if counter % 2 == 1:
          return None

  previous = [0] * n #proba zawalczenia ze złożonościa O(n^3)... tablica, ktora dla kazdego wierzchołka przechowuje gdzie z niego poszliśmy ostatnim razem
  # Co to daje? Dzięki temu zabiegowi, niezaleznie od tego ile razy odwiedzimy dany wierzchołek, przejdziemy po wszystkich jego krawedziach tylko raz, zamiast potencjalne n-1 razy.
  #stad nawet w pesymistycznym przypadku (graf pełny), gdy odwiedzamy kazdy wierzchołek n-1 razy (ergo DFS visit wewnatrz funkcji wywołamy ~n^2 razy),
  # to dzieki zastosowanemu rozwiazaniu złozonośc wyniesie O(n^2), gdzie n = |V|.

  # algorytm DFS usuwajacy krawedzie, po których przeszedł, jak z wykładu
  def DFS_visit(G, s):
      nonlocal Cycle
      for e in range(previous[s],n):
          if G[s][e] == 1:
              G[s][e], G[e][s] = 8, 8  #8 oznacza usunieta krawędź
              previous[s] = e + 1
              DFS_visit(G, e)

      Cycle += [s]
      return

  DFS_visit(G,0) #ponieważ graf jest spojny wystarczy wywołac DFS raz

  #przywrócenie macierzy reprezentujacej graf do stanu pierwotego
  for i in range(n):
      for j in range(n):
          if G[i][j] == 8:
              G[i][j] = 1

  return Cycle


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")