def generowanie(zbior , n, k):

    if zbior[k - 1] < n:
        j = k - 1
    else:
        j = k - 2

        while j >= 0 and zbior[j] + 1 == zbior[j + 1]:
            j -= 1

    if j >= 0:
        zbior[j] += 1
        for i in range(j + 1, k - 1):
            zbior[i] = zbior[i - 1] + 1

    return zbior

#generuje kolejny zbiór

print(generowanie([2,3],3, 2))

