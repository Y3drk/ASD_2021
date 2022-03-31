from zad2testy_egz0 import runtests

class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.leftval = 0     # wartość krawędzi do lewego poddrzewa jeśli istnieje
    self.right   = None  # prawe poddrzewo
    self.rightval= 0     # wartość krawędzi do prawego poddrzewa jeśli istnieje
    self.X       = None  # miejsce na dodatkowe dane


def initiate(T,k):
    T.X = [float('-inf') for _ in range(k)]
    if T.left != None:
        initiate(T.left, k)

    if T.right != None:
        initiate(T.right, k)


def walk_the_tree(v,k):
    if v.left == None and v.right == None:
        return [0 for _ in range(k)]

    if v.left != None and v.right != None:
        v.X[0] = max(v.leftval, v.rightval)

        tmp1 = walk_the_tree(v.left, k)
        tmp2 = walk_the_tree(v.right, k)
        for i in range(1,k):
            if i == 1:
                v.X[i] = max(v.X[1], v.leftval + tmp1[0], v.rightval + tmp2[0], v.leftval + v.rightval)

            elif i == 2:
                v.X[i] = max(v.X[i], v.leftval + v.rightval + tmp1[0], v.leftval + v.rightval + tmp2[0], v.rightval + tmp2[i - 1], v.leftval + tmp1[i - 1])

            else:
                #v.X[i] = max(v.X[i], v.leftval + tmp1[i - 1], v.rightval + tmp2[i - 1], v.leftval + v.rightval + tmp1[i - 2] + tmp2[i - 2])
                for l in range(i-2):
                    v.X[i] = max(v.X[i], v.leftval + v.rightval + tmp1[l] + tmp2[i - 2 - l])
        #print(v.X)
        return v.X

    if v.left != None:
        tmp1 = walk_the_tree(v.left, k)
        v.X[0] = v.leftval
        for i in range(1,k):

            if i == 1:
                v.X[i] = max(v.X[1], v.leftval + tmp1[0])

            else:
                v.X[i] = max(v.X[i], v.leftval + tmp1[i - 1])

        return v.X

    if v.right != None:
        v.X[0] = v.rightval
        tmp2 = walk_the_tree(v.right, k)
        for i in range(1,k):

            if i == 1:
                v.X[i] = max(v.X[1], v.rightval + tmp2[0])

            else:
                v.X[i] = max(v.X[i], v.rightval + tmp2[i - 1])

        return v.X


def valuableTree( T, k ):
    print(k)
    initiate(T,k)
    walk_the_tree(T,k)
    best = float('-inf')
    #print(T.X)

    def tree_travel(T, k):
        nonlocal best
        print(T.X[k - 1])
        best = max(best, T.X[k - 1])
        if T.left != None:
            tree_travel(T.left, k)

        if T.right != None:
            tree_travel(T.right, k)

    tree_travel(T,k)
    return best

    
runtests( valuableTree )


