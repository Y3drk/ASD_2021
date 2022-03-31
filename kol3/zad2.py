#Jedrzej Ziebura

# bedziemy schodzic w dół drzewa, dopóki nie dotrzemy do liscia lub bedziemy mogli pójsc tylko w prawo.

# W kazdym weźle bedziemy badali potencjalne minimum czyli:
# -> jesli wezeł ma dwójke dzieci, to porównamy jego wartosc z suma minimów znalezionych w tych dzieciach,
# -> jesli ma tylko lewe dziecko to z minimum z jego podrzewa,
# -> a dla tylko prawego dziecka nie bedziemy sprawdzać, bo z definicji drzew BST nie bedziemy w stanie poprawic minimum idąc tam.

# w ten sposób dla kazdej sciezki znajdziemy tylko jedna optymalna wartosc, a suma takich wartosci bedzie minimum zapisanym w korzeniu,
# co tez zwrócimy

# W kazdym weźle bedziem tylko raz stad takie przejscie to koszt O(n).


from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def if_leave(node):
    return (node.left == None and node.right == None)


def walk_the_tree(node,mini):

    if node.parent != None and not (node.left == None and node.right == None) and mini > node.value:
        mini = node.value

    if node.left != None and node.right != None:
        left = walk_the_tree(node.left, float('inf'))
        right = walk_the_tree(node.right, float('inf'))
        res = left + right
        if res < mini and not if_leave(node.left) and not if_leave(node.right):
            mini = res

        return mini

    if node.left != None:
        opt = walk_the_tree(node.left, mini)
        if opt < mini:
            mini = opt

    return mini


def cutthetree(T):
    tmp = walk_the_tree(T,float('inf'))
    return tmp

    
runtests(cutthetree)


