''' Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie.'''

# idea korzystamy z funckji f(i,j) = najtansza droga do pola i,j ruszajac sie tylko w dół lub w prawo
#przypadki brzegowe f(0,0) = A[0][0]
# do pierwszej kolumny mozna dotrzec  tylko od góry wiec mozemy ja od razu uzupełnic, analogicznie dla pierwszego wiersza

def cheapest_walk(A):
    y = len(A)
    x = len(A[0])
    C = [[0]*x for _ in range(y)]
    C[0][0] = A[0][0]
    for i in range(y):
        for j in range(x):
            if i == 0 and j > 0:
                C[i][j] = A[i][j] + C[i][j-1]
            elif j == 0 and i > 0:
                C[i][j] = A[i][j] + C[i-1][j]

            elif j > 0 and i > 0:
                C[i][j] = min(C[i - 1][j], C[i][j - 1]) + A[i][j]

    '''for i in range(y):
        print(C[i])
        '''
    return C[y - 1][x - 1]


test = [[4, 7, 8],
        [2, 1, 1]]

print(cheapest_walk(test))