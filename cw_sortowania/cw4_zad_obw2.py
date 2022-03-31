'''Zad obw 2  (dwa mozliwe rozwiązania o identycznej złożonosci obliczeniowej)
Pewna tablica długości n zawiera jedynie ceil(logn) róznych wartosci (wiele z nich sie powtarza). Proszę zaimplementowac jak najszybszy algorytm sortujący taką tablicę (szybszy niż nlog)
'''

#metoda pierwsza - count sort z dodatkowa tablica wykorzystującą binary search
'''Idea - 
Tworzymy nasza tablice liczników (C) i tablice informacyjną (I). Uzupełniamy ją  (I) naszymi logn wartosciami. Sortujemy ją w czasie logn*log(logn) np. quicksortem
Potem odpalamy count sorta, z tym ze nasze liczby (w I) nie są już tozsame z indeksami w tablicy C to odp wartości wyszukujemy binary searchem i dopiero wtedy dzieje sie 'magia' countsorta,
który dzięki temu ma złożonośc O(n + logn*log(logn)) --chuj wie co miałem na mysli - binary search to log(logn) złożonosci'''

##stad nasza łaczna złożoność O(nlog(logn))


def interpolation_search(tab, el):  #bs tylko dużo szybciej zawęza przedział
    import math
    l, r = 0, len(tab) - 1

    while l <= r:
        #print(":)")
        #print("Left value:", tab[l])
        #print("right value:", tab[r])

        if tab[l] <= el <= tab[r]:
            mid = l + math.floor(((el - tab[l])*(r - l))/(tab[r]-tab[l]))
            #print('mid:', mid, tab[mid])

            if el > tab[mid]:
                l = mid + 1

            elif el == tab[mid]:
                return mid

            else:
                r = mid - 1

        #print("----")

    if l < len(tab) and el == tab[l]:
        return l

    return False


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


def supercount_sort(T):
    n = len(T)
    I = []
    B = [0 for i in range(n)]

    for i in range(n):   #dodajemy elementy do naszej tablicy informacyjnej  O(nlog(logn)) - tu tez mozna uzyc BS'a zamiast pałowego sprawdzania i bedzie git
        if T[i] not in I:
            I += [T[i]]

    quick_sort_mem2(I,0, len(I)-1) #sortujemy nasza tablice informacyjna O(logn * log(logn))
    C = [0 for i in range(len(I))] #tworzymy nasza tablice liczników
    #print(I)
    #print("....")
    for j in range(n):   #uzupełnianie tablicy liczników  O(n)
        #print("szukamy:",T[j])
        pos = interpolation_search(I,T[j])  # O(log(logn))
        #print(pos)
        C[pos] += 1         #stad nasza łaczna złożoność O(nlog(logn))
    #print(C)
    #print("....")
    for k in range(1,len(I)):  #przekształcenie naszej tablicy do etapu 2
        C[k] += C[k -1]

    for l in range(n - 1, -1, -1):   #finalne sortowanie znowu nasza górna złożonośc
        pos2 = interpolation_search(I,T[l])
        C[pos2] -= 1
        B[C[pos2]] = T[l]
    #print(B)
    for i in range(n):   #przepisywanie wyniku do tablicy wynikowej
        T[i] = B[i]

    return T


test = [8,3,2,16,3, 3,16,8,2,8,3,2,3,16,8,16]
print(supercount_sort(test))
