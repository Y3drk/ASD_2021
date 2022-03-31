'''W problemie sumy podzbioru mamy dany ciąg liczb naturalnych dodatnich A[0],A[1],...,A[n-1] oraz liczbe T.
Należy stwierdzić czy istnieje podciąg sumujący się dokładnie do T'''

# idea - adaptacja problemu plecakowego
# zamiast MaxW używamy T, ale nie mamy tym razem dwóch tablic P i W tylko jedną A. Znowu stajemy przed wyborem, czy nalezy liczbę wziąc do sumy, czy tez nie?
# funkcja rekurencyjna jest niemal taka sama jak w orginalnym, dyskretnym problemie plecakowym.
# f(i,t) = suma najbliższa T jaką można osiągnąc wybierajac spośród przedmiotów od 0 do i nie przekraczając wartości t.
# przypadki graniczne:
# 1) f(0,t) = 0 jesli A[0] > t lub A[0] wpp
# 2) f(i,0) = 0 - wynika z założenia o liczbach należących do zbioru
# generalny wzór : f(i,t) = max { (I) f(i-1,w), (II) f(i - 1, t - A[i]) + A[i]) }
# (I) - gdy nie chcemy wziąc danego elementu, co zawsze może się wydarzyć
# (II) - gdy chcemy wziąć dany element i możemy to zrobić ( zał. t >=  A[i])
# jesli mozliwe jest utworzenie takiej sumy liczb to F[n - 1][T] == T


def knapsack_for_sum(A,T):
    n = len(A)
    if n == 0:
        return False

    F = [[0]*(T+1) for i in range(n)]

    '''mini = 10**3 #dodatkowy case który pomoże w wypełnianiu tablicy, byc moze niekonieczny
    ind = None
    for i in range(n):
        if mini > A[i]:
            mini = A[i]
            ind = i

    A[0], A[ind] = A[ind], A[0]'''

    for t in range(A[0],T + 1):  #przypadek graniczny 1
        F[0][t] = A[0]

    for i in range(1,n):  #od jedynki przez przypadek graniczny 1
        for t in range(1,T + 1):   #od jedynki przez przypadek graniczny 1
            F[i][t] = F[i - 1][t]
            if t >= A[i]:
                F[i][t] = max(F[i][t], F[i - 1][t - A[i]] + A[i])

    #print(T)
    for h in range(n):
        print(F[h]) #testowe printy
    print("-------------")

    return F[n - 1][T] == T


test = [5,1,3,10,27,2,8,4,17,6]
'''import random
test_rnd = random.sample(range(1,100),random.randint(1,99))
print(test_rnd)
print(knapsack_for_sum(test_rnd,random.randint(1,1000)))'''
test2 = [5,4,3]
print(knapsack_for_sum(test,21))
print(knapsack_for_sum(test2,10))
#wydaje sie działac





