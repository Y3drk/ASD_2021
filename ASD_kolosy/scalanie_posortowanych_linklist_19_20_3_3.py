# skurwiałe zadanie z kurwa kopcem jebanym

# wrzucamy pierwszy element kazdej listy do kopca min, wyciagamy korzen i dodajemy do wynikowej listy,
# naprawiamy kopiec i dodajemy kolejny element z tej samej listy, z której przed chwila wyciagalismy korzen i tak az do wyczerpania wszystkich list

# złożonosc O(nlogk) gdzie n to ogolna liczba elementów, a k to liczba list na wejsciu

class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


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


def get_first(wsk):
    tmp = wsk
    wsk = wsk.next
    tmp.next = None
    return tmp, wsk


def integrate(T):
    L = []
    fucking_Heap = []
    Guardian = Node()
    New = Guardian
    pointer = Guardian

    for i in range(len(T)):
        tmp = tab2list(T[i])
        into, tmp = get_first(tmp)
        L += [tmp]
        fucking_Heap += [(into.value, into, i)]

    #print(L)
    buildheap_min(fucking_Heap)

    while len(fucking_Heap) != 0:          # O(nlogk) , wyciagnaie pierwszych elementów z list przyjmujemy za O(1), bo to tylko przepinanie wskazników
        _, tmp, ind = fucking_Heap[0]

        fucking_Heap[0], fucking_Heap[len(fucking_Heap)-1] = fucking_Heap[len(fucking_Heap)-1], fucking_Heap[0]
        fucking_Heap = fucking_Heap[:len(fucking_Heap) -1]
        heapify_min(fucking_Heap, len(fucking_Heap),0)

        pointer.next = tmp
        pointer = pointer.next

        if L[ind] != None:
            #print(L[ind])
            fresh, curr = get_first(L[ind])
            L[ind] = curr
            insert_to_heap_min(fucking_Heap,(fresh.value,fresh,ind))

    return New.next


test = [[0,1,2,4,5],[0,10,20],[3,5,8,15,25]]
res = integrate(test)
printlist(res)
















