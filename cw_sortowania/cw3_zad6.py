'''kolejne zadanie z bit Algo, przepisze tutaj ideę Pawła Pyci i sprobuje to zaimplementowac

Zad.6
Proszę przedstawić W jaki sposób zrealizować strukturę danych, która pozwala wykonywać
operacje:
1. Insert
2. RemoveMedian (wyciągnięcie mediany)
tak, żeby wszystkie operacje działały w czasie O(log n).

Idea - konstruujemy dwa kopce, MIN (gdzie zbieramy elementy wieksze od mediany) i MAX (gdzie zbieramy elementy mniejsze od mediany).
Musimy je balansowac, czyli róznica ich wielkości nie moze być większa niż 1. Jeśli po insercie w jednym z kopców jest więcej o 2 elementy to zabieramy z
niego korzeń i wstawiamy do drugiego kopca, po czym naprawiamy pierwszy z nich.
Medianę uzyskujemy zaleznie od liczby elementów:
1) jezeli jest parzysta to wyciągamy srednia arytmetyczną z dwóch korzeni kopców
2) jezeli jest nieparzysta to madianą jest wartosc korzenia z większego kopca.

'''


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


def remove_median(min_heap, max_heap):
    if len(min_heap) == len(max_heap) == 0:
        return "No median, heaps are empty", min_heap, max_heap
    if len(min_heap) == len(max_heap):
        median = (min_heap[0] + max_heap[0]) / 2
        min_heap = min_heap[1:]
        heapify_min(min_heap,len(min_heap),0)
        max_heap = max_heap[1:]
        heapify_max(max_heap,len(max_heap),0)
        return median, min_heap, max_heap
    elif len(min_heap) > len(max_heap):
        median = min_heap[0]
        min_heap = min_heap[1:]
        heapify_min(min_heap, len(min_heap), 0)
        return median, min_heap, max_heap
    else:
        median = max_heap[0]
        max_heap = max_heap[1:]
        heapify_max(max_heap, len(max_heap), 0)
        return median, min_heap, max_heap


def balance(min_heap, max_heap):
    if abs(len(min_heap) - len(max_heap)) <= 1:
        return min_heap, max_heap
    elif len(min_heap) > len(max_heap):
        print("w balance")
        print(min_heap)
        insert_to_heap_max(max_heap,min_heap[0])
        min_heap[0] = min_heap[len(min_heap)-1]  #dzieki takiemu naprawianiu na pewno sprawdzimy strukture kopca głebiej i nam sie nie rozsypie struktura
        min_heap = min_heap[:-1]
        heapify_min(min_heap,len(min_heap),0)
        print(min_heap)
        print(max_heap)
        return min_heap, max_heap
    else:
        insert_to_heap_min(min_heap,max_heap[0])
        max_heap[0] = max_heap[len(max_heap) - 1] # ^
        max_heap = max_heap[:-1]
        heapify_max(max_heap, len(max_heap),0)
        return min_heap, max_heap


def controller(T):
    min_heap, max_heap = [], []
    n = len(T)
    for i in range(n):
        if len(min_heap) == 0 or T[i] > min_heap[0]:
            insert_to_heap_min(min_heap,T[i])
        else:
            insert_to_heap_max(max_heap, T[i])

        print('before balance')
        print('min:', min_heap)
        print("max:", max_heap)
        min_heap, max_heap = balance(min_heap,max_heap)
        print("after balance")
        print('min:',min_heap)
        print("max:",max_heap)
        print(".....")


    print("-----")
    print('min:',min_heap)
    print("max:",max_heap)
    median, min_heap, max_heap = remove_median(min_heap,max_heap)
    print(median)
    print('min:',min_heap)
    print("max:",max_heap)

    return


test = [7,5,1,8,3,1,2,4,5,6,3,9]
controller(test)