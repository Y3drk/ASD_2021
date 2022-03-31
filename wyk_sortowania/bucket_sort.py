from random import random
from random import randint


def select_sort(T):            #do sortowania wewnątrz kubełków bucket sort uzywa innego sortowania. Cormen poleca select sorta wiec i ja go uzyje
    n = len(T)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if T[j] < T[mini]:
                mini = j

        T[mini], T[i] = T[i], T[mini]

    return T

def insert_sort(T): #bez wartownika
    n = len(T)
    for i in range(1, n):
        tmp = T[i]
        j = i - 1
        while (j >= 0) and (tmp < T[j]):
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = tmp

    return T


def bucket_sort(T):         #bucket_sort czesto zakłada, że sortowane sa liczby z przedziału [0,1)
    n = len(T)
    B = [[] * n for _ in range(n)] #tablica kubełków

    maxi = -1                     #dodatkowa procedura umożliwiajaca sortowanie wiekszych liczb  (*)
    for l in range(n):
        if T[l] > maxi:             #szukanie najwiekszej liczby i jej długosci, nastepnie wszystkie liczby sprowadzamy do zakresu [0,1) (*)
            maxi = T[l]

    for i in range(n):                #rozkładanie elementów do kubełków
        B[int(n*T[i] / (maxi + 1))] += [T[i]]     #dzielimy przez wartosc najwiekszej liczby + 1 zeby nie wyjsc za zakres
    for j in range(n):      #sortowanie kazdego kubełka osobno
        if B[j] != []:
            select_sort(B[j])
    T = []
    for k in range(n):   #złaczenie posortowanych kubełków
        if B[k] != []:
            T += B[k]

    return T


#fragmenty oznaczone gwiazdką(*) dotycza sortowania elementow >= 1. Bucket sortem robi się to rzadko, ale chce mieć taką możliwosc

test = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
test2 = [23,45,67,89,10,20,33,45,67,89,99,18,88,63,78]  #krzaczy sie podział na kubełki prawdopodobnie stad założenie o zakresie liczb - fixed
test3 = [round(random(),2) for i in range(20)]
test4 = [round(randint(1,2000),2) for _ in range(30)]
print(bucket_sort(test))
print(bucket_sort(test2))
print(bucket_sort(test3))
print(bucket_sort(test4))

