'''Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje.
Kawałki mają długość w metrach wyrażoną zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n metrów.
Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.'''

# idea - f(i) = najwiekszy mozliwy do uzyskania zysk ze sprzedazy preta o długosci i

# f(0) = 0
# f(i) = max (po k od 0 do i - 1) {f(i - k) + p(k)} , gdzie p jest tablica zysku ze sprzedazy preta danej długosci

# de facto za kazdym razem sprawdzamy jakie ciecie nam sie najbardziej opłaca bazujac na poprzednich rozwiazaniach


def cut_the_pret(P):
    n = len(P)
    F = [0 for i in range(n)]
    S = [-1 for _ in range(n)] #tablica parentów - czyli skad wzielismy optymalne rozwiazanie
    for i in range(1,n):
        best = float("-inf")
        ind = n+1
        for k in range(1,i + 1):
            if best < F[i-k] + P[k]:
                best = F[i-k] + P[k]
                ind = k

        F[i] = best
        S[i] = ind

    #print(F)
    #print(S)
    return F[n-1],S


def print_solution_pret(P):
    n = len(P) - 1
    while n > 1:
        print(P[n], end=' ')
        #print("n=",n)
        n -= P[n]

    return


test = [0,1,5,8,9,10,17,17,20,24,30]
result = cut_the_pret(test)
print("Najlepszy możliwy wynik to:",result[0],"osiagniety z: ",end='')
print_solution_pret(result[1])


