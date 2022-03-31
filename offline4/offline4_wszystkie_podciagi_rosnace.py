'''Proszę zaimplementować funkcję printAllLIS( A ), która otrzymuje na wejściu tablicę liczb naturalnych A i wypisuje na ekran wszystkie najdłuższe ciągi
rosnące oraz zwraca ich liczbę.'''

# idea - modyfikujemy rozwiazanie O(n^2) LIS w ten sposób, że w tablicy Parent zapisujemy indeksy wszystkich elementów, które przedłuzone przez ity element daja
# na ten moment optymalny ciąg. Koszt takiej operacji to O(n^2) czasu i około O(n^2) pamięci
# (zaleznie od charakterystyki wejscia, nie testowałem wszsytkich mozliwych opcji, wiec nwm jak duża bedzie tablica P w pesymistycznym przypadku)
# Potem korzystajac z globalnego licznika i rekurencyjnej funkcji print_solution_ALL wypisujemy wszystkie najdłuższe podciągi i zliczamy ich ilośc
# złożonosc tej czesci zadania zalezy od ilosci "lisów"...
# pesymistyczny "koszt" czasowy pojawia się gdy komórki tablicy Parent sa wieloelementowe, a zwłaszcza gdy zawieraja podobną / identyczną liczbe elementów
# wtedy mamy do czynienia z czyms na kształt "eksplozji kombinatorycznej", bo nasza funkcja musi rozwazyc wszystkie mozliwe poprawne połaczenia,
# czyli funkcja wywoła sie (ilość przedłuzonych elementów przez najwiekszy el) * (ilość przedłuzonych elementów przez drugi najwiekszy el)*...*(ilość przedłuzonych elementów przez drugi najmniejszy el)
# razy...
# Dziękuję Nikodemowi Korohodzie, który zgodził się żebym użył jego matematycznej interpretacji ww. zagadnienia

# Rozważmy ciąg typu 5,4,3,2,1,10,9,8,7,6 itp.
# Oznaczmy długość jednego 'interwału' (podciągu spójnego, malejącego) jako 'k',
# wtedy wszystkich najdłuższych rosnących ciągów jest k^(n/k)

# funkcja f(x)=x^(1/x) osiąga maximum w x=e
# zatem maksymalna wartość k^(n/k)=(e^(1/e))^n i to jest maksymalna złożoność czasowa


def print_solution_ALL(T,P,ind,tmp):
    global counter
    if ind == -1:
        for i in range(len(tmp) - 1, -1, -1):
            print(T[tmp[i]]," ", end='')
        print()
        counter += 1
        return

    if len(P[ind]) == 1:
        print_solution_ALL(T, P, P[ind][0], tmp + [ind])
    else:
        for i in range(len(P[ind])):
            print_solution_ALL(T,P,P[ind][i],tmp + [ind])


def printALLLIS(T):
    global counter
    n = len(T)
    F = [1 for i in range(n)]
    P = [[-1] for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if T[i] > T[j] and F[i] < F[j] + 1:
                P[i] = [-1]
                F[i] = F[j] + 1
                P[i][0] = j

            elif T[i] > T[j] and F[i] == F[j] + 1:
                F[i] = F[j] + 1
                P[i] += [j]


    checker = max(F)
    if checker == 1:
        for i in range(n):
            print(T[i])

        return n

    counter = 0
    for i in range(n - 1, -1, -1):
        if F[i] == checker:
            tmp = []
            print_solution_ALL(T,P,i,tmp)

    return counter


test2 = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
test = [3, 1, 5, 7, 2, 4, 6, 9, 16, 8]
test3 = [2, 1, 4, 3]
test4 = [8,7,6,5,4,3,2,1]
#print("T:",test3)
print(printALLLIS(test3))
print("----")
print(printALLLIS(test2))
print("----")
print(printALLLIS(test4))
