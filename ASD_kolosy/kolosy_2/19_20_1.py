'''2pkt.] Zadanie 1. Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami
(wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero) i zwraca długość (wagę) najdłuższej ścieżki prostej w
tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:

class Node:
def __init__( self ):
self.children = 0 # liczba dzieci węzła
self.child = [] # lista par (dziecko, waga krawędzi)
... # wolno dopisać własne pola

Poniższy kod tworzy drzewo z korzeniem A, który ma dwoje dzieci, węzły B i C, do których
prowadzą krawędzie o wagach 5 i −1:

A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
Rozwiązaniem dla drzewa A jest 5 (osiągnięte przez ścieżkę A-B; ścieżka B-A-C ma wagę
5 − 1 = 4. Proszę skrótowo wyjaśnić ideę algorytmu oraz oszacować jego złożoność czasową.'''