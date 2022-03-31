'''Dostajemy na wejściu trzy stringi: A, B i C. A i B są tej samej długości. Zachodzą następujące właściwości:
Litery na tym samym indeksie w stringach A i B są równoważne
Jeżeli litera a jest równoważna z literą b, to litera b jest równoważna z literą a
Jeżeli litera a jest równoważna z b, a litera b z literą c, to litera a jest równoważna z literą c
Każda litera jest równoważna sama ze sobą

W stringu C możemy zamienić dowolną literę z literą do niej równoważną. Jaki jest najmniejszy leksykograficznie string, który możemy w tej sposób skonstruować?
'''

# idea - korzystanie z find union, tylko zamiast rangi drzewa łączymy, z najmniejszym leksykograficznie reprezentantem, co troche psuje
# złożonośc ale zapewnia poprawność. Wszystkie uniklane litery z a i b początkowo ustawiamy jako node'y
# potem przechodzimy po a i b az do zakonczenia krótszego z nich i wykonujemy operacje find-union wg umówiony reguł równoważności
# potem przechodzimy po c i gdy tylko to możliwe zamieniamy jego litere z korzeniem takiego drzewa


class Node:
    def __init__(self,val, rank = 0):
        self.val = val
        self.rank = rank
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent


def union(x,y):  # rank jest stały bo oznacza pozycje leksykograficzna litery, niestety zlożonosc tych operacji spada do O(n), (???)
    # gdzie n to ilosc operacji makeSet -
    # CZY MOZNA TO OBEJSC
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank < y.rank:
        y.parent = x

    else:
        x.parent = y

def equivalent_letters(A, B, C): #potencjalna złożnośc całosci O(min(a,b)^2) (???)
    a = len(A)
    b = len(B)
    c = len(C)
    letters = []
    for i in range(26):
        letters += [Node(i,i)]

    for l in range(min(a,b)):
        if find(letters[ord(A[l]) - 97]) != find(letters[ord(B[l]) - 97]):
            union(letters[ord(A[l]) - 97],letters[ord(B[l])-97])

    res = []

    for s in range(c):
        #print("probujemy podmienic:",C[s])
        x = find(letters[ord(C[s]) - 97])
        #print("znalezlismy:",chr(x.val + 97))
        #print("----")
        res += chr(x.val + 97)

    for i in range(c):
        print(res[i],end='')
    return


A0 = 'buddha'
B0 = 'abada'
C0 = 'honda'

equivalent_letters(A0,B0,C0)


