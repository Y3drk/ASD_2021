'''Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
być zarówno dodatnie jak i ujemne):
n1 + n2 + ... + nk
Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
najmniejszy.

 !!! Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie wybiera kolejność dodawań. !!!

Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej wystepują w sumie;
zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
wejściowej:
[1,−5, 2]
funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.'''


# skorzystamy z funkcji dynamicznej --> f(i,j) = najmniejszy z najwiekszych wyników tymczasowych dodawań elementów od i do j

# odp to wartosc f(0, n-1)

# warunki brzegowe
# f(i,i) = abs(tab(i))
# f(i, i+1) = abs(tab(i) + tab(i + 1))

# f(i,j) = min po l od 0 do j-i { max [ f(i + l + 1, j), f(i, i+l), |suma od i do j| ] }

# złożonosć O(n^3)


def opt_sum(tab):
    n = len(tab)
    F = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        F[i][i] = abs(tab[i])

    for i in range(n - 1):
        F[i][i + 1] = abs(tab[i] + tab[i + 1])

    S = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        S[i][i] = tab[i]

    for a in range(n):
        for b in range(a + 1, n):
            S[a][b] = S[a][b - 1] + tab[b]

    for j in range(1, n):
        for i in range(j - 2, -1, -1):
            for l in range(j - i):
                F[i][j] = min(max(F[i + l + 1][j], F[i][i + l], abs(S[i][j])), F[i][j])

    return F[0][n - 1]


t1 = [1, -5, 2]
t2 = [-3, 2, 7, 1, 8, -16]
t3 = [1, 2, 3, 4, -5]
print("answer:", end=" ")
print(opt_sum(t1))
print("----")
print("answer:", end=" ")
print(opt_sum(t2))
print("----")
print("answer:", end=" ")
print(opt_sum(t3))
