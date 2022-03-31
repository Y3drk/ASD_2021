'''Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie.
Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.
Podpowiedź. Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
(Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).'''

#jebac robimy zachłan z kopcem. tylko smartie, wrzucamy do kopca te pola które sa w zasiegu żaby, potem wyciagamy z kopca najwieksza wartosc i zwiekszamy zasieg

def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2


def heapify_max(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l][0] > T[m][0]:
        m = l
    if r < n and T[r][0] > T[m][0]:
        m = r

    if m != i:
        T[i],T[m] = T[m], T[i]
        heapify_max(T,n,m)


def buildheap_max(T):
    n = len(T)
    for i in range(parent(n - 1), - 1, -1):
        heapify_max(T,n,i)


def reverse_heapify_max(T, i):
    p = parent(i)
    m = i
    if p >= 0 and T[p][0] < T[i][0]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_max(T,m)


def insert_to_heap_max(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_max(T,n-1)


def remove_max(max_heap):
    res = max_heap[0]
    max_heap[0] = max_heap[len(max_heap)-1]
    max_heap.pop()
    heapify_max(max_heap, len(max_heap),0)
    return res,max_heap


def greedy_frog_zibi(A):
    jumps = 1
    leaves = [0]
    n = len(A)
    frog_range = A[0]
    Heap = []
    for i in range(1,min(frog_range+1,n)):
        insert_to_heap_max(Heap,(A[i],i))

    while len(Heap) > 0 and frog_range < n - 1: #logn - obsługa kopca
        tmp, Heap = remove_max(Heap)
        leaves += [tmp[1]]
        jumps += 1

        for i in range(frog_range + 1,min(frog_range + 1 + tmp[0],n)):  # po kazdym elemencie przejdziemy raz stad o(n)
            if A[i] > 0:
                insert_to_heap_max(Heap, (A[i], i))

        frog_range += tmp[0]

    if frog_range >= n - 1:
        leaves += [n-1]
        print(leaves)
        return jumps

    else:
        return -1


t1 = [2,2,1,0,0,0]
t2 = [4,5,2,4,1,2,1,0]
t3 = [2,1,0,1,4,2,3,1]
t4 = [2,3,0,0,0,0,0,0,0,0]
print(greedy_frog_zibi(t1))
print("----")
print(greedy_frog_zibi(t2))
print("----")
print(greedy_frog_zibi(t3))
print("----")
print(greedy_frog_zibi(t4))






