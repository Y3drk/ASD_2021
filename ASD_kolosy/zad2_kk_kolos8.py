class NIEkarta:
    def __init__(self,cena,wartosc):
        self.cena = cena
        self.wartosc = wartosc

''''#idea : skorzystamy z dynamicznej funkcji f(i,y,p) = najlepsza wartosc uzyskana z wziecia dokładnie y niekart z puli od 0 do i kart i nie przekraczajaca kosztu p

# warunki brzegowe:
# f(i,0,p) = 0
# f(i,1,p) = max po k od 0 do i jesli cena i-tej karty <= p
# f(i,y,0) = 0 bo nie ma nic za darmo na tym swiecie
# f(0,y,p) = wartosc 0 niekarty jesli jej cena <= p

# ogólny zapis funkcji : f(i,y,p) = max(f(i-1,y,p), f(i - 1, y - 1, p - T[i].cena) + T[i].wartosc **)
# ** jesli p >= T[i].cena

# potem z tak wypełnionej tablicy wydobywamy odp

# złożonosc pamieciowa i czasowa O(nxD)'''


def starszy_pasjonat(T,x,D):
    n = len(T)
    DP = [[[-1 for _ in range(D+1)]  for _ in range(x+1)] for _ in range(n)]
    #print(len(DP),len(DP[0]),len(DP[0][0]), D+1,x+1,n+1)
    for i in range(n):
        for p in range(D+1):
            #print(i,p)
            DP[i][0][p] = 0

    for i in range(n):
        for y in range(x+1):
            DP[i][y][0] = 0

    for y in range(x+1):
        for p in range(D+1):
            if T[0].cena <= p:
                DP[0][y][p] = T[0].wartosc
            else:
                DP[0][y][p] = 0

    for i in range(n):
        for p in range(D+1):
            if T[i].cena <= p:
                DP[i][1][p] = max(DP[i][1][p], T[i].wartosc)

    for i in range(1,n):
        for y in range(2,x+1):
            for p in range(1,D + 1):
                DP[i][y][p] = DP[i-1][y][p]
                if T[i].cena <= p:
                    DP[i][y][p] = max(DP[i - 1][y][p], DP[i-1][y-1][p - T[i].cena] + T[i].wartosc)


    '''for plaster in DP:
        print("||||||||")
        for row in plaster:
            print(row)
    print("------")'''
    # tu umiesc implementacje
    ans = get_solution(DP,T,n-1,x,D)
    #print(ans)
    return ans


def get_solution(DP, T, i, y, p):
    if i < 0 or y < 0:
        return []

    if i == 0:
        if p >= T[0].cena:
            return [0]
        return []

    if p >= T[i].cena and DP[i][y][p] == DP[i - 1][y - 1][p - T[i].cena] + T[i].wartosc:
        return get_solution(DP,T,i -1, y - 1, p - T[i].cena) + [i]

    return get_solution(DP, T, i - 1, y, p)


from copy import deepcopy
T = [NIEkarta(5,10), NIEkarta(5,5), NIEkarta(9,1), NIEkarta(10,2)]
cp = deepcopy(T)
x = 2
D = 10
print(starszy_pasjonat(T,x,D),[0,1])

T = [NIEkarta(5,10), NIEkarta(2,5), NIEkarta(4,6), NIEkarta(1,2)]
cp = deepcopy(T)
x = 3
D = 9
print(starszy_pasjonat(T,x,D),[0,1,3])
