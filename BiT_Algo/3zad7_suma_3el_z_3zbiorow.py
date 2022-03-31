'''Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka a, b, c z odpowiednio A, B, i C, że a + b = c.
 Nie wolno korzystać ze słowników!'''

# 2 pomysły o podobnej złożoności
# Ozn. : n - najdłuzsza , m - srednia, k- najkrótsza

# 1) sortujemy dwie najkrótsze tablice, przechodzimy po najdłuzszej, przechodzimy po najkrótszej robiac binary search po srdeniej -> O(n*k*logm)

# 2) Sortujemy tablice A i B, przechodzimy przez C. Ustawiamy wskaźnik na poczatek A i koniec B, potem odpowiednio je przesuwamy, jesli znajdziemy odp sume to ofc przerywamy
# -> O( aloga + blogb + c(a+b))

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


def find_sum_abc(A,B,C):
    quick_sort_mem2(A,0, len(A) - 1)
    quick_sort_mem2(B,0,len(B) -1)

    for i in range(len(C)):
        lA, rB = 0, len(B) - 1

        while lA < len(A) and rB > -1:

            if A[lA] + B[rB] == C[i]:
                print(A[lA],B[rB],C[i])
                return True

            elif A[lA] + B[rB] < C[i]:
                lA += 1

            elif A[lA] + B[rB] > C[i]:
                rB -= 1

    return False


A = [5, 7, 11,23, 13, 12, 1, 9, 60]
B = [91, 4, 66, 2, 45, 1, 0, 3, 76, 51, 6]
C = [1000, 0, 188]
print(find_sum_abc(A,B,C))