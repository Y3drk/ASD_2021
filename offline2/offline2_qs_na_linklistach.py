from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    

def qsort( L ):
  #print("Tu proszę napisać swoją funckję")
  '''Ogólny pomysł jest taki, że pracujemy cały czas na jednej liście i tylko odpowiednio przesuwamy wskaźniki, aby działać na coraz mniejszych jej fragmentach.
  W partition wydzielamy ten fragment listy na którym bedziemy działać. Rozdzielamy go na 3 fragmenty: mniejszy, równy i większy.
  Z nich zczytujemy wskazniki na dwa kolejne fragmenty listy, którymi zajmiemy się w nastepnym wywołaniu rekurencyjnym.
  Na koniec działania partition scalamy wszystkie fragmnety w odpowiedniej kolejnosci. Jeśli znalezione fragmenty spełniają założenia, czyli
  nie są jednym elementem oraz nie są puste (w implementacji jako None) to wywołujemy dla nich funkcje.
  Dodatkowy while w funkcji partition wynika właśnie z potrzeby wydzielenia pożądanego fragmentu tablicy. Jednak nie jest zagnieżdzony więc dodaje nam maksymalnie
  + n - 2 do złożoności, więc (mam nadzieje, że się nie mylę) funkcja partition powinna działać w czasie O(n - 2 + n) czyli liniowym O(n), zatem
  opierajac sie na wiedzy z wykładu cały algorytm powinien działac w czasie O(nlogn) '''
  
  def find_end(L):
    while L.next is not None:
      L = L.next
    return L
  
  def quicksort_ll(start,beg,end):
    #print("-----")
    #printlist(start)
    new_start, new_beg_ls,new_end_ls, new_beg_bg, new_end_bg = new_partition(start,beg,end)

    if new_beg_ls != None and new_end_ls != None and new_end_ls != new_beg_ls:
      #print("beng")
      new_start = quicksort_ll(new_start,new_beg_ls,new_end_ls)

    if new_beg_bg != None and new_end_bg != None and new_end_bg != new_beg_bg:
      #print("bonk")
      new_start = quicksort_ll(new_start,new_beg_bg,new_end_bg)

    return new_start


  def new_partition(start, beg, end):
    new_beg_ls, new_end_ls, new_beg_bg, new_end_bg = None, None, None, None
    holder_t = end.next
    end.next = None
    holder_h = None
    #printlist(holder_t)
    #print("start", start.value)
    if start != beg:
      holder_h = start
      while start.next != beg:
        start = start.next

      start.next = None
      #printlist(holder_h)

    # odcielismy wszystko co nas nie interesuje, mozemy pracowac na naszej liscie docelowej
    pivot = end.value
    pointer = beg
    g_ls, g_eq, g_bg = Node(), Node(), Node()
    g_ls.value, g_eq.value, g_bg.value = "less", "equal", "bigger"
    ls, eq, bg = g_ls, g_eq, g_bg
    while pointer.value != None and pointer != end:  # przepinanie do odp list wg wartosci wzgledem pivota
      if pointer.value > pivot:
        bg.next = pointer
        bg = bg.next
      elif pointer.value < pivot:
        ls.next = pointer
        ls = ls.next
      else:
        eq.next = pointer
        eq = eq.next

      if pointer.next != None:
        pointer = pointer.next
      else:
        break

    eq.next = end  # przepiecie pivota do equal
    eq = eq.next
    ls.next, eq.next, bg.next = None, None, None  # uciecie pivota ze wszystkich list, zeby był tylko tam gdzie powinien

    '''printlist(g_ls)
    printlist(g_eq)
    printlist(g_bg)'''

    if g_ls.next == None:
      new_beg_ls = None
      new_end_ls = None
    else:
      new_beg_ls = g_ls.next
      new_end_ls = ls

    if g_bg.next == None:
      new_beg_bg = None
      new_end_bg = None
    else:
      new_beg_bg = g_bg.next
      new_end_bg = bg

    # połączenie wszystkiego z powrotem do kupy
    beg = g_ls
    ls.next = g_eq.next
    if g_bg.next != None:
      eq.next = g_bg.next
      bg.next = holder_t
    else:
      eq.next = holder_t
    beg = beg.next

    if holder_h != None:
      start.next = beg
      return holder_h, new_beg_ls, new_end_ls, new_beg_bg, new_end_bg

    return beg, new_beg_ls, new_end_ls, new_beg_bg, new_end_bg


  end = find_end(L)
  L = quicksort_ll(L,L,end)
  return L


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(42)

n = 100
T = [ randint(1,10) for i in range(n) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

