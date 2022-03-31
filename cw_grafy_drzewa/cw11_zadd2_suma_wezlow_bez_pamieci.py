'''Zadanie 2. Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości w drzewie binarnym
zdefiniowanym na węzłach typu:
class BNode:
def __init__( self, value ):
self.left = None
self.right = None
self.parent = None
self.value = val
Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę drzewa, pod
warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)
'''

class BST_Tree:
    def __init__(self):
        self.root = None
        #self.elements = []


class BST_Node:
    def __init__(self,key,value=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.value = None

#złożoność obu procedur jest liniowa wzgledem wysokości drzewa (O(h)), zatem jest silnie zależna od odpowiedniego jego balansowania

#dodawanie
def insert(Tree,key):
    y = None
    x = Tree.root

    while x != None:
        y = x
        if key < x.key:
            x = x.left
        elif key > x.key:
            x = x.right
        else: #przypadek gdy węzeł o danym kluczu już jest w drzewie
            return False

    # "przypięcie" nowego elementu do jego rodzica
    elem = BST_Node(key)
    elem.parent = y

    # odpowiednie przypisanie nowego elementu w jego rodzicu
    if y == None:
        Tree.root = elem

    elif elem.key < y.key:
        y.left = elem

    else:
        y.right = elem

    return True


#usuwanie
def remove(Tree,key):

    def transplant(Tree,u,v): #procedura odpowiednio przepinająca węzły
        if u.parent == None:
            Tree.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent

    #gdy danego klucza nie ma w drzewie
    elem = find(Tree.root,key)
    if elem == None:
        return False

    else:
        if elem.left == None:
            transplant(Tree,elem, elem.right)

        elif elem.left == None:
            transplant(Tree,elem, elem.left)

        else:
            next = find_min(elem.right)
            if next.parent != elem:
                transplant(Tree,next, next.right)
                next.right = elem.right
                next.right.parent = next

            transplant(Tree,elem,next)
            next.left = elem.left
            next.left.parent = next

    return True


#znajdywanie
def find(node,key):
    while node != None:

        if node.key == key:
            return node

        elif node.key > key:
            node = node.left

        else:
            node = node.right

    return None


#znajdywanie maximum
def find_max(root):
    while root.right is not None:
        root = root.right

    return root


#znajdywanie minimum
def find_min(root):
    while root.left is not None:
        root = root.left

    return root

#cw11_zad_obw1

#znajdywanie poprzednika
def find_prev(node):
    if node.left is not None:
        node = node.left
        return find_max(node)

    else:
        upper = node.parent
        while upper != None and node == upper.left: #dopóki nie przejdziemy pierwszy raz po prawej gałezi idziemy w góre, albo nie dojdziemy do roota
            node = upper
            upper = upper.parent

        return upper


#znajdywanie nastepnika
def find_next(node):
    if node.right is not None:
        node = node.right
        return find_min(node)

    else:
        upper = node.parent
        while upper != None and node == upper.right:  # dopóki nie przejdziemy pierwszy raz po lewej gałezi idziemy w góre
            node = upper
            upper = upper.parent

        return upper


def in_order(node,tmp):
    if node.left != None:
        in_order(node.left,tmp)
    tmp.append(node.key)
    if node.right != None:
        in_order(node.right, tmp)

    return tmp


# jako wartosci traktujemy klucze, smigniemy sb iteracyjnie po drzewie, dodajac do jednej zmiennej cnt
#złożonosc bedzie dosyc słaba bo nlogn dla zbalansowanego drzewa, ale za to pamiec O(1)

def count_all(root):
    cnt = 0
    node = find_min(root)

    while node != None:
        #print(node.key,cnt)
        cnt += node.key
        node = find_next(node)

    return cnt


Tree = BST_Tree()
insert(Tree,8)
insert(Tree,4)
insert(Tree,12)
insert(Tree,2)
insert(Tree,6)
insert(Tree,1)
insert(Tree,3)
insert(Tree,5)
insert(Tree,7)
insert(Tree,10)
insert(Tree,14)
insert(Tree,9)
insert(Tree,11)
insert(Tree,13)
insert(Tree,15)

print(in_order(Tree.root,[]))
print("......")
print(count_all(Tree.root))
