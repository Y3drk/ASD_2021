'''. Dane są następujące struktury:
struct Node { Node* next; int val; };
struct TwoLists { Node* even; Node* odd; };
Napisać funkcję: TwoLists split(Node* list);
Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
nieparzyste. Listy nie zawierają wartowników.
'''

# Złożonosc O(n)

# idea - przechodzac raz po liscie przepinamy liczby do nowych list w zaleznosci od ich %2. Dwie wynikowe listy zwracamy

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

'''class TwoLists:
    def __init__(self):
        self.even = None
        self.odd = None'''


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


def split(wsk):
    pointer_odd, pointer_even = None, None
    p, r = wsk, wsk.next

    while p != None:
        if p.value % 2 == 0:
            p.next = pointer_even
            pointer_even = p
            p = r
            if r != None:
                r = r.next

        else:
            p.next = pointer_odd
            pointer_odd = p
            p = r
            if r != None:
                r = r.next

        '''print_all(pointer_odd)
        print_all(pointer_even)
        print("----")'''

    return pointer_odd, pointer_even


test = [1,3,5,7]
z1 = create(test)
print("wyjsciowa")
print_all(z1)
z_odd, z_even = split(z1)
print("nieparzyste")
print_all(z_odd)
print("parzyste")
print_all(z_even)

#[1,2,3,4,5,6,7,8]
#[1,2,4,5,6,7,8, 9, 11]

#wydaje sie działać