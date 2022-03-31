'''Wyjeżdżacie ze znajomymi na wakacje. Macie dwa samochody i N bagaży o łącznej wadze W.
Waga każdego z bagaży jest liczbą naturalną dodatnią. Czy jesteście w stanie tak je zapakować, aby w obu samochodach były bagaże o tej samej łącznej wadze?'''

# idea - szukamy podciagu sumujacego sie do W/2, czyli de facto obowiazkowe o sumie podciagu rownej dokładnie t
# złozonosc O(n*W)

def baggage_packing(A,W):
    n = len(A)
    if n == 0:
        return False

    if W % 2 == 1:
        return False

    F = [[0]*((W//2)+1) for i in range(n)]

    '''mini = 10**3 #dodatkowy case który pomoże w wypełnianiu tablicy, byc moze niekonieczny
    ind = None
    for i in range(n):
        if mini > A[i]:
            mini = A[i]
            ind = i

    A[0], A[ind] = A[ind], A[0]'''

    for t in range(A[0],(W//2) + 1):  #przypadek graniczny 1
        F[0][t] = A[0]

    for i in range(1,n):  #od jedynki przez przypadek graniczny 1
        for t in range(1,(W//2) + 1):   #od jedynki przez przypadek graniczny 1
            F[i][t] = F[i - 1][t]
            if t >= A[i]:
                F[i][t] = max(F[i][t], F[i - 1][t - A[i]] + A[i])

    #print(T)
    '''for h in range(n):
        print(F[h]) #testowe printy
    print("-------------")'''

    return F[n - 1][(W//2)] == W//2



test = [5,1,3,10,27,2,8,4,16,6]
W = 0
for i in range(len(test)):
    W += test[i]

print(W)
print(baggage_packing(test,W))