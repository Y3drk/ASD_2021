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

tab = [1,2,3,4]
z1 = create(tab)
print_all(z1)
