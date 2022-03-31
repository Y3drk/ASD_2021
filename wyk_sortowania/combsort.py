def combsort(T):
    swapped = True
    n = len(T)
    gap = n
    while gap > 1 or swapped:
        gap = max(int(gap / 1.3), 1)
        if gap == 9 or gap == 10:  #wstawka do combsort 11
            gap = 11
        top = n - 1 - gap
        swapped = False
        for i in range(top + 1):
            j = i + gap
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
                swapped = True

    return T


T = [7,4,55,67,8,2,3,44,12,1,2,99]
print(combsort(T))