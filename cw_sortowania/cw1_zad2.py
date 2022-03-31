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


def create(tab):  #wersja z wartownikiem
    ll = insert(None, "Guardian")
    for i in range(len(tab)):
        ll = insert(ll, tab[i])

    return ll


def insert_sorted(wsk,x):
    p, prev = wsk.next, wsk
    while p != None and p.value < x.value:
        prev = p
        p = p.next

    prev.next = x
    x.next = p

    return wsk


def delete_maximum(wsk):
    maxi = -1
    maxi_next, maxi_prev = None, None
    p, prev = wsk.next, wsk
    while p != None:
        if p.value > maxi:
            maxi_prev, maxi_next = prev, p.next
            maxi = p.value

        prev = p
        p = p.next

    maxi_prev.next = maxi_next
    return wsk


'''tab = [2,3,4,5,6,7,9]
z1 = create(tab)
print_all(z1)
z1 = insert_sorted(z1, Node(8))
z1 = insert_sorted(z1, Node(88))
z1 = insert_sorted(z1, Node(1))'''
tab2 = [4,5,7,10,6,8]
z1 = create(tab2)
print_all(z1)
z1 = delete_maximum(z1)
print_all(z1)






