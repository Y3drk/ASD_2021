'''Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time),
przy czym są one posortowane niemalejąco według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów jest w stanie bezkonfliktowo obsłużyć te pociągi,
tzn. w żadnym momencie nie będzie “rywalizacji” pociągów o dostępne perony.
Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie.
'''

# prostsza implementacja - wolnieszy algorytm
# przemapowujemy tablice z arrivals i departures tak ze kazdy element nowej tablicy zawiera czas i znak czy oznacza on arrival czy departure
# sortujemy tablice najpierw po czasach potem po znakach, tak, ze arrival < departure (zakładamy, ze jednoczesny odjazd i przyjazd pociagu to nie kolizja)
# potem przechodzimy po tej tablicy i jesli trafiamy na arrival dodajemy do licznika, jesli na departure to odejmujemy.
# jesli w ktorymkolwiek momencie wartosc licznika przekroczy m to zwracamy false wpp zwracamy true
# złozonośc O(nlogn) czasowa i jesli O(n^2) pamieciowa, ale mozemy zakładac ze przemapowujemy wejscie


def trains_mapping(T,m):
    n = len(T)
    N = [[0,0] for i in range(2*n)]
    i, j = 0, 0
    while i < 2*n:
        N[i][0] = T[j][0]
        N[i][1] = 0
        i += 1
        N[i][0] = T[j][1]
        N[i][1] = -1
        j += 1
        i += 1

    # free (T)
    quick_sort_mem2(N,0,len(N) - 1)

    '''for elem in N:
        print(elem)'''

    n = len(N)
    counter = 0
    for i in range(n):
        if N[i][1] == 0:
            counter += 1
        else:
            counter -= 1

        if counter > m:
            return False

    return True


def partition_trains(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]    #dokonujemy wyboru losowego elementu i zamieniamy go z ostatnim elementem

    x_time = T[r][0]
    x_type = T[r][1]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < x_time:
            i += 1
            T[i], T[j] = T[j], T[i]
        elif T[j][0] == x_time:
            if T[j][1] <= x_type:
                i + 1
                T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_trains(T, p, r)
        if q - p <= r - q:   # zawsze wywołujemy quicksorta dla mniejszej czesci powstałej po podziale, a dla wiekszej czesci wracamy do poczatku pętli
            quick_sort_mem2(T, p, q - 1)
            p = q + 1 #i wywołujemy dla niej partition jeszcze raz

        else:
            quick_sort_mem2(T, q + 1, r)   #jak wyżej tylko tutaj mamy przypadek gdy prawa czesc jest mniejsza
            r = q - 1



# wersja trudniejsza, ale szybsza
# tworzymy kopiec min o maksymalnej długosci m
# bierzemy przedział i wrzucamy jego dep.time do kopca zachowujemy jego własnosci (zawsze wrzucamy nowy dep.time do kopca)
# jesli najwczesniejszy dep.time < arr.time aktualnego przedziału to go usuwamy
# jesli w dowolnym momencie wielkosc kopca przekroczy m zawracamy false, wpp. zwracamy true

#złożonośc O(nlogm)

def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2


def heapify_min(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] < T[m]:
        m = l
    if r < n and T[r] < T[m]:
        m = r

    if m != i:
        T[i],T[m] = T[m], T[i]
        heapify_min(T,n,m)


def buildheap_min(T):
    n = len(T)
    for i in range(parent(n - 1), - 1, -1):
        heapify_min(T,n,i)


def reverse_heapify_min(T, i):
    p = parent(i)
    m = i
    #print(p)
    if p >= 0 and T[p] > T[i]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_min(T,m)


def insert_to_heap_min(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_min(T,n -1)


def trains_hepified(T,m):
    n = len(T)
    H = [T[0][1]]

    for i in range(1,n):
        insert_to_heap_min(H,T[i][1])  #O(logm)
        if T[i][0] >= H[0]:
            H[0] = H[len(H) - 1]
            H.pop() #usuwamy element z konca O(1)
            heapify_min(H,len(H),0)
            # H = H[1:], slicing jednego elementu // można do tego napisac funkcje działającą w czasie O(m), wtedy oszczedzilibysmy pamiec
            # lub zamieniamy el. najmniejszy z ostatnim z kopca, robimy pop O(1) i odpalamy heapify log(m)
        #print("Aktualny kopiec:",H)

        if len(H) > m:
            return False

    return True


test1 = [(8,11),(9,12),(11,16),(13,17),(14,18),(17,21)]
print("Wersja mapujaca:",trains_mapping(test1,3))
print("wersja z kopcem:",trains_hepified(test1,3))
test2 = [(8,11),(9,12),(11,16),(12, 15),(13,17),(14,18),(17,21)]
print("Wersja mapujaca:",trains_mapping(test2,3))
print("wersja z kopcem:",trains_hepified(test2,3))