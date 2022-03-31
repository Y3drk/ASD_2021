class BST_Tree: # dodatkowa klasa, żeby było bardziej przejrzyście i mozna było gdzies przechowywac korzeń, oczywiscie mozna dodac inne pola, np. elements itd
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


#znajdywanie minimum
def find_min(root):
    while root.left is not None:
        root = root.left

    return root
