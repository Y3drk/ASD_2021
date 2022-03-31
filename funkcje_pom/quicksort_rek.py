def quicksort(T, l, p):
    i, j = l, p
    x = T[(l + p) // 2]

    while i <= j:
        while T[i] < x:
            i += 1
        while T[j] > x:
            j -= 1

        if i <= j:
            T[j], T[i] = T[i], T[j]
            i += 1
            j -= 1

    if l < j:
        quicksort(T, l, j)

    if i < p:
        quicksort(T, i, p)

    return T

'''test = [19,3,29,7,11,5,13,2,23]
print(quicksort(test,0 , len(test)-1))


print("----")
print(T[l:p + 1])
print("po operacji:",T)
print("left")
print("right")'''