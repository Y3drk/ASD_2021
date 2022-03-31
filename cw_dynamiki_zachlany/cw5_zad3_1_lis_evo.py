# 3.2 jest w zestaw 5 plus wczesniejsze kolosy w code forces + pierdoły

'''Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
najdłuższego rosnącego podciągu?'''

# idea - bierzemy tablice, z ktorej mamy wydobyc ten LIS i tworzymy jej kopie, która nastepnie sortujemy.
# jesli w tym momencie odpalimy lcs to podciag który znajdziemy na pewno bedzie rosnacy ze wzgledu na posortowana kopie i to zapewnia nam poprawne rozwiazanie zadania

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

    '''for i in range(n+1):
        print(L[i])'''

    return L[n][m]


A = [4,2,5,1,8,7,16,5]
B = A.copy()
B.sort()
print(A)
print(B)
print("----")
print(lcs(A,B))