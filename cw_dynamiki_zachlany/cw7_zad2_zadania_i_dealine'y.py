'''Zadanie 2. (wybór zadań z terminami)
Mamy dany zbiór zadań T={t1, . . . , tn}.
Każde zadanietidodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie wterminie (liczba naturalna).
Wykonanie każdego zadania trwa jednostkę czasu.
Jeśli zadanietizostaniewykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti)(pierwsze wybrane zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.'''

# idea
# 1) sort zadan po deadline'ach
# 2) patrz od końca, wybieraj najwiekszy profit, gdy zadanie ma termin wiekszy od x

# dowód poprawnosci : jesli algorytm przynajmniej raz wybrał inaczej niz wskazuje rozw. optymalne
# 1) jesli danego przedziału nie ma w rozw. optymalnym to jest to ewidentna sprzecznosc
# 2) jesli jest to wybór rózni sie tylko kolejnoscia, która jest bez znaczenia


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random_sec_seed(T, p, r)
        if q - p <= r - q:   # zawsze wywołujemy quicksorta dla mniejszej czesci powstałej po podziale, a dla wiekszej czesci wracamy do poczatku pętli
            quick_sort_mem2(T, p, q - 1)
            p = q + 1 #i wywołujemy dla niej partition jeszcze raz

        else:
            quick_sort_mem2(T, q + 1, r)   #jak wyżej tylko tutaj mamy przypadek gdy prawa czesc jest mniejsza
            r = q - 1


def partition_random_sec_seed(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]    #dokonujemy wyboru losowego elementu i zamieniamy go z ostatnim elementem

    x = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][1] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def tasks_and_deadlines(T, i):
    n = len(T)
    Taken = []
    for j in range(n):   # przystosowanie danych
        T[j] = [T[j][0], T[j][1], False]

    quick_sort_mem2(T,0, n-1) # (1)
    #print(T)

    while i > 0:
        best = -1
        best_ind = n
        for j in range(n - 1, -1, -1):
            if T[j][1] < i:
                break
            elif T[j][0] > best and T[j][2] == False:
                best = T[j][0]
                best_ind = j

        if best_ind < n:
            Taken += [[T[best_ind][0],T[best_ind][1]]]
            T[best_ind][2] = True

        #print(Taken)
        i -= 1

    res = 0
    for k in range(len(Taken)):
        res += Taken[k][0]

    return res, Taken


T = [[1,1],[3,4],[2,1],[0,2],[6,8],[1,3],[0,3],[8,2],[1,4],[1,7]]
i = 4
result = tasks_and_deadlines(T,i)
print("Laczna nagorda za wykonane zadania:",result[0],"oraz wykonane zadania:",result[1])


#mozna mozliwe zadania wrzucac do kopca maximum i wyciagac najwieksze,  i wtedy jest O(nlogn)







