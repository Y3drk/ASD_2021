'''Zadanie 1. (Indeksowane drzewa BST) Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają pole z liczbą węzłów w danym poddrzewie.
Proszę opisać jak w takim drzewie wykonywać
następujące operacje:
1. znalezienie i-go co do wielkości elementu,
2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
Proszę zaimplementować obie operacje.'''

class BST_Tree:
    def __init__(self):
        self.root = None
        #self.elements = []


class BSTNode:
    def __init__(self, key, elems):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.elems = elems


#dodawanie
def insert(Tree,key,elems):
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
    elem = BSTNode(key,elems)
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



# 2)wyznaczanie ktorym co do wielkosci w drzewie jest zadany wezel
# jesli wezeł ma lewe dziecko to dodajemy to do wartosci, potem...
# idziemy od wezła w góre, jesli przyszlismy po lewej krawedzi to znaczy ze juz wszystko co pod nami dodalismy, wpp musimy dodac to co było pod nami
# w lewym poddrzewie (bo przyszlismy z wiekszego, prawego)
def elems(node):
    count = 1
    visited = False
    while node.parent != None:
        if node.left != None and not visited:
            count += node.left.elems
        if node.parent.left == node:
            visited = True
        else:
            visited = False

        node = node.parent

    if node.left != None and not visited:
        count += node.left.elems

    return count


#brakuje podpunktu 1)
# zakładamy, że taki numer istnieje
def find_ity(root, i):
    num_high = root.elems
    num_low = 1
    node = root

    while (num_low + num_high)//2 != i: #and node != None:
        #print(node.key,i)
        #print((num_low + num_high) // 2)
        #print(num_low,num_high)
        if (num_low + num_high)//2 < i:
            #print("dupa")
            num_low = (num_high + num_low)//2 + 1
            node = node.right

        else:
            #print("hooy")
            num_high = (num_high + num_low)//2 - 1
            node = node.left

        #print("-----")
    return node



Tree = BST_Tree()
insert(Tree,8,15)
insert(Tree,4,7)
insert(Tree,12,7)
insert(Tree,2,3)
insert(Tree,6,3)
insert(Tree,1,1)
insert(Tree,3,1)
insert(Tree,5,1)
insert(Tree,7,1)
insert(Tree,10,3)
insert(Tree,14,3)
insert(Tree,9,1)
insert(Tree,11,1)
insert(Tree,13,1)
insert(Tree,15,1)

print(in_order(Tree.root,[]))
print("......")
print(find_ity(Tree.root,11).key)
print(find_ity(Tree.root,5).key)

