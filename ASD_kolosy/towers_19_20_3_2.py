'''Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
i ciągnie się do pozycji bi. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
tablicę A zawierającą pozycje klocków ai,bi. Funkcja powinna zwrócić maksymalną wysokość wieży
jaką można uzyskać w klocków w tablicy A.

Przykład Dla tablicy A = [(1,4),(0,5),(1,5),(2,6),(2,4)] wynikiem jest 3, natomiast dla
tablicy A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)] wynikiem jest 2.'''


# skorzystamy z dynamicznej funckji f(i) = najwyzsza wieża składająca sie z klocków od 0 do i oraz konczaca sie na klocku itym
# f(0) = 1
# f(i) = max po j od 0 do i - 1 { jesli klocki nachodza na siebie [f[j]] } + 1

def towers(A):
    n = len(A)
    F = [1 for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[i], F[j] + 1)

    #print(F)
    return max(F)

A1 = [(1,4),(0,5),(1,5),(2,6),(2,4)]
print(towers(A1))
A2 = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
print(towers(A2))

