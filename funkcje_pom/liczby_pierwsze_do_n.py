def pierwsze(n):
    lista = []
    for i in range(2,n + 1):
        lista.append(i)

    for x in range(2,n):
        if x in lista:
            pom = 2 * x
            while pom <= n:
                if pom in lista:
                    lista.remove(pom)
                    pom += x
                else:
                    pom += x
    return lista