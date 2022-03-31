# Jędrzej Ziebura

# posortujemy przedziały (zapamiętując ich pierwotne połozenie)

# skorzystamy z funkcji dynamicznej f(i,j) = najwieksze mozliwe przecięcie składające sie z j przedziałów i konczące się w i-tym przedziale,
# w którym bedziemy również zapisywac dane przeciecie

# warunki brzegowe:
# f(i,0) = 0
# f(i,1) = zakres przedziału

# f(i,j) = max (po l od j-2 do i - 1) {jesli przedział lty i dotychczasowy rezulat sie przecinaja} [długosc obecnego przeciecia, długosc nowego przeciecia]

# po wykonaniu funkcji przechodzac tablice zapisujaca wyniki i na tej podstawie odzyskamy wynik

# złozonosc O(n^2 * k)


from zad3testy import runtests


def przeciecie(int1, int2):
    if int1[0] >= int2[1] or int1[1] <= int2[0]:
        return False, None

    elif int1[0] <= int2[0] and int1[1] >= int2[1]:
        return True, int2

    elif int1[0] >= int2[0] and int1[1] <= int2[1]:
        return True, int1

    elif int1[0] >= int2[0] and int1[1] >= int2[1]:
        return True, [int1[0], int2[1]]

    elif int1[0] <= int2[0] and int1[1] <= int2[1]:
        return True, [int2[0], int1[1]]


def kintersect(A, k):
    n = len(A)
    F = [[[-1, None] for _ in range(k + 1)] for _ in range(n)]

    for i in range(n):
        A[i] = [A[i][0], A[i][1], i]

    A.sort()  # O(nlogn)

    for i in range(n):
        F[i][0] = [0, None]
        F[i][1] = [A[i][1] - A[i][0], [A[i][0], A[i][1]]]

    for j in range(2, k + 1):
        for i in range(j - 1, n):
            for l in range(j - 2, i):
                int1 = (A[i][0], A[i][1])
                int2 = F[l][j - 1][1]
                if int2 != None:
                    tmp = przeciecie(int1, int2)
                    if tmp[0]:
                        if tmp[1][1] - tmp[1][0] >= F[i][j][0]:
                            F[i][j][0] = tmp[1][1] - tmp[1][0]
                            F[i][j][1] = tmp[1]

    best = -1
    best_int = None
    border = None
    for i in range(n):
        if F[i][k][1] != None and F[i][k][0] > best:
            best = F[i][k][0]
            best_int = F[i][k][1]
            border = i

    res = []
    for i in range(border+1):
        if A[i][0] <= best_int[0] and A[i][1] >= best_int[1]:
            res.append(A[i][2])

    """Miejsce na Twoją implementację"""
    return res


runtests(kintersect)
