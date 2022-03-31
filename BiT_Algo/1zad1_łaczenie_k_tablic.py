'''Proszę zaproponować algorytm scalający k posortowanych tablic
w jedną posortowaną tablicę. Łączna liczba elementów we wszystkich tablicach wynosi n. Algorytm powinien działać w czasie O(n*log(k))'''
#załóżmy, że mamy jak daną tablice dwuwymiarową składającą się z k tablic jednowymiarowych

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
    if l < n and T[l][0] < T[m][0]:
        m = l
    if r < n and T[r][0] < T[m][0]:
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
    if p >= 0 and T[p][0] > T[i][0]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_min(T,m)


def insert_to_heap_min(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_min(T,n -1)


def merging(T):
    ind = [0 for _ in range(len(T))]
    k = len(T)
    min_heap = []
    res = []
    for i in range(k):
        min_heap += [(T[i][0], i)]
        ind[i] += 1
    buildheap_min(min_heap)

    while len(min_heap) > 0:
        #print(min_heap)
        res += [min_heap[0][0]]
        tmp = min_heap[0][1]   #indeks skad wzielismy
        min_heap = min_heap[1:]
        heapify_min(min_heap, len(min_heap), 0)
        if ind[tmp] < len(T[tmp]):
            insert_to_heap_min(min_heap,(T[tmp][ind[tmp]],tmp))
            ind[tmp] += 1

    return res


test = [[2,4,6,8],[1,3,5,7],[2,3,6,9,30],[6,9,10,13,14],[1,7,8,18,88]]
print(merging(test))
