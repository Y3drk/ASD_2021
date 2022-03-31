'''Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n.
 Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.'''


def binary_search(T,x):
    n = len(T)
    left, right = 0, n -1
    while left <= right:
        mid = (left + right) // 2
        if T[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    if left < n and T[left] == x:
        return left

    return False


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[
            j] <= x:
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


def are_separate(S1, S2):  #zakładamy ,ze m == S1 i n == S2 oraz m << n
    quick_sort_mem2(S1,0, len(S1)-1)   #sortujemy mniejszy zbiór w czasie O(mlogm) - nie mozemy uzyc countsorta lub bucketa bo nie wiemy nic o danych
    for i in range(len(S2)):
        if binary_search(S1, S2[i]) != False:  #jesli znajdziemy element z S2 w posortowanym S1 to znaczy, że zbiory nie są rozłączne
            return False

    #złożonosc pętli powyżej to O(nlog(m)) i to jest ogolna złożonośc naszego zadania

    return True



'''test = [2,3,5,7,8,11,13,17,19,23]
print(binary_search(test,8))'''

m = [3,9,7,6,4,5,8]
n = [18, 23, 45, 2, 44, 10,88, 17, 1, 2, 100, 16, 30, 35, 13]
print(are_separate(m,n))



