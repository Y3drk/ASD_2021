''' Zad obw 1
Prosze zaimplementować jak najszybszy algorytm sortujący n-elementową tablicę zawierająca liczby ze zbioru {0,1,2,...n^2 - 1}

Idea -
zapisujemy wszystkie liczby w systemie o podstawie n. Dzięki temu, że znamy maks wartość elementów mamy pewność, że bedzie to zapis w dwóch czesciach, pierwsza* n^0 + druga * n^1
czyli nie przekroczy wartosci n^2 - 1.
Tak zapisane liczby sortujemy radix sortem od konca, stosujac wewnątrz count sort (bo mamy tylko n róznych wartości)'''


def sys_chng(a, b):
    index = -1
    tab = []
    n = 0
    while b ** n <= a:
        tab += [0]
        n += 1

    while a != 0:
        tab[index] = a % b
        a //= b
        index -= 1

    return tab


def sys_to_decimal(tab, sys):
    n = len(tab)
    num , tmp = 0, 0
    for i in range(n - 1, -1, -1):
        num += tab[i] * (sys ** tmp)
        tmp += 1
        #print(num)

    return num


def count_sort(T,k, ind):
    n = len(T)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[T[i][ind]] += 1

    for j in range(1,k):
        C[j] += C[j - 1]

    for l in range(n - 1, -1, -1):
        C[T[l][ind]] -= 1
        B[C[T[l][ind]]] = T[l]

    for i in range(n):
        T[i] = B[i]

    return T


def radix_sort(T):
    n = len(T)
    for i in range(n):           #przekształcamy liczby na zapis w systemie o podstawie n
        T[i] = sys_chng(T[i],n)

    s = len(T[0])

    for j in range(s - 1,-1, -1):   #radix sort
        T = count_sort(T,n, j)

    for k in range(n):   #przywracamy normalne wartości
        T[k] = sys_to_decimal(T[k],n)

    return T


test = [56, 8, 17, 31, 23, 44, 61, 47]
print(test)
print("Mieli mieli...")
print(radix_sort(test))
print("sheesh")