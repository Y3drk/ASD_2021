#bellman- Ford bez weryfikacji bo nie ma ujemnych cykli, ale ma tez pewne ograniczenia
# 1) nigdy nie weźmiemy niebieskiej karty
# 2) w łapce możemy miec czerwona karte tylko przez x dni, ergo mozemy isc po czerwonych tylko te x dni
# 3) nie zawsze mamy odpowiednio duzo pitosu, zeby gdzieś pójsc

#problemy - każda osobna sciezka po pierwszym kroku ma swój osobny budżet niezalezny od pozostałych scieżek
# pewnie cos jeszcze


#zmiana założen - zawsze stac nas na zakup karty bo na starcie mamy float inf pitosu, ergo nie opłaca sie zatrzymywac, jazdaaaa

# złożonosc narzucona przez Bellamna-Forda O(VE)

def BF_cards(G,s,x,T):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    holding_red = [0 for _ in range(n)]

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u
            if T[v] == 'czerwony':
                holding_red[v] = holding_red[u] + 1

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if T[v] != 'niebieski' and G[u][v] != 0:
                    if T[v] != 'czerwony' or holding_red[u] + 1 <= x:
                        relax(u,v, G[u][v])

    return parent


def get_path(P,ind):
    tmp = []
    while ind != None:
        tmp.append(ind)
        ind = P[ind]

    return tmp[::-1]


def mlodszy_pasjonat(M,A,B,y,D,x,T):
    # tu umieść swoją implementację
    res = BF_cards(M,A,B,x,T)
    #print(res)
    ans = get_path(res,B)

    return ans

from copy import deepcopy

M = [[0,10,0,120,0,0,1],
      [10,0,6,0,0,0,0],
      [0,6,0,7,0,0,0],
      [120,0,7,0,1,0,0],
      [0,0,0,1,0,1,0],
      [0,0,0,0,1,0,1],
      [1,0,0,0,0,1,0]]
T = ["biały","biały","czerwony","czarny","czerwony","czerwony","biały"]

A = 0
B = 3
y = 6
D = 4
x = 0
odp = [0,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

y = 8
x = 1
odp = [0,1,2,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

y = 10
x = 3
odp = [0,6,5,4,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

