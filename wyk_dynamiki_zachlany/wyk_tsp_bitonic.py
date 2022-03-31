"Bitoniczny problem komiwojażera - TSP bitonic"

# idea - skorzystamy z Funkcji f(i,j) =  minimalny koszt sciezek z 0 do j i z i do 0, takich, że łacznie te ścieżki odwiedzaja każde miasto ze zbioru
# {1,...,i,...,j} dokładnie raz (oprócz ofc miasta 0 bo je odwiedzamy dwa razy)
# ciche zał:
# 1) odległosci miedzy miastami sa wyrazone za pomoca metryki euklidesowej w przestrzenii R^2
# 2) współrzedne x'owe miast są parami różne
# 3) sciezka wyznaczana funkcja jest bitoniczna, czyli najpierw oddala sie od miasta 0 a potem ciagle do niego wraca.

# f(i,j) = (a) lub (b)

# (a) - gdy i < j - 1
# na pewno wiemy, ze miasto j - 1 musi nalezec do sciezki od 0 do j stad
# f(i,j) = f(i, j-1) + d(j-1,j) , gdzie d jest metyka euklidesowa

# (b) - gdy i = i - 1
# wtedy nie znamy naleznosci do sciezki punktu j-1 ani zadnego nastepnego, wiec musimy rozwazyc wszystkie opcje
# f(i,j) = min (po k od 1 do j - 2 włącznie) min { f(k, j-1) + d(k,j)}

# ogolna złożonosc O(n^2)

# aby dobrze realizowac zadanie musimy nasze miasta posorotowac wzgledem współrzednej x
# mozemy to zrobic quick sortem bo i tak zostanie on przykryty przez główny algorytm


def partition_random_cities(T, p, r): #partition przystosowane do danych wejscia
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][1] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random_cities(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


def d(T,i,j):   #funkcja odległosci
    from math import sqrt
    if i != j:
        return sqrt((T[j][1] - T[i][1])**2 + (T[j][2] - T[i][2])**2)
    else:
        return 0


def tsp_f(i,j,F,D):

    if F[i][j] != float('inf'): # warunek brzegowy , który wskazuje ze juz wczesniej ta wartosc obliczalismy
        return F[i][j]

    if i == j - 1:  #pzypadek (b)
        best = float('inf')
        for k in range(j -1):
            best = min(best, tsp_f(k, j - 1, F, D) + D[k][j])

        F[i][j] = best

    else:
        F[i][j] = tsp_f(i, j -1, F, D) + D[j-1][j]

    '''for row in F:
        print(row)
    print("----")'''

    return F[i][j]


def TSP_Bitonic(T):
    n = len(T)
    F = [[float('inf')]*n for _ in range(n)]
    D = [[0]* n for _ in range(n)]

    quick_sort_mem2(T,0, n-1)

    #print(C)

    for i in range(n):
        for j in range(n):
            D[i][j] = d(T,i,j)

    F[0][1] = D[0][1]

    '''for row in D:
        print(row)'''
    for p in range(n - 1):
        tsp_f(p, n-1, F, D)

    #print("----")
    #for row in F:
       #print(row)

    res = float("inf")
    best = float("inf")
    for i in range(n-1):
        if res > F[i][n -1] + D[i][n - 1]:
            res =  F[i][n -1] + D[i][n - 1]
            best = i

    return res, F, D, best

#ODZYSKIWANIE WYNIKU

def get_solution(F, D, C, i, j, New, flag=True):
    # w tej funkcji bedziemy chcieli uzyskać tylko jedna, ze "ściezek" tę kończącą się w n - 1
    # flaga True oznacza, że ind należy do scieżki kończącej się w n -1
    # flaga False oznacza przeciwny wypadek


    if i == 0 and j == 1:  # warunek brzegowy, cofnęliśmy się już do końca, "przeszliśmy" cała ścieżkę
      return New

    if i < j - 1:
      if flag:
        New += [C[j - 1][0]]
        C[j - 1][3] = 1
        return get_solution(F, D, C, i, j - 1, New, flag)
      else:
        return get_solution(F, D, C, i, j - 1, New, flag)

    if i == j - 1:
      mini = float('inf')
      pointer = float('inf')
      for k in range(i):
        if F[k][i] + D[k][j] < mini:
          mini = F[k][i] + D[k][j]
          pointer = k

      if flag:
        return get_solution(F, D, C, pointer, j - 1, New, False)

      else:
        New += [C[j - 1][0]]
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


C =  [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1],["Paprykarz",5,2]]
score = TSP_Bitonic(C)
print("----")
for i in range(len(C)):
    C[i] += [0]
#print(C)
print(score[0])
New = [C[len(C) - 1][0]]
C[len(C) - 1][3] = 1
New1 = get_solution(score[1], score[2],C,score[3], len(C) -1, New)
print_solution(C,New1)

C2 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]   # oczekiwane 15.236816791848371  -->A, E, C, B, D, F, A
score2 = TSP_Bitonic(C2)
print("----")
for i in range(len(C2)):
    C2[i] += [0]
#print(C2)
New = [C2[len(C2) - 1][0]]
C2[len(C2) - 1][3] = 1
print(score2[0])
New = get_solution(score2[1],score2[2],C2,score2[3],len(C2) - 1, New)
print_solution(C2,New)

C3 = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],['I', 0.5, 2.5], ['J', 1.5, 3.5]]
# oczekiwana długosc 18.705481427033437 i wynik A I J H D E G F C B A
score3 = TSP_Bitonic(C3)
print("----")
for i in range(len(C3)):
    C3[i] += [0]
#print(C3)
New2 = [C3[len(C3) - 1][0]]
C3[len(C3) - 1][3] = 1
print(score3[0])
New2 = get_solution(score3[1],score3[2],C3,score3[3],len(C3) - 1, New2)
print_solution(C3,New2)

#COS SIE PIEPRZY, ROZKIMINIC

C4 = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
# oczekiwana długosc i wynik 1 2 3 4 5 6 7 8 9 10 1
score4 = TSP_Bitonic(C4)
print("----")
for i in range(len(C4)):
    C4[i] += [0]
#print(C4)
New3 = [C4[len(C4) - 1][0]]
C4[len(C4) - 1][3] = 1
print(score4[0])
New3 = get_solution(score4[1],score4[2],C4,score4[3],len(C4) - 1, New3)
print_solution(C4,New3)

'''
C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Paprykarz", 5, 2]]
# oczekiwane 15.236816791848371  -->A, E, C, B, D, F, A

C2 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3],["F", 0.5, -2]]


C3 = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],['I', 0.5, 2.5], ['J', 1.5, 3.5]]
# oczekiwana długosc 18.705481427033437 i wynik A I J H D E G F C B A

C4 = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2],["9", 4, 3], ["10", 2, 3]]
# oczekiwana długosc i wynik 1 2 3 4 5 6 7 8 9 10 1

M1 = [["A",1,4],["B",2,7],["C",4,7],["D",6,7],["E",8,7],["I",10,3],["F",11,7],["H",13,3],["G",15,4]]
# A B C D E F G H I A

T3 = [[7, 12, -54], [6, 25, 13], [2, 37, 21], [3, 50, -18], [4, 53, -40], [1, 60, -56], [5, 77, 54], [0, 84, 75], [9, 93, 54], [8, 96, -57]]

bitonicTSP( C )
print("----")
bitonicTSP( C2 )
print("----")
bitonicTSP( C3 )
print("----")
bitonicTSP( C4 )
print("----")
bitonicTSP( M1 )
print("----")
bitonicTSP(T3)
'''