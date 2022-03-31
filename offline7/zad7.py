#from queue import PriorityQueue
#posługuje się kopcem minimum, który w mojej implementacji pełni role kolejki priorytetowej,
# ponieważ chciałem kombinowac ze zmienianiem metod porównywania we wbudowanej PriorityQueue, co było mi potrzebne w moim rozwiazaniu

# idea - korzystając z algorytmu podanego na wykładzie i rozdziału Kody Huffmana z Cormena tworzę drzewo prefiksowe, wykorzystujac przy tym kolejke priorytetowa (funkcja make_tree)
# nastepnie odpowiednio przechodzac po drzewie generuje kody prefiksowe dla okreslonych symboli (funkcja get_code)
# na koniec wypisuje wygenerowane kody i obliczam ile bitów potrzebne jest do zapisania stringa po zastosowaniu algorytmu Huffmana (odp. funkcje print_codes i print_new_size)

# złożonosc :

# (1) - budowanie drzewa - f. make_tree --> f. buildheap = O(n) (udowodnione na wykładzie) , f. insert_to_heap_min = O(logn) ze wzgledu na wewnetrzne wywołanie reverse heapify
# Wiemy, że aby utworzyc odpowiednie drzewo dla n elementów bedziemy musieli wykonac n-1 "połączeń" i w kazdym z nich wykonac operacje get_min i insert...
# zatem ostateczna zlozonosc make_tree to O(nlogn)

# (2) - tworzenie kodów - f. get_code --> ze względu na charakterystykę drzewa każdy węzeł zotanie odwiedzony dokładnie raz --> O(T), gdzie T jest rozmiarem drzewa, ~O(n^2)

# (3) wypisywanie kodów - f. print_codes -->  O(n* max(długosc kodu dla jednego symbolu)) - zatem pesymistyczne O(n^2)

# (4) wypisywanie nowego kosztu zapisu napisu - f. print_new_size --> O(n) (zał: operacja len to koszt O(1) źródło : ics.uci.edu, Complexity of Python Operations))

# ostatecznie cała złożonośc jest przykrywana przez wypisywanie kodów zatem całość to koszt O(n^2)

# złożoność: pamięciowa --> ~O(3*n) (zał: węzeł zajmuje stała ilość pamięci), na wezły w drzewie, i przechowywanie powstałych kodów

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]


def huffman( S, F ):
  """miejsce na Twoją implementację!"""

  class Node:
    def __init__(self, freq=None, name=None):
      self.left = None
      self.right = None
      self.freq = freq
      self.name = name

  def left(i):
    return 2 * i + 1

  def right(i):
    return 2 * i + 2

  def parent(i):
    return (i - 1) // 2

  def heapify_min(T, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l][0] < T[m][0]:
      m = l
    if r < n and T[r][0] < T[m][0]:
      m = r

    if m != i:
      T[i], T[m] = T[m], T[i]
      heapify_min(T, n, m)

  def buildheap_min(T):
    n = len(T)
    for i in range(parent(n - 1), - 1, -1):
      heapify_min(T, n, i)

  def reverse_heapify_min(T, i):
    p = parent(i)
    m = i
    # print(p)
    if p >= 0 and T[p][0] > T[i][0]:
      m = p

    if m != i:
      T[m], T[i] = T[i], T[m]
      reverse_heapify_min(T, m)

  def insert_to_heap_min(T, el):
    T += [el]
    n = len(T)
    reverse_heapify_min(T, n - 1)

  def get_min(T):  # O(logn) - wyciaganie pierwszego elementu, zamiania i usuwanie ostatniego to operacje w czasie stały, heapify kosztuje nas O(logn)
    item = T[0]
    T[0], T[len(T) - 1] = T[len(T) - 1], T[0]
    T.pop()  # usuwamy element z konca -> O(1)
    heapify_min(T, len(T), 0)
    return item

  def make_tree(F, S):
    n = len(F)
    Q = []
    for i in range(n):
      new_item = Node(F[i], S[i])
      Q += [(F[i], new_item)]

    buildheap_min(Q)

    for i in range(n - 1):
      new_node = Node()
      freq_r, new_node.right = get_min(Q)
      freq_l, new_node.left = get_min(Q)
      new_node.freq = freq_l + freq_r
      insert_to_heap_min(Q, (new_node.freq, new_node))

    return get_min(Q)

  def get_code(v, S, tmp=[]):
    if v.name != None:
      for i in range(len(S)):
        if v.name == S[i][0]:
          S[i][1] = tmp
          return

    return get_code(v.left, S, tmp + [0]), get_code(v.right, S, tmp + [1])


  def print_codes(S):
    n = len(S)
    for i in range(n):
      print(S[i][0], ":", end=" ")
      for j in range(len(S[i][1])):
        print(S[i][1][j], end='')
      print()

    return

  def print_new_size(S, F):
    n = len(S)
    res = 0
    for i in range(n):
      res += len(S[i][1]) * F[i]

    print("dlugosc napisu:", res)
    return

  _, root = make_tree(F, S)

  for i in range(len(S)):
    S[i] = [S[i], 0]

  get_code(root, S)
  print_codes(S)
  print_new_size(S, F)

  pass
  
  
  
huffman( S, F )
