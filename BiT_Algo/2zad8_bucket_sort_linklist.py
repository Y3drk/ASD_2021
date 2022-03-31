'''Dana jest klasa :
class Node:
	val = 0
	next = None
reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val poszczególnych węzłów zostały wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a, b].
Napisz procedurę sort(first), która sortuje taką listę. Funkcja powinna być jak najszybsza.
'''


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


def find_end(L):
    while L.next is not None:
        L = L.next
    return L


def insert_sort_ll(wsk): #O(n^2) - w załozeniu bucket_sorta dostaje tak małe dane, że sortuje w czasie stałym
    guardian = Node()
    guardian.value = "!"
    guardian.next = wsk
    pointer = wsk.next
    guardian.next.next = None
    #printlist(guardian)
    #printlist(pointer)

    while pointer != None:
        prev_l = guardian
        looker = guardian.next
        current = pointer
        pointer = pointer.next
        current.next = None
        '''print("wynikowa:")
        printlist(looker)
        print("sortowany element:")
        printlist(current)
        print("Co zostało:")
        printlist(pointer)'''

        while looker != None and looker.value <= current.value:
            #print("1")
            prev_l = looker
            looker = looker.next

        if looker == None:
            #print("end 1")
            prev_l.next = current
        else:
            #print("end 2")
            current.next = looker
            prev_l.next = current



        #print("----")
        #printlist(guardian)

    return guardian.next


def get_len(wsk):
    cnt = 0
    p = wsk
    while p != None:
        p = p.next
        cnt += 1

    return cnt


def bucket_sort_ll(wsk,mini,maxi):
    n = get_len(wsk)

    if n == 0 or n == 1:
        return wsk

    Buckets = [Node() for _ in range(n)]
    Heads = [Buckets[i] for i in range(n)]
    '''for i in range(n):
        Heads[i] = Buckets[i]'''

    #print(Buckets)

    #b_interval = (maxi - mini) / n
    p = wsk
    while p != None:
        current = p
        p = p.next
        current.next = None
        #print(current.value)
        #printlist(p)
        Buckets[int(n * (current.value - mini) / (maxi - mini + 1))].next = current
        Buckets[int(n * (current.value - mini) / (maxi - mini + 1))] = Buckets[int(n * (current.value - mini) / (maxi - mini + 1))].next
        #printlist(Buckets[int(n * current.value / (maxi + 1))])
        #print("----")

    '''for i in range(n):
        printlist(Heads[i])

    print("----")'''

    for i in range(n):
        if Heads[i].next != None:
            Heads[i] = insert_sort_ll(Heads[i].next)

    '''for i in range(n):
        printlist(Heads[i])



    print("-----")'''

    guardian = Node()
    guardian.value = "chuj"
    pointer = guardian
    for i in range(n):
        if Heads[i].value != None:
            pointer.next = Heads[i]
            pointer = find_end(Heads[i])  # czas działania funkcji O(n) , czy mozemy załozyc ze wewnatrz bucketu stały ?


    #printlist(guardian)

    return guardian.next


from random import randint
n = int(input("Podaj ilosc el: "))
a = int(input("Podaj wartosc min:"))
b = int(input("Podaj wartosc max:"))
test = [randint(a,b) for i in range(n)]
print(test)
z1 = tab2list(test)
#z1 = insert_sort_ll(z1)
#printlist(z1)
#print(get_len(z1))
z1 = bucket_sort_ll(z1,a,b)
printlist(z1)

'''test_spec = []
z2 = tab2list(test_spec)
z2 = bucket_sort_ll(z2,1,1)
printlist(z2)'''