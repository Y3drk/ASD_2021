#Jędrzej Ziebura
# zbudujemy drzewo przedziałowe (takie jak pierwsze pokazane na wykładzie) oraz
# stworzymy tablice H przechowujace informacje na jakiej wysokosci konczy sie dany klocek w potencjalnej wiezy.
# w wezłach drzewa bedziemy umieszczać informacje, jaki klocek jako ostatni umiescilismy w danym przedziale.
# po kazdym zastapieniu ostatniego klocka nowym bedzie sprawdzac czy postawienie nowego klocka na poprzednim poprawia wynik wysokosci.
# jesli tak bedzie to odpowiednio zaktualizujemy tablice H
# na koniec przejdziemy po tablicy H, a naszym wynikiem bedzie maksimum z niej

# złożonosć :
# czasowa -> O(nlogn) - wymuszone zarówno sortowaniem punktów brzegowych, zbudowaniem drzewa jak i wstawianiem przedziałów
# pamieciowa -> O(n) - zużywana na drzewo oraz tablice H

# poniewaz od razu bedziemy mieli dostep do wszystkich punktów brzegowych to mozemy od razy zbudowac zbalansowane drzewo
# jesli punkty brzegowe sie powtórza to nic nie szkodzi bo przewiduje to nasza funkcja insert


class Interval_Tree:
    def __init__(self):
        self.root = None


class BST_Node:
    def __init__(self, key, last=None, interval=(float('-inf'), float('inf'))):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.last = last
        self.interval = interval


def insert(Tree, key):
    y = None
    x = Tree.root

    while x != None:
        y = x
        if key < x.key:
            x = x.left
        elif key > x.key:
            x = x.right
        else:
            return False

    elem = BST_Node(key)
    elem.parent = y

    if y == None:
        Tree.root = elem

    elif elem.key < y.key:
        y.left = elem

    else:
        y.right = elem

    return True


def adapt_arr(tab, l, r, flag, New):
    if l != r:
        mid = (l + r) // 2
        New.append(tab[mid])

        if flag:
            if mid != l:
                adapt_arr(tab, l, mid, not flag, New)

            if (mid + 1) != r:
                adapt_arr(tab, mid, r, not flag, New)

        else:
            if (mid + 1) != r:
                adapt_arr(tab, mid, r, not flag, New)

            if mid != l:
                adapt_arr(tab, l, mid, not flag, New)


def set_up_intervals(node, inter):
    node.interval = inter
    if node.left != None:
        set_up_intervals(node.left, (inter[0], node.key))

    if node.right != None:
        set_up_intervals(node.right, (node.key, inter[1]))


def set_up_leaves(node):
    if node.left != None:
        set_up_leaves(node.left)

    else:
        leaf = BST_Node(-1, None, (node.interval[0], node.key))
        leaf.parent = node
        node.left = leaf

    if node.right != None:
        set_up_leaves(node.right)

    else:
        leaf = BST_Node(-1, None, (node.key, node.interval[1]))
        leaf.parent = node
        node.right = leaf


def lets_play_tetris(node, brick, H, ind):
    if node != None:

        if node.interval[0] >= brick[0] and node.interval[1] <= brick[1]:
            print("wbita dla klocka",brick,"do node'a:",node.interval)
            if node.last != None:
                H[ind] = max(H[ind], H[node.last] + brick[2])
            else:
                H[ind] = max(H[ind], brick[2])

            node.last = ind


        if node.interval[1] >= brick[1]:
            lets_play_tetris(node.left, brick, H, ind)

        if node.interval[0] <= brick[0] or node.interval[1] >= brick[1]:
            lets_play_tetris(node.right, brick, H, ind)

    return


def block_height(K):
    IT = Interval_Tree()
    n = len(K)
    H = [0 for _ in range(n)]  # tablica przechowujaca wysokosci na ktorych koncza sie dane klocki
    tmp = []
    for i in range(n):
        tmp.append(K[i][0])
        tmp.append(K[i][1])

    tmp.sort()  # 2n*log(2n)
    new = []
    adapt_arr(tmp, 0, len(tmp) - 1, False, new)
    new.append(tmp[len(tmp) - 1])

    for elem in new:  # budujemy drzewo BST
        insert(IT, elem)

    # chcemy jeszcze lisciom dodac liscie bez liczby oraz przedziały wszystkim węzłom w drzewie 2*O(~2*n) (przejscie po kazdym elemencie drzewa w obu przypadkach)
    set_up_leaves(IT.root)
    set_up_intervals(IT.root, IT.root.interval)

    # mamy juz gotowe drzewo teraz trzeba pododawac przedzialy i odpowiednio uzpełniac H (wewnątrz funkcji lets_play_tetris)
    for e in range(n):
        lets_play_tetris(IT.root, K[e], H, e)

    print(H)
    return max(H)


K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R1 = 5

K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R2 = 6

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")
