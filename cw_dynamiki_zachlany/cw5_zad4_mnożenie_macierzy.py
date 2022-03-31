'''Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejności.'''

# CORMEN
# korzystamy z funkcji m(i,j) = minimalny koszt obliczenia iloczynu macierzy Ai,...,Aj
# pzypadki brzegowe :
# m(i,i) = 0
# m(i,j) = min (po k od i(+1?) do j-1) { m(i,k) + m(k + 1,j) + pi-1*pk*pj} gdzie pi-1, pk i pj to odp wymiary macierzy
# oprocz tablicy M zapamietujacej optymalne wyniki, mamy tez tablice S zapamietujaca optymale umieszczenie indeksu k aby moc odtworzyc wynik


def matrix_multiplication_lowest_cost(P):
    n = len(P)
    M = [[float('inf')]*n for i in range(n)]
    S = [[0]*(n) for i in range(n)]

    for l in range(n):
        M[l][l] = 0  #przypadek brzegowy

    '''for l in range(n):
        print(M[l])'''

    for l in range(2,n):
        #print("for z l")
        for i in range(1,n - l + 1):
            #print("for z i")
            j = i + l - 1
            for k in range(i,j):
                #print("for z k")
                q = M[i][k] + M[k + 1][j] + P[i-1]*P[k]*P[j]
                #print(q)
                if q < M[i][j]:
                    M[i][j] = q
                    S[i][j] = k
            #print("----")
    '''for l in range(n):
        print(M[l])'''

    return M[1][n-1],M, S


def print_optimal_parens(S,i, j):  # odzywskiwanie wyniku
    if j == i:
        print("A",i," ",end="")
    else:
        print("(", end='')
        print_optimal_parens(S,i,S[i][j])
        print_optimal_parens(S,S[i][j] + 1, j)
        print(")",end='')


test = [30,35,15,5,10,20,25]
score = matrix_multiplication_lowest_cost(test)
print(score[0])
print_optimal_parens(score[2],1,len(test) -1)
