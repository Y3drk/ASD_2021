''' Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).'''

# Ciche zał: zestaw monet umozliwia wypłacenie każdej kwoty
# idea - koszystamy z funkcji f(i) = najmniejsza ilosc monet potrzebna do wypłacenia kwoty i
#przypadek brzegowy f(0) = 0
# f(i) = min (idac po kazdym nominale) f(i - nominał) + 1
# złozonosc O(nx) gdzie x to kwota która mamy wypłacic

def coins(M,x):
    F = [(x + 1) for _ in range(x+1)]
    F[0] = 0
    for i in range(x + 1):
        for m in M:
            if i >= m:
                F[i] = min(F[i], F[i - m] + 1)

    #print(F)
    return F[x]

x = 15
M = [1,5,8]
print(coins(M,x))
