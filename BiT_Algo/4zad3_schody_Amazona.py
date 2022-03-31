'''Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1.
początkowo stoimy na pozycji 0, wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.

Przykład A = {1,3,2,1,0}
Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4.
Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
'''

# idea - f(i) = ilosc sposobów na która mozna dotrzec do pola i-tego


def Amazon_staircase(A):
    n = len(A)
    DP = [0 for _ in range(n)]
    DP[0] = 1
    for i in range(n):
        for j in range(1, A[i] + 1):
            DP[i + j] += DP[i]

    #print(DP)
    return DP[n -1]


test = [1,3,2,1,0]
print(Amazon_staircase(test))
