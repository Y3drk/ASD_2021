def nwd (l1, l2):
    if l1 >= l2:
        a = l1
        b = l2
    else:
        a = l2
        b = l1

    while b != 0:
            c = a % b
            a = b
            b = c

    return a


def nww(l1,l2):
    nww = (l1 * l2) // nwd(l1, l2)

    return nww

print(nww(24,36))



