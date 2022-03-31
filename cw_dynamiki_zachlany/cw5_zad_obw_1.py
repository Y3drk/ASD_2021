'''Prosze przedstawić algorytm dla problemu knapsack działający w czasie O(n*(suma wszystkich profitów))'''

#idea - modyfikacja funkcji f w nastepujacy sposób
# Co wazne, w tablicy pomocniczej F zapisujemy zarówno wage naszego rozwiazania czastkowego jak i profit tegoż rozwiązania!

# f(i,p) = waga maksymalnego zysku nieprzekraczającego p, mozliwego do uzyskania z przedmiotów od 0 do i

# przypadki graniczne:
# 1) f(0,p) = 0 gdy p < P[0] lub W[0], gdy p >= P[0]
# 2) f(i,0) = 0 , ciche zał. nie ma przedmiotów bezwartościowych

# głowna funkcja :
# f(i,p) = komórka z wiekszym ZYSKIEM spośród {f(i - 1)(p) , f(i - 1)(p - P[i]) + P[i]} **
# ** jesli zyski są równe jako wynik funkcji przyjmujemy komórkę o mniejszej WADZE

# wyniku uzyskujemy przechodząc po ostatnim wierszu od końca i sprawdzając warunek czy waga komórki <= MaxW


def knapsack_o_nsum_of_profits(W,P,MaxW):
    n = len(W)
    sum_of_profits = 0
    for i in range(n):
        sum_of_profits += P[i]

    F = [[[0, 0]]*(sum_of_profits + 1) for _ in range(n)]

    for p in range(P[0], sum_of_profits + 1):
        F[0][p] = [P[0],W[0]]


    for i in range(1,n):
        #print("i:",i)
        for p in range(P[0], sum_of_profits + 1):
            F[i][p] = F[i - 1][p]
            #print("p:",p)
            if p >= P[i]:  #czy wgl możemy wziac dany element do plecaka
                #print("ent1")
                if F[i][p][0] == F[i - 1][p - P[i]][0] + P[i]:   #jesli zysk w obu kwestiach jest równy (**)
                    #print("ent2")
                    if F[i][p][1] >= F[i - 1][p - P[i]][1] + W[i]: #jesli waga bez wziecia jest >= z wzieciem to bierzemy przedmiot
                        #print("ent3")
                        F[i][p] = [F[i - 1][p - P[i]][0] + P[i],F[i - 1][p - P[i]][1] + W[i]]


                elif F[i][p][0] < F[i - 1][p - P[i]][0] + P[i]:
                    #print("ent2.2")
                    F[i][p] = [F[i - 1][p - P[i]][0] + P[i], F[i - 1][p - P[i]][1] + W[i]]

            #print(".....")

    '''for h in range(n):
        print(F[h])
    print("-------------")'''

    for p in range(sum_of_profits, 0, -1): #wyciaganie wyniku
        if F[n-1][p][1] <= MaxW:
            return F[n-1][p][0]

    return


Wtest2 = [4, 5, 12, 9, 1, 13]
Ptest2 = [10, 8, 4, 5, 3, 7]
MaxWtest2 = 24
print(knapsack_o_nsum_of_profits(Wtest2,Ptest2,MaxWtest2))

Wtest_pod_obw1 = [1, 4, 2, 3, 4, 3]
Ptest_pod_obw1 = [2, 5, 3, 8, 1, 1]
MaxWtest_pod_obw1 = 10
print(knapsack_o_nsum_of_profits(Wtest_pod_obw1,Ptest_pod_obw1,MaxWtest_pod_obw1))

Wtest =[4,1,2,4,3,5,10,3]
Ptest =[7,3,2,10,4,1,7,2]
MaxWtest = 10
print(knapsack_o_nsum_of_profits(Wtest,Ptest,MaxWtest))
#te chyba działa

W_test_pod_wyjebke = [10]
P_test_pod_wyjebke = [88]
MaxW_test_pod_wyjebke = 9
print(knapsack_o_nsum_of_profits(W_test_pod_wyjebke,P_test_pod_wyjebke,MaxW_test_pod_wyjebke))

#print("rnd tests")
import random
Wtest_rnd = [random.randint(1,20) for _ in range(10)]
Ptest_rnd = [random.randint(1,20) for _ in range(10)]
MaxWtest_rnd = random.randint(1,89)
#print(Wtest_rnd)
#print(Ptest_rnd)
#print(MaxWtest_rnd)
#print(knapsack_o_nsum_of_profits(Wtest_rnd,Ptest_rnd,MaxWtest_rnd))

P = [10,8,4,5,3]
W = [4,5,12,9,1]
MW = 24
print(knapsack_o_nsum_of_profits(W,P,MW))