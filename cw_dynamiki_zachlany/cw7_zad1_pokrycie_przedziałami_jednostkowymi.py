'''Zadanie 1. (pokrycie przedziałami jednostkowymi)
Dany jest zbiór punktówX={x1, . . . , xn} na prostej.
Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,potrzebnych do pokrycia wszystkich punktów z X.
 (Przykład: JeśliX={0.25,0.5,1.6}to potrzeba dwóchprzedziałów, np.[0.2,1.2]oraz[1.4,2.4])'''

# idea -  bierzemy przedział zawierajacy najwczesniej lezacy niepokryty jeszcze punkt
# czynnosc powtarzamy do zakrycia wszystkich punktów

#ciche zał. otrzymany zbiór zawiera już posorotwane punkty

#złozonosc : czasowa O(n) - kazdy punkt przejdziemy maksymalnie raz, pamieciowa -> w miejscu


def cover(X):
    n = len(X)
    counter = 0
    ind = 0

    while ind < n:
        counter += 1
        tmp = X[ind] + 1
        inside = ind + 1
        while inside < n and X[inside] <= tmp:
            inside += 1

        ind = inside

    return counter


test = [0.25, 0.5, 1.6]
test2 = [0.25, 0.5, 1.3, 1.6, 2.3, 6.9]
print(cover(test2))




