def palindrom(l):

    pom = list(l)
    k = 0

    while k <= (len(l) / 2):
        if pom[k] == pom[-k - 1]:
            k +=1
        else:
            return False

    return True