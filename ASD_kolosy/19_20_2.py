#idea - korzystajac z quick selecta znajdujemy zołnierza, który po posortowaniu tablicy znajdowałby sie na pozycji p, natepnie wykonujemy partition gdzie pivotem jest wartosc T[p],
#czynnosc powtarzamy dla zołnieza , który po posortowaniu znajdowałby sie na pozycji q, z tym ze mozemy juz szukac tylko na pozycjach p+1,n -1 oraz
# w partition możemy juz nie dotykac pozycji 0 do p.

#nastepnie albo sliceujemy nasza tablice, co pewnie jet illegal, albo tworzymy nowa, o długosci q - p i tam wpisujemy naszych szukanych zołniezy, jesli dobze rozumiem
#tłumaczenie falisza z wykładu to koszt pamieciowy bedzie taki sam

# złożonosc - wszystkie czynnosci wykonywane będa w czasie liniowym. Jedyna watpliowsc moze budzic quickselect, który może ukwadratowić sie dla niekorzystnych danych.
#Problem można wyeliminowac algorytmem magicznych piątek, a bez niego mozna modlic sie o dobre dane :))

def partition_spec(T, l, r, ind):    #przerobione tak aby mogło przyjmowac indeks elementu którego chcemy przyjąc za pivota
    x = T[ind]
    T[ind], T[r] = T[r], T[ind]
    i = l - 1
    for j in range(l, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quickselect(T,p,r,k): #przystosowany by zwracac obecny indeks połozenia tej liczby
    if p == r:
        return p

    q = partition_spec(T,p,r,r)

    if q == k:
        return q

    elif k < q:
        return quickselect(T,p, q - 1, k)

    else:
        return quickselect(T, q + 1, r, k)


def section(T, p, q):
    n = len(T)

    p = quickselect(T, 0, n - 1, p)
    #print(p, T[p])

    #tmp = partition(T, 0, n - 1, p)   tego nie robic - jałowe przejscie
    #print(T)


    q = quickselect(T, p, n - 1, q)
    #print(q, T[q])
    #_ = partition(T, tmp, n - 1, n - q)  tego nie robic - jałowe przejscie
    #print(T)
    Section = [0]*(q-p + 1)
    ind = 0
    for i in range(p, q + 1):
        Section[ind] = T[i]
        ind += 1
        #print(T[i])

    #print(suma, cnt)
    return Section


test = [156,203,200,167,178,189,176,165,185,191,202,139]
print(section(test,3,8))

#1.5 pkt od Lukasza za jałowe przejscia