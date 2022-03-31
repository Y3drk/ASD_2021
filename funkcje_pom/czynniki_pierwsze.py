def czynniki_pierwsze(n):
    tab = []
    d = 2
    tmp = n
    while d <=  n and tmp > 1:
        if tmp % d == 0:
            tab += [d]
            while tmp % d == 0:
                tmp //= d

        d += 1

    return tab


print(czynniki_pierwsze(42))