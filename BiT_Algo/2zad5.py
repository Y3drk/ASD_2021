# 6 i 7 to obowiazkowe z wykładu

'''Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k].
Zamieniono 10 liczb z tej tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne).
 Napisz algorytm, który posortuje tablicę w czasie O(n).'''

# Idea - znajdujemy te 10 liczb i sortujemy je osobno czymkolwiek innym w czasie stałym O(10), a reszte sortujemy countsortem normalnie


def insert_sort(T): #bez wartownika
    n = len(T)
    for i in range(1, n):
        tmp = T[i]
        j = i - 1
        while (j >= 0) and (tmp < T[j]):
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = tmp



def count_sort(T,k):
    n = len(T)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[T[i]] += 1

    for j in range(1,k):
        C[j] += C[j - 1]

    for l in range(n - 1, -1, -1):
        C[T[l]] -= 1
        B[C[T[l]]] = T[l]

    for i in range(n):
        T[i] = B[i]


def task(T,k):
    A = [0]*10
    cnt = 9
    n = len(T)
    for i in range(n):
        if T[i] < 0 or T[i] > k + 1:
            A[cnt] = T[i]
            T[i] = 0
            cnt -= 1

        if cnt == -1:
            break
        #print(A)

    count_sort(T,k+1)
    insert_sort(A)
    ind = 0

    while ind <= 10:
        if A[ind] < 0:
            ind += 1
        else:
            break

    #Z = A[:ind] + T[10:] + A[ind:] #tworzenie wyniku, mozna zrobic bez slicingu
    W = [0 for i in range(n)]
    pointer = 0
    while pointer < ind:
        W[pointer] = A[pointer]
        pointer += 1
    #print(pointer)
    i = pointer
    while i < n - 10 + pointer:
        W[i] = T[i + 10 - pointer]
        i += 1

    while pointer < 10:
        W[n - 10 + pointer] = A[pointer]
        pointer += 1

    #print(Z)
    return W


test = [-3, 2, 4, 7, 5, 6, 2,8 ,1 ,0, 27,-5, 88, -12, 3, 4, 5,6, 34, 30, -6, 5,4,3,7,69,8,77, 4,5]
print(task(test,8))





