
def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2

#KOPIEC MINIMUM

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


def remove_min(min_heap):
    print(min_heap[0])
    min_heap[0] = min_heap[len(min_heap)-1]
    min_heap = min_heap[:-1]
    heapify_min(min_heap, len(min_heap),0)
    return min_heap


#KOPIEC MAXIMUM

def heapify_max(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] > T[m]:
        m = l
    if r < n and T[r] > T[m]:
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
    if p >= 0 and T[p] < T[i]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_max(T,m)


def insert_to_heap_max(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_max(T,n-1)


def remove_max(max_heap):
    print(max_heap[0])
    max_heap[0] = max_heap[len(max_heap)-1]
    max_heap = max_heap[:-1]
    heapify_max(max_heap, len(max_heap),0)
    return max_heap
