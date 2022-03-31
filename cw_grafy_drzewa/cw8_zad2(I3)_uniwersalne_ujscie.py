'''Zadanie 2. (uniwersalne ujście) Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
wychodząca z t.
1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n^2)).
2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.
'''

#1) proste przejscie po tablicy sprawdzajace czy istnieje wiersz samych zer a nastepnie czy istnieje kolumna gdzie wszystkie wiersze poza wczesniej wymienionym
# maja 1


#2) idziemy od G[0][0] i jesli trafimy na 0 idziemy dalej w prawo, a jesli na 1 to idziemy w dół, jesli w jakims wierszu dojdziemy do konca
# to sprawdzamy jeszcze czy składa sie on z samych zer (2), bo jest jedyna szansa na uniwersalne ujscie, a jesli ten warunek bedzie sprawdzony to sprawdzamy,
# te kolumne która przyszlismy do naszego wiersza (3)


def universal_influx(G):
    n = len(G)
    tg_col, tg_row = n, n
    r,c = 0,0
    while r < n and c < n :
        if G[r][c] == 0:
            tg_row = r
            c += 1

        elif G[r][c] == 1:
            r += 1

    if r == n:  #jesli przeszlismy po wszystkich wierszach i nie zatrzymalismy sie na zadnym to na pewno nie ma ujscia
        return False

    elif c == n:
        for i in range(n):  #(2)
            if G[tg_row][i] == 1:
                return False

            if i != tg_row:
                if G[i][tg_row] == 0:
                    return False

    return True


G1 = [[0,1,0,1,1],
     [0,1,1,1,1],
     [0,0,0,0,1],
     [0,0,0,0,0],
     [0,0,1,1,0]]

print(universal_influx(G1))
