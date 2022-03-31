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


tab = [7, 23, 13, 29, 19, 8, 2, 1]
print(insert_sort(tab))

# z wartownikiem
'''x = T[i]
        T[0] = x
        j = i - 1
        while x < T[j]:
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = x'''