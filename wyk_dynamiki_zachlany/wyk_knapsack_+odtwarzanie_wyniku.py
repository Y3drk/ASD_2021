def knapsack(W,P,MaxW):
    n = len(W)
    F = [[0]*(MaxW + 1) for _ in range(n)]  #tablica z wierszami a kolumny to wartosci wagi

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]    #uzupełniamy naszą tablice wyjsciowa

    for i in range(1,n): #wypełniamy po kolei wiersze
        for w in range(1, MaxW + 1):      #a w kazdym wierszu wszystkie dopuszczalne wagi
            F[i][w] = F[i - 1][w]  #sytuacja gdy naszego i-tego przedmiotu nie wzięlismy co zawsze mozemy zrobić
            if w >= W[i]:  #jesli przedmiot zdołamy wziac do naszego plecaka to...
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i]) #sprawdzamy ktora opcja nam sie bardziej opłaca, bo moze jednak warto ten przedmiot wziac

        #wynikiem jest prawy dolny róg naszej tablicy
            '''for h in range(n):
                print(F[h]) #testowe printy
            print("-------------")'''''

    return F[n - 1][MaxW],F #jaki jest najwiekszy zysk jesli dopuszczamy MaxW i rozwazamy n przedmiotów


def get_solution(F,W,P,i,w):
    if i < 0:
        return []

    if i == 0:
        if w >= W[0]:
            return [0]
        return []

    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]

    return get_solution(F, W, P, i - 1, w)


Wtest2 = [4, 5, 12, 9, 1, 13]
Ptest2 = [10, 8, 4, 5, 3, 7]
MaxWtest2 = 24

Wtest_pod_obw1 = [1, 4, 2, 3, 4, 3]
Ptest_pod_obw1 = [2, 5, 3, 8, 1, 1]
MaxWtest_pod_obw1 = 10
score,F = knapsack(Wtest_pod_obw1, Ptest_pod_obw1, MaxWtest_pod_obw1)
res = get_solution(F,Wtest_pod_obw1,Ptest_pod_obw1,len(Wtest_pod_obw1)-1,MaxWtest_pod_obw1)
print(score)
for i in range(len(res)):
    print(Ptest_pod_obw1[res[i]]," ", end="")

#print("")
#print(res)