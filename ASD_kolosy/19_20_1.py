

def digits(x):     #złożonośc O( len(liczby) + 10) - raczej można uznac za stały
    C = [0] * 10
    one_t, many_t = 0,0
    while x != 0:
        C[x%10] += 1
        x //= 10

    for i in range(10):
        if C[i] == 1:
            one_t += 1
        elif C[i] > 1:
            many_t += 1

    return one_t, many_t


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x1 = T[r][1]    #przystosowanie do potrzeb sprawdzania ładnosci
    x2 = T[r][2]
    i = p - 1
    for j in range(p, r):
        if T[j][1] > x1:   #sprawdzanie pierwszego kryterium ładnosci
            i += 1
            T[i], T[j] = T[j], T[i]

        elif T[j][1] == x1 and T[j][2] <= x2:  #sprawdzanie drugiego kryterium ładnosci, tutaj nam potrzeba tej równości, żeby petla nie kreciła sie w kólko
            i += 1
            T[i], T[j] = T[j], T[i]


    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):   #ogolna złożonosc quicksorta O(nlogn)
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1


        else:
            quick_sort_mem2(T, q + 1, r)

            r = q - 1


def pretty_sort(T):
    n = len(T)
    S = [[0]*3 for i in range(n)] #struktura przechowujaca dane - czas alokacji O(n) / O(3n) ???

    for i in range(n):  #jedno przejscie po tablicy i uzupełnienie struktury danych
        S[i][0] = T[i]
        S[i][1], S[i][2] = digits(T[i])



    quick_sort_mem2(S,0, n-1) #sortowanie wartosci według kryteriów ładności   O(nlogn) ????

    for i in range(n):  #przepisywanie wyniku do tablicy wysciowej
        T[i] = S[i][0]

    for i in range(i):  # testowy print czy struktura działa
        print(S[i])
    print("----")

    return T


test_num = 23455521     #zatem digits działa tak jak chcielismy :))
#print(digits(test_num))
test_tab1 = [[123,3,0],[23455,3,1],[6377,2,1],[1266,2,1],[114577,2,2]]
'''partition_random(test_tab1,0,len(test_tab1) - 1)  #ciezko stwierdzic po jednym partition ://
print(test_tab1)'''
test_tab2 = [123,23455,6377,1266,114577,36,4557899,321455,234243,66756755,7688767,123244,23456,30]  #w partition odkurwia sie lekki random
print(pretty_sort(test_tab2))


#chyba działa

#złozonosc O(nlogn) narzucona przez algorytm sortowania quick sort, reszta operacji w czasie liniowym lub stałym, pytanie tylko co z alokacja tablicy S

#opis - tworzymy dodatkowa strukture która przechowuje dane typu [liczba, ile cyfr jednokrot. , ile cyfr wielokrot.]. Potem sortujemy ją według odpowiednich kryteriów.
#po posortowaniu przepisujemy same liczby w odpowiedniej kolejnosci do tablicy wynikowej, ilosc cyfr obu typów wyciagamy korzystajac z pomocniczej tablicy wystapien , czyli
#idei zaczerpnietej z countsorta


#1 pkt od Lukasza za za słabą złożoność