from random import randint, shuffle, seed
#from time import time


def linearselect( A, k ):

  return quickselect_with_magic(A,0,len(A)-1,k)

# magic fives
'''Chcemy podzielic tablice na czesci 5cio elementowe. Z kazdej z nich wyciagnąc mediane (np.posortowac bo robimy to w czasie stałym O(5) i wziac el o ind 2) i zamieniac ja z elementem odp "indeksowi czesci" ,np. mediane pierwszej czesci zamienimy z T[0]
itd. Potem z tych median rekurencyjnie wyciagnac ich mediane i kontynuujemy jak w quickselectcie tylko używamy mediany median jako pivota.'''


def insertion_sort(T, beg, end):  # przyda nam się do sortowania "piątek" bo ma niską stałą, przystosujemy go do nich
    for i in range(beg + 1, end + 1):
        x = T[i]
        j = i - 1
        while j >= beg and x < T[j]:
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = x


def partition_magic(T, p, r,mm):  #standardowe partition tylko uzywajac mediany median jako pivota
    T[mm], T[r] = T[r], T[mm]
    x = T[r]
    i = p - 1

    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def magic_fives(T, beg, end):

  if beg == end:
    return T[beg]

  nr = beg
  pointer = beg

  for i in range(beg + 4, end + 1, 5):  # etap 1 i 2 naszego algorytmu z wykładu
    insertion_sort(T, i - 4, i)  # sortujemy nasze piatki w czasie stałym
    T[nr], T[i - 2] = T[i - 2], T[
      nr]  # zamieniamy znaleziona mediane z elementem na indeksie równym numerowi piatki (liczymy od 0)
    nr += 1  # zwiekszamy nr piatki
    pointer = i

  pointer += 1

  if pointer <= end:  # dodatkowy case gdy lizba elementów w tablicy jest niepodzielna przez 5

    l = end - pointer + 1
    med = (l - 1) // 2
    insertion_sort(T, pointer, end)
    T[nr], T[pointer + med] = T[pointer + med], T[nr]

  if (nr - beg) > 5:     #etap 3 z wykładu - jesli ilosc median jest wystarczająco mała to sortujemy ją w czasie stałym i wyciagamy nasza docelowa mediane median
    return magic_fives(T, beg, nr)    #w przeciwnym wypadku szukamy mediany wsród median i tak w kółko, aż do osiagniecia zadowalajacej ilosci

  insertion_sort(T, beg, nr)
  return (nr + beg) // 2


def quickselect_with_magic(T, beg, end, k):  #standardowy quickselect. Jedyne co to używamy znalezionej mediany median jako pivota w partition
  if beg == end:
    return T[beg]
  x = magic_fives(T, beg, end)
  q = partition_magic(T, beg, end, x)

  if q == k:
    return T[q]

  elif k < q:
    return quickselect_with_magic(T, beg, q - 1, k)

  else:
    return quickselect_with_magic(T, q + 1, end, k)


seed(42)

n = 11
#start = time()
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")
#stop = time()
#print(stop - start)
