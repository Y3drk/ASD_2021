class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


def insert(wsk,val):
    p, prev = wsk, None

    while p != None:
        prev = p
        p = p.next

    q = Node(val)

    if prev == None:
        q.next = p
        return q

    prev.next = q
    q.next = p
    return wsk


def print_all(p):
    while p != None:
        print(p.value,"-->", end = '')
        p = p.next

    print("|")


def create(tab):
    ll = insert(None, tab[0])
    for i in range(1,len(tab)):
        ll = insert(ll, tab[i])

    return ll


def series(first):
    tab = []
    q = first
    while q != None:
        tab += [q]  # wrzucamy liste do tablicy
        p = q
        while p.next != None and p.value <= p.next.value:  # przesuwamy sie tak długo jak trwa seria
            p = p.next
        w = p.next    #te 3 instrukcje przerywaja nam liste , ostatecznie ustalajac serie i pozwalajac nam pójsc dalej
        p.next = None
        q = w

    return tab


def scal(tab):
    n = len(tab)

    for i in range(n - 1):        #to scalanie jest n^2 de facto 
        tab[i + 1] = merge(tab[i], tab[i + 1])

    return tab[n - 1]



def merge(wsk1, wsk2):
    guardian = Node("!")
    pointer = guardian
    p1, p2 = wsk1, wsk2
    while p1 != None and p2 != None: # wazne nie musze za kazdym razem przewijac tej cholernej listy
                                        # no i pomysł dobry tylko musze ogarnac mozg z listami
        if p1.value <= p2.value:
            pointer.next = p1
            p1 = p1.next

        else:
            pointer.next = p2
            p2 = p2.next

        pointer = pointer.next

    if p1 is not None:
        pointer.next = p1

    if p2 is not None:
        pointer.next = p2

    return guardian.next


tab = [1, 5, 2, 3, 8, 10, 4, 2, 7, 5, 8, 9, 1]
z1 = create(tab)
print_all(z1)
print('----')
tmp = series(z1)
for i in range(len(tmp)):
    print_all(tmp[i])
print("----")
z3 = scal_better(tmp)
print_all(z3)
