from zad3testy import runtests
#problem rozwiążę dynamicznie
# (1) posortuje tablice otrzymanych liczb (siła rzeczy musimy ją przejść od początku do końca)
# skorzystam z funkcji f(i) = minimalny koszt przejscia od 0 do i włącznie, jeśli takie przejście jest możliwe
# warunek brzegowy f(0) = 0
# zapis rekurencyjny f(i) = max (po k od 0 do i-1 włącznie) {f(k) + | P[k] - P[i]| jeżeli przejście z k do i jest możliwe }

#złożoność - pamięciowa O(n^2 + n) - tablice DP i checker, czasowa O(n^2) - narzucone przez obliczanie funkcji f(i) oraz sprawdzanie możliwosci przejscia z liczby do liczby.

def find_cost(P):
    # tu prosze wpisac wlasna implementacje
    P.sort()  #O(nlogn)
    n = len(P)
    F = [float('inf') for _ in range(n)]
    Checker = [[True]*n for i in range(n)] # tablica sprawdzajaca czy mozemy przeskoczyc z danej pozycji na inna

    for i in range(n):   #uzupełnienie tablicy Checker  O(n^2)
        for j in range(i + 1,n):
            res = checker(P[i],P[j])
            Checker[i][j] = res
            Checker[j][i] = res

    F[0] = 0
    for a in range(1,n):
        for b in range(a):
            if Checker[a][b]:
                F[a] = min (F[a], F[b] + abs(P[a] - P[b]))
    if F[n-1] == float('inf'):
        return -1
    else:
        return F[n-1]

#zał. długość liczby uznaję za wartość stałą, bo nie są to wielkości duże dla komputera (no kurwa błagam liczby rzedu 10^18 maja 18 cyfr to co to jest)
# stad złożonośc funkcji checker to O(stała1*log(stała1) + stała2*log(stała2) + stała1 + stała2) ~~ O(1)
def checker(num1, num2):
    t1, t2 = [], []
    while num1 > 0:
        t1 += [num1%10]
        num1 //= 10

    while num2 > 0:
        t2 += [num2%10]
        num2 //= 10

    t1.sort()
    t2.sort()
    i, j = 0, 0
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            i += 1
        elif t1[i] > t2[j]:
            j += 1

        else:
            return True

    return False

#TZW GOWNo

runtests(find_cost) 
