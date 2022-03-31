def nwd (l1, l2):
    if l1 >= l2:
        a, b = l1, l2
    else:
        a,b = l2, l1

    while b != 0:
            c = a % b
            a, b = b, c

    return a


print(nwd(14,58))
