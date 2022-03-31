'''Zadanie 6 (ścieżka w drzewie) Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma—
potencjalnie ujemną—wartość value(v). Proszę zaproponować algorytm, który znajduje wartość najbardziej
wartościowej ścieżki w drzewie T.'''

# idea - f(v) = wartosc najlepszej sciezki zaczynajacej sie w v i idacej w strone lisci

# f(v) = max { 0, v.val, v.val + f(v.left),  v.val + f(v.right)}
# 4 opcje -
# (1) wgl nie bierzemy tego wezła,
# (2) bierzemy tylko jego,
# (3) bierzemy jego lewa sciezke i jego samego silą rzeczy,
# (4) bierzemy jego prawa sciezke i jego samego silą rzeczy

# skąd wynik - max ( po wszystkich v) { v.val + f(left) + f(right) , 0}
