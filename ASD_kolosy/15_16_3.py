'''Dana jest struktura Node opisująca listę jednokierunkową:
struct Node { Node * next; int value; };
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej.'''

# idea -
# 1) przechodzimy po otrzymanej liscie i szukamy tego "specjalnego" węzła, sprawdzajac warunki (jesli oczywiscie sa mozliwe - nie sprawdzamy prev dla pierwszego wezla i next dla
# ostatniego) current.value < prev.value i current.value > next.value  -> O(n)
# 2) znalezionego "specjalnego" node'a wypinamy -> O(1)
# 3) idac po liscie od poczatku szukamy miejsca na nasza "perełkę" -> O(n)
# 4) umieszczamy ww. element w opowiednim miejscu -> O(n) (ale osobno)

# Zlożonosc - O(n)


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


def fix_sorted_list(wsk):
    prev1, curr = None, wsk
    special = None

    while curr != None:   #kroki (1) i (2)

        if prev1 == None and curr.value > curr.next.value:  #specjalny case gdy perełką jest pierwszy element
            special = curr
            wsk = curr.next
            special.next = None
            break


        if prev1 != None and prev1.value > curr.value:
            special = curr
            prev1.next = curr.next
            special.next = None
            break

        if curr.next != None and prev1 != None and prev1.value <= curr.next.value < curr.value:
            special = curr
            prev1.next = curr.next
            special.next = None
            break

        prev1 = curr
        curr = curr.next

    prev2, p = None, wsk

    #print(special.value)
    while p != None and p.value <= special.value: #krok (3)
        prev2 = p
        p = p.next

    if prev2 == None: #gdy musimy wstawic perełke na poczatek
        #print("wst1")
        special.next = wsk
        return special

    #print("wst2")
    prev2.next = special
    special.next = p

    return wsk


test1 = [30,2,3,5,7,11,13,17]
test2 = [2,3,5,7,11,13,17,0]
test3 = [2,3,5,7,11,16,13,17]
test4 = [2,3,5,1,7,11,13,17]
print("test1")
z1 = tab2list(test1)
printlist(z1)
z1 = fix_sorted_list(z1)
printlist(z1)
print("----")
print("test2")
z2 = tab2list(test2)
printlist(z2)
z2 = fix_sorted_list(z2)
printlist(z2)
print("----")
print("test3")
z3 = tab2list(test3)
printlist(z3)
z3 = fix_sorted_list(z3)
printlist(z3)
print("----")
print("test4")
z4 = tab2list(test4)
printlist(z4)
z4 = fix_sorted_list(z4)
printlist(z4)



