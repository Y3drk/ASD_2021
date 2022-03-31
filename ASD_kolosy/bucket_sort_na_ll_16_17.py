'''Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.'''

#bucket_sort na linklistach


class Node:
  def __init__(self):
    self.next = None
    self.value = None


def get_len(wsk):
    cnt = 0
    while wsk != None:
        cnt += 1
        wsk = wsk.next

    return cnt

def get_max(wsk):
    best = float('-inf')
    while wsk != None:
        best = max(best,wsk.value)
        wsk = wsk.next

    return best


def select_sort(T):            #do sortowania wewnątrz kubełków bucket sort uzywa innego sortowania. Cormen poleca select sorta wiec i ja go uzyje
    n = len(T)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if T[j].value < T[mini].value:
                mini = j

        T[mini], T[i] = T[i], T[mini]

    return T


def bucket_sort_ll(wsk):
    n = get_len(wsk)
    maxi = get_max(wsk)
    B = [[] for _ in range(n)]

    printlist(wsk)

    while wsk != None:
        holder = wsk
        wsk = wsk.next
        holder.next = None
        B[int(n*holder.value / (maxi + 1))].append(holder)

    '''for i in range(n):
        for j in range(len(B[i])):
            print(B[i][j].value, end=", ")
        print("next bucket")

    print("-----")'''
    for i in range(n):
        if len(B[i]) > 0:
            select_sort(B[i])

    '''for i in range(n):
        for j in range(len(B[i])):
            print(B[i][j].value, end=", ")
        print("next bucket")'''

    guardian = Node()
    pointer = guardian

    for i in range(n):
        if len(B[i]) > 0:
            for j in range(len(B[i])):
                pointer.next = B[i][j]
                pointer = B[i][j]

    return guardian.next


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


T0 = [0.06, 1.003, 7.61, 8.88, 3.21, 9.81, 4.20, 2.137, 6.96, 5.112, 2.115, 8.420, 9.09, 7.07, 1.21, 0.69, 4.47]
wsk0 = tab2list(T0)
res0 = bucket_sort_ll(wsk0)
printlist(res0)




