def ile_cyfr(x):
    dlg = 0

    while x != 0:
        dlg +=1
        x //= 10

    return dlg