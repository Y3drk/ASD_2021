'''czołg ma za zadanie przejechac z punktu A=0 do punktu B = x.
dane:
1. czołg spala dokładnie 1 L na 1 km
2. -||- ma pojemnosc baku równa L.
3. P to tablica cen benzyny na kazdej stacji
4. S to tablica odległosci stacji od punktu '''

# zadanie b2) - obliczyć minimalny koszt dotarcia do punktu B, jesli przy kazdym tankowaniu musimy zatankowac do pełna

# problem rozwiazemy dynamicznie

# skorzystamy z funkcji f(i) = minimalna kwota wydana na benzyne potrzebna na dotarcie do punktu i oraz zatankowanie w nim do pełna
# ciche zał. bak ma pojemnosc wystarczająca aby dotrzec do danej stacji w ten czy inny sposób
# f(0) = 0
# f(1) = P[1] * (L - S[1])
# f(i) = min ( po k od S[i] - L do S[i -1]) ( f(k) + P[i] * (S[i] - S[k]))

#złożonosc - czasowa //pesymistyczne// O(n^2)
# pamieciowa - O(n)

def full_tank_fuel(P,S,L):
    n = len(S)
    F = [float('inf') for _ in range(n)]
    F[0] = 0
    for i in range(1,n):  #specjalny case, który sprawdza czy nasze ciche założenie jest uzasadnione
        if S[i] - S[i - 1] > L:
            return -1

    F[1] = P[1] * S[1]

    for i in range(2,n):
        start = i
        for j in range(i):
            if S[i] - S[j] - L <= 0:
                start = j
                break

        for k in range(start,i):
            F[i] = min(F[i], F[k] + P[i] * (S[i] - S[k]))

    #print(F)
    return F[n - 1]


S = [0,6,1,2,4,5,4,3,0]
L = [0,5,15,25,27,29,49,59,64]
limit_D = 20
print(full_tank_fuel(S,L,limit_D))