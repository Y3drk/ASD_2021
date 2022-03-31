'''. Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.'''

#idea -
# 1) przepisujemy te sufit z logn wartosci parzystych do nowej tablicy - O(n)
# 2) sortujemy je za pomocą quicksort - O(logn * log(logn))
# 3) przepisujemy je z powrotem do tablicy wejsciowej - ofc w odpowiednie miejsca - O(n)

# Złożonosc - n > logn * log(logn) zatem ogolna złożonosc wynosi O(n)


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


def sorting_even_only(T):
    import math
    n = len(T)
    I = [0 for _ in range(math.ceil(math.log2(n)))]  #nowa struktura na wyłapane parzyste
    ind_b = 0
    for i in range(n):   # krok (1)
        if T[i] % 2 == 0:
            I[ind_b] = T[i]
            ind_b += 1

    quick_sort_mem2(I, 0, len(I) - 1) #krok (2)

    ind_e, i = 0, 0
    New = []
    while i < n:    # krok (3)
        if T[i] % 2 == 1:
            if ind_e >= ind_b:
                New += [T[i]]
                i += 1

            elif ind_e < ind_b and T[i] < I[ind_e]:
                New += [T[i]]
                i += 1

            elif ind_e < ind_b and T[i] > I[ind_e]:
                #print(T[i], I[ind_e])
                New += [I[ind_e]]
                ind_e += 1

        elif T[i] % 2 == 0 and ind_e < ind_b and I[ind_e] < T[i + 1]:
            #print(T[i],I[ind_e])
            New += [I[ind_e]]
            ind_e += 1
            i += 1

        else:
            i += 1

    return New


test = [1,2,5,7,9,11,13,8,30,19,21,23,18,27,29,31]
print(sorting_even_only(test))

