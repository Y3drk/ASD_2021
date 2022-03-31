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


#TESTING
BST = BST_Tree()
print("Wstawianie")
print(insert(BST,10))
print(insert(BST,58))
print(insert(BST,131))
print(insert(BST,99))
print(insert(BST,17))
print(insert(BST,518))
print(insert(BST,375))
print(insert(BST,66))
print(insert(BST,131))
print(insert(BST,88))
print(insert(BST,8))
print(insert(BST,17))
print(in_order(BST.root,[]))
print("-----")

print("Wyszukiwanie")
print(find(BST.root,4))
print(find(BST.root,66))
print(find(BST.root,375))
print(find(BST.root,518))
print("-----")
print("find max i find min")
print(find_min(BST.root))
print(find_max(BST.root))
print("-----")
print("Usuwanie i potem sprawdzenie poprawnosc findem")
print(remove(BST,375))
print(in_order(BST.root,[]))
print(remove(BST,17))
print(in_order(BST.root,[]))
print(remove(BST,66))
print(in_order(BST.root,[]))
print(remove(BST,131))
print(in_order(BST.root,[]))
print(remove(BST,16))
print(in_order(BST.root,[]))
print(remove(BST,375))
print(in_order(BST.root,[]))
print(remove(BST,10))
print(in_order(BST.root,[]))

print(BST.root.key)
print(find(BST.root,58))
print(find(BST.root,66))
print(find(BST.root,88))
print(find(BST.root,99))




