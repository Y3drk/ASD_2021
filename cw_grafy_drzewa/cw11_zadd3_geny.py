'''Zadanie 3. (geny) W pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. Każda sekwencja
to pewien napis składający się z symboli G, A, T, i C. Przed dalszymi badaniami konieczne jest upewnić się,
że wszystkie sekwencje DNA są parami różne. Proszę opisać algorytm, który sprawdza czy tak faktycznie
jest.
'''

#zwracamy true jesli juz taka sekwencja genowa istnieje

# idziemy sb po drzewie (od korzenia) i patrzymy czy juz taki układ liter był, jesli nie to dodajemy nowe litery aby uzupełnic baze sekwencji, jesli tak to idziemy po
# okreslonej gałęzi dalej zadajac to samo pytanie
# tam gdzie konczy sie sekwencja ustawiamy 1 aby obrazowac ze dana sekwencja jest juz zapisana w drzewie


class GATCNode:
    def __init__(self, letter):
        self.letter = letter
        self.g = None
        self.a = None
        self.t = None
        self.c = None
        self.exist = 0


def exist(root, string):
    current = root
    for letter in string:
        if letter == 'G':

            if current.g is None:
                node = GATCNode("G")
                current.g = node
            current = current.g

        elif letter == 'A':
            if current.a is None:
                node = GATCNode("A")
                current.a = node
            current = current.a

        elif letter == 'T':
            if current.t is None:
                node = GATCNode("T")
                current.t = node
            current = current.t

        elif letter == 'C':
            if current.c is None:
                node = GATCNode("C")
                current.c = node
            current = current.c

    if current.exist == 0:
        current.exist = 1
        return False

    return True


string1 = "GATC"
string2 = "GATAC"
string3 = "GATAC"

G = GATCNode("G")
A = GATCNode("A")
T = GATCNode("T")
C = GATCNode("C")

root = GATCNode('.')
root.g = G
root.a = A
root.t = T
root.c = C

print(exist(root, string1))
print(exist(root, string2))
print(exist(root, string3))

