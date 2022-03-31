''' Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2)).'''

# idea - korzystamy z funkcji f(i,j) = najdłuższy wspolny podciąg konczacy sie w A[i] i B[j]
# przypadek brzegowy f(0,0) = 0
# jesli trafimy wskaznikami na te same elementy to zwiekszamy komórke na skos w dól o 1 bo to oznacza, ze udało nam sie przedłuzyc najdłuzszy wspólny ciag
# wpp bierzemy lepszy wynik z tych znalezionych wczesniej (co jest oczywiste bo chcemy "ciagnac" za soba ten najlepszy dotychczasowy wynik)
# f(i,j)= max { f(i-1,j), f(i, j-1)}



def lcs(A, B):
    n = len(A)
    m = len(B)
    L = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif A[i-1] == B[j-1]:    #jesli elementy sa takie same to juz mozemy uzupełnic komórke na skos, a -1 sa ze wzgledu na to ze nasza tablica L jest wieksza o 0
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    for i in range(n+1):
        print(L[i])

    return L[n][m]


A = [4,2,5,8,7,5]
B = [8,4,2,9,5,1,7]
print(A)
print(B)
print("----")
print(lcs(A,B))