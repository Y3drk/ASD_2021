#from math import *

C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]

#komentarz
# dodamy do kazdego miasta w C dodatkowa komórke wystapien o wartosci 0 lub 1

# w funkcji get_solution bedziemy chcieli uzyskać tylko jedna, ze "ściezek" tę kończącą się w n - 1.

# gdy bierzemy miasto do sciezki w dodatkowej tablicy wpisujemy 1, wpp 0.

# w funkcji print solution wypisujemy najpierw elementy niewybrane do sciezki w ww. funkcji tworzac monotoniczna sciezke idącą w prawo
# a nastepnie wypisujemy od konca sciezke z get_solution otrzymujac monotoniczna sciezke idącą w lewo co daje cały cykl bitoniczny.

# złożoność:
# algorytm znajdywania rozwiązania wymusza złożoność czasową O(n^2) i  pamięciową O(2*n^2)
# natomiast algorytm wypisywania rozwiazania ma pesymistyczna złożoność czasową O(n^2) i dodatkową złożonosc pamieciową O(~2n), gdzie O(n) to dod. komórka w C
# potencjalnie drugie O(n) to scieżka z get_solution

#algorytm można próbowac optymalizować łaczac sąsiadujące przypadki (a) oraz sprytnie spisując elementy od k+1 do j-1 w przypadkach (b)
# ,ale u mnie prowadziło to do wielu błedów w przepisywaniu miast, wiec z tego zrezygnowałem.


def bitonicTSP( C ):

  def partition_random_cities(T, p, r):  # partition przystosowane do danych wejscia
    from random import randint
    rdm = randint(p, r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r][1]
    i = p - 1
    for j in range(p, r):
      if T[j][1] <= x:
        i += 1
        T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1

  def quick_sort_mem2(T, p, r):
    while p < r:
      q = partition_random_cities(T, p, r)
      if q - p <= r - q:
        quick_sort_mem2(T, p, q - 1)
        p = q + 1

      else:
        quick_sort_mem2(T, q + 1, r)
        r = q - 1

  def d(T, i, j):  # funkcja odległosci
    from math import sqrt
    if i != j:
      return sqrt((T[j][1] - T[i][1]) ** 2 + (T[j][2] - T[i][2]) ** 2)
    else:
      return 0

  def tsp_f(i, j, F, D):

    if F[i][j] != float('inf'):  # warunek brzegowy , który wskazuje ze juz wczesniej ta wartosc obliczalismy
      return F[i][j]

    if i == j - 1:  # pzypadek (b)
      best = float('inf')
      for k in range(j - 1):
        best = min(best, tsp_f(k, j - 1, F, D) + D[k][j])

      F[i][j] = best

    else:
      F[i][j] = tsp_f(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j]

  def TSP_Launcher(T):
    n = len(T)
    F = [[float('inf')] * n for _ in range(n)]
    D = [[0] * n for _ in range(n)]

    quick_sort_mem2(T, 0, n - 1)

    for i in range(n):
      for j in range(n):
        D[i][j] = d(T, i, j)

    F[0][1] = D[0][1]

    for p in range(n - 1):
      tsp_f(p, n - 1, F, D)

    res = float("inf")
    best = float("inf")
    for i in range(n - 1):
      if res > F[i][n - 1] + D[i][n - 1]:
        res = F[i][n - 1] + D[i][n - 1]
        best = i

    return res, F, D, best


  def get_solution(F, D, C, i, j, New, flag=True):
    # flaga True oznacza, że ind należy do scieżki kończącej się w n -1
    # flaga False oznacza przeciwny wypadek

    if i == 0 and j == 1:  # warunek brzegowy, cofnęliśmy się już do końca, "przeszliśmy" cała ścieżkę
      return New

    if i < j - 1:  #przypadek (a) z wykładu, ten łatwiejszy, oznaczający że elementy od i + 1 do j na pewno są w sciezce konczacej sie w j
      if flag:   #dlatego jesli jestesmy na interesujacej nas scieżce kończacej sie w n -1 (ozn. Sn) to mozemy dane elementy dodac
        New += [C[j - 1][0]] #dodajemy tylko jeden element bo jesli i << j -1 to w kolenym kroku sytuacja sie powtorzy i wykonamy ta sama operacje
        C[j - 1][3] = 1
        return get_solution(F, D, C, i, j - 1, New, flag)
      else:
        return get_solution(F, D, C, i, j - 1, New, flag)

    if i == j - 1: #przypadek (b) z wykładu, trudniejszy
      mini = float('inf')
      pointer = float('inf')
      for k in range(i):
        if F[k][i] + D[k][j] < mini:
          mini = F[k][i] + D[k][j]
          pointer = k    # k jest przedostatnim elementem w sciezce konczacej sie w j, co oznacza, ze wszystkie elementy od k +1 do j - 1 sa w sciezce konczaej sie w i

      if flag:
        return get_solution(F, D, C, pointer, j - 1, New, False)

      else:  #jesli jestesmy na sciezce która nas nie interesuje to mozemy elementy od k +1 do j - 1 dodac do Sn
        New += [C[j - 1][0]] #dodajemy tylko jeden element z tego samego powodu co w przypadku (a)
        C[j - 1][3] = 1
        return get_solution(F, D, C, pointer, j - 1, New, True)


  def print_solution(C, New):
    for i in range(len(C)):
      if C[i][3] != 1:
        print(C[i][0], end=', ')

    for elem in New:
      print(elem, end=', ')

    print(C[0][0])

    return

  score = TSP_Launcher(C)
  for i in range(len(C)):
    C[i] += [0]
  # print(C)
  New = [C[len(C) - 1][0]]
  C[len(C) - 1][3] = 1
  New1 = get_solution(score[1], score[2], C, score[3], len(C) - 1, New)
  print_solution(C, New1)

  print(score[0])

  return

bitonicTSP(C)
