'''Zadanie 4. (klocki) Dany jest ciąg klocków (K1, . . . , Kn). Klocek Ki zaczyna sie na pozycji ai
i ciągnie
się do pozycji bi (wszystkie pozycje to nieujemne liczby naturalne) oraz ma wysokość 1. Klocki układane są po
kolei–jeśli klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzającego
klocka). Na przykład dla klocków o pozycjach (1, 3), (2, 5), (0, 3), (8, 9), (4, 6) powstaje konstrukcja o
wysokości trzech klocków. Proszę podać możliwie jak najszybszy algorytm, który oblicza wysokośc powstałej
konstrukcji.'''


#mozna jakos dzrewem przedziałowym, ja sb trzaskam dynamica O(n^2) i elo

# korzystamy z funkcji f(i) = najwieksza wysokosc wiezy, ktora zawiera elemnty od 0 do i-1 i konczy sie i-tym klockiem
# f(0) = 1
# f(i) = (j od 0 do i-1) {jesli klocki "zachaczaja sie"} max( po spełniajacych warunki) + 1

def fucked_up_tetris(K):
    n = len(K)
    F = [0 for _ in range(n)]
    F[0] = 1

    for i in range(1,n):
        maxi = 0
        for j in range(i):
            if K[j][0] <=K[i][1] <= K[j][1] or K[j][1] >= K[i][0] >= K[j][0]:
                maxi = max(maxi,F[j])

        F[i] = maxi + 1

    print(F)
    return max(F)


test = [(1,3),(2,5),(0,3),(8,9),(4,6)]
print(fucked_up_tetris(test))

