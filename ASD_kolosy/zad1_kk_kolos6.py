class Node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.right = right
        self.left = left

# na poczatek zliczymy ilosc wezłów w drzewie
# stworzymy tablice reprezentujaca piony (w pesymistycznym przypadku pato-drzewa bedzie ich n)
# i bedziemy schodzic w dół drzewa pamietajac w jakim pionie jestesmy i dodawac do odp pól wartosci węzłów
# potem przejdziemy po tablicy wybierajac min i max
# w kązdym wezle bedziemy raz stad złożonosc to O(3n)


def walk_and_add(T,node,pos):
    if T[pos] == None:
        T[pos] = node.key
    else:
        T[pos] += node.key

    if node.left != None:
        walk_and_add(T,node.left, pos - 1)

    if node.right != None:
        walk_and_add(T,node.right, pos + 1)


def maxi_suma_pionowa(root):
    n = 0

    def count_nodes(node):
        nonlocal n
        if node.left != None:
            count_nodes(node.left)
        n += 1
        if node.right != None:
            count_nodes(node.right)

        return

    count_nodes(root)

    T = [None for _ in range(n + 2)]
    mid = n // 2
    walk_and_add(T,root,mid)

    biggest, lowest = float('-inf'), float('inf')

    for i in range(len(T)):
        if T[i] != None:
            if T[i] > biggest:
                biggest = T[i]

            if T[i] < lowest:
                lowest = T[i]

    return biggest, lowest



root = Node(1)
root.left = Node(2)
root.right = Node(3,Node(5,Node(7),Node(8)),Node(6))
print(maxi_suma_pionowa(root),"?=?",11,",",6)

root = Node(-10,
        Node(-20,
            None,
            Node(-11)),
        Node(100,
            Node(90,
                Node(5,
                    None,
                    Node(50)),
                Node(95)),
            Node(105,
                Node(102),
                None)))
print(maxi_suma_pionowa(root),"?=?",297,",",-15)
