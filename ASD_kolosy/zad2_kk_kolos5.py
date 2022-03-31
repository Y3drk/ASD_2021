#ZROBILEM TO WCZESNIEJSZA WERSJE Z PRZECIECIEM BO NIE WIEDZIALEM ZE SA ZMIANY XD , be merciful please

#TESTY SIE NAWET NIE OPALAJA I NIKT NIE WIE CZEMU (NAWET ŁUKASZ) WIEC SPOJRZ KTOS NA KOD ŁADNIE PROSZE

#pomysł (chuj w to ze moze nieefektywny)
# A) przechodzimy po drzewach i zliczamy ilosc ich elementów O(km) m = srednia ilosc elementów w drzewie
# B) obieramy najmniejsze (w sensie licznosci elementów) z drzew za nasze wynikowe,
# C) wykonujemy nastepujacą sekwencje, dopóki nie trafimy na None:
# 1) w kroku pierwszym znajdujemy minimum, potem nastepnika wczesniejszego wezła O(h)
# 2) w pozostałych drzewach szukamy zadanego klucza O(kh)
# 3) jesli jest on we wszystkich drzewach to zostawiamy go w swietym spokoju i przechodzimy do instrukcji 1),
# wpp usuwamy wierzchołek wczesniej znajdujac jego nastepnika i siła rzeczy przechodzimy do kroku 2 (pamietajac o weryfikacji czy found_next != None)

# Nigdy nie dodamy nic do drzewa, będziemy co najwyżej usuwac
# Nie zuzywamy zadnej pamieci ponad stałe na flagi,holdery itd oraz pamiec potrzebna do przechowywania wejscia
# O balansowaniu powstałego drzewa wiemy tyle, ze bez rotacji i innych chujów mujów jest losowa. Nawet jesli wejsciowe drzewo jest zbalansowane to
# usuwajac mozemy dostac jedna sciezke i chuj nam na łeb.

# czas działania całosci to O(nkh + km) gdzie:
# m = srednia ilosc elementów w drzewie
# n = liczba elementów w najmniejsyzm drzewie
# k = liczba drzew
# h = srednia wysokosc drzewa, mozna ja równiez oszacowac jako O(logn) wtedy całosc to O(knlogn + km)


class Tree:
    def __init__(self,root=None):
        self.root = root

    def insert(self, val):
        y = None
        x = self.root

        while x != None:
            y = x
            if val < x.val:
                x = x.left
            elif val > x.val:
                x = x.right

        #liczymy ze mam mózg i nie dodam dwa razy tego samego
        elem = BSTNode(val)
        elem.parent = y

        if y == None:
            Tree.root = elem

        elif elem.val < y.val:
            y.left = elem

        else:
            y.right = elem


class BSTNode:
    def __init__(self,val=0):
        self.val  = val
        self.parent = None
        self.left = None
        self.right = None
        # mozna dopisywac itp itd


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
        while upper != None and node == upper.right:
            node = upper
            upper = upper.parent

        return upper


def in_order(node, cnt):
    if node.left != None:
        in_order(node.left, cnt)
    cnt += 1
    if node.right != None:
        in_order(node.right, cnt)

    return cnt


def drzewa_jakies(tab) -> Tree:
    mini = float('inf')
    mini_tree = None
    for T in tab: #(A)
        print(T.root) #(???)
        tmp = in_order(T.root,0)
        if mini > tmp:
            mini = tmp
            mini_tree = T #(B)

    # (C)
    flag = False
    holder = find_min(mini_tree.root)  #(1.0)
    while holder != None:
        for T in tab:
            if T != mini_tree:
                res = find(T.root,holder.val)
                if res == None:
                    future = find_next(holder)
                    remove(mini_tree,holder.val)
                    holder = future
                    flag = True

        if not flag:
            holder = find_next(holder)

    return mini_tree


if __name__ == "__main__":
    from zad2testy_kk_kolos5 import runtests
    runtests(drzewa_jakies)
