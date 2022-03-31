'''Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
na k spójnych podciągów (naszych "płotów"): (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1).
Przez wartość i-go podciągu rozumiemy sumę jego elementów,
 a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób).
Wartością podziału jest wartość jego najgorszego podciągu. Zadanie polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości'''

# idea - korzystamy z funkcji f(i,t) = maksymalna watosc podziału ciagu od a0,..,ai na t pracowników.
# warunki brzegowe :
# f(0,t) = a[0] jesli t = 1, -inf wpp
# f(i,t) = gdy i < t --> -inf
# główna funkcja : f(i,t) = max(po k od 0 do i-1) { min((f(i - k, t-1), suma od k+1 do i po a[i]), f(i,t)}


def sum_for_one(A,k,i):
    sum = 0
    #print(A[i -k + 1:i+1])
    for i in range(i - k + 1,i + 1):
        sum += A[i]

    return sum


def painting_fences(t,A):
    n = len(A)
    DP = [[-float('inf')]*(t+1) for _ in range(n)]
    DP[0][1] = A[0]
    for i in range(1,n):
        DP[i][1] = DP[i -1][1] + A[i]

    for f in range(1,n):   # f = fences
        for w in range(2,min(f + 2,t+1)): # w = workers
            #print("płotów:",f + 1,"pracowników",w)
            for k in range(1,f + 1):
                #print("k=",k,";wynik dla ",f - k + 1," płotów i ",w -1,", pracowników=",DP[f - k][w - 1],";wynik t-ego pracownika=",sum_for_one(A,k,f),";obecny rezultat=",DP[f][w])
                #print("co wpisujemy:",max(min(DP[f - k][w - 1],sum_for_one(A,k,f)), DP[f][w]))
                DP[f][w] = max(min(DP[f - k][w - 1],sum_for_one(A,k,f)), DP[f][w])
            #print("-----")

    '''for i in range(n):
        print(DP[i])'''

    return DP[n-1][t]


test = [2,8,6,5,4,1,3,4]
k = 3
print(painting_fences(k,test))