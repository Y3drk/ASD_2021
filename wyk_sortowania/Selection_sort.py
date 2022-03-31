def select_sort(T):
    n = len(T)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if T[j] < T[mini]:
                mini = j

        T[mini], T[i] = T[i], T[mini]

    return T

T = [7,4,55,67,8,2,3,44,12,1,2,9]
print(select_sort(T))