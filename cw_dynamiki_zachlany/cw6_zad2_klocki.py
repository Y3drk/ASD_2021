'''Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
[a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim.'''

# pewne podobieństwo do problemu LIS

# idea - f(i) = najdłuzszy ciąg klocków, zawierających się w sobie, kończących się na klocku i
# f(0) = 1
# f(i) = max(po j od 0 do i) { f(j) + 1 | (jeśli) klocek j zawiera klocek i}

# odp = n - f(n - 1) = liczba klocków - najdłuzszy ciąg


def bricks(T):
    n = len(T)
    F = [1]*n
    for i in range(1,n):
        for j in range(i):
            if T[i][0] >= T [j][0] and T[j][1] >= T[i][1] and F[j]+1 > F[i]:
                F[i] = F[j]+1

    return n-max(F)


I = [[1,5],[2,7],[3,4],[1,10],[3,3]]
print(bricks(I))