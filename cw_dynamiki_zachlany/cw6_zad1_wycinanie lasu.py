'''Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
, jaki
można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
John znajdzie optymalny plan wycinki.'''

# idea - korzystamy z funkcji f(i) = najwieksza wartosc wycinki drzew od 0 do i przestrzegajaca zasad

# f(0) = T[0] - wiadomo ze pojedyncze drzewo zawsze lepiej wyciac niz nie xdd

# albo dane drzewo bierzemy albo nie
# f(i) = max { f(i - 2) + T[i], f(i - 1)}

#złożoność:
# czasowa - O(n)
# pamieciowa w miejscu

def cut_trees(T):
    n = len(T)
    u_tree = T[0]
    p_tree = max(T[0], T[1])

    for i in range(2,n):
        p_tree,u_tree = max(u_tree + T[i], p_tree), p_tree

    return p_tree


test = [4,11,5,2,10]
print(cut_trees(test))


'''credit Niko Korohoda
def funk(C):
    n = len(C)
    x2 = C[0]
    x1 = max(C[0], C[1])
    for i in range(2, n):
        x1, x2 = max(x2 + C[i], x1), x1

    return x1'''


