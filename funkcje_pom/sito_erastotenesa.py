def sito_erastotenesa(n):
    primes = [True for _ in range(n+1)]
    i = 2
    while (i * i) < n:
        if primes[i]:
            for j in range(2*i,n+1,i):
                primes[j] = False

        i += 1

    primes[0],primes[1] = False, False

    T = []
    for i in range(n+1):
        if primes[i]:
            T += [i]

    return T

test = 30
print(sito_erastotenesa(test))
