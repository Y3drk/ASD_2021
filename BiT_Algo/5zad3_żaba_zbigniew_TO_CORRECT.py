'''Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąski dodaje się do aktualnej energii Zbigniewa).

Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja powinna zwrócić minimalną liczbę skoków potrzebną,
 żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.

Podpowiedź. Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
dotrzeć do liczby i mieć w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
(Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).
'''


# idea - korzystamy z podpowiedzianej funkcji f(i,y)
# przypadki brzegowe:
# f(0,0 do A[0] - 1) = 0
# ???? f(0,A[0]) = A[0]
# f(i, y) = min (po k od 1 do i -1) { f(i - k, y - A[i] + k)} + 1 - wewnątrz tej funkcji nie chcemy dostac liczby ujemnej ale załatwi to max(y - A[i] + k,0)

#rozwiazanie powinno być w komórce DP[n -1][0] -- ale trzeba to sprawdzic

# złożoność O(n^3)

def Zbigniew_the_frog(A):
    n = len(A)
    DP = [[-1]*n for _ in range(n)]

    for i in range(A[0] + 1):
        DP[0][i] = 0

    for j in range(A[0] + 1,n):
        DP[0][j] = float("inf")

    for row in DP:
        print(row)

    for i in range(1,n):
        for y in range(n):
            best = float('inf')
            print("i:",i,"y:",y)

            for k in range(1,i):
                print("w drugiej komorce:",max(y + i - A[i] - k,0),y + i - A[i] + k, A[i], k)
                print("gdzie patrzymy:",DP[k][max(y + i- A[i] - k,0)])

                best = min(best, DP[k][max(y + i - A[i] - k,0)])  #max(y - A[i] + k,0)

            print(best)
            if best != float("inf"):
                DP[i][y] = best + 1

            for row in DP:
                print(row)
            print("---")

    for row in DP:
        print(row)

    #złe wyciaganie odpowiedzi
    '''if DP[n -1][0] != -1: 
        return DP[n -1][0]
    else:
        return -1'''

A1 =  [2,2,1,0,0,0] #oczekiwany wynik 3
print(Zbigniew_the_frog(A1))
print("----")
A2 =  [4,5,2,4,1,2,1,0] #oczekiwany wynik 2
#print(Zbigniew_the_frog(A2))
print("----")





