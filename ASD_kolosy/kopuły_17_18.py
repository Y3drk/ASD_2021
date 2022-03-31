'''8. Miasto chce pokry¢ park kopuªami antysmogowymi. Park ma ksztalt prostok¡ta podzielonego na T odcinków jednakowej długosci.
Firma produkuj¡ca kopuªy ma do dyspozycji
okre±lone produkty, dane jako trójki (ai,bi,ci) dla i-tej kopuªy, gdzie a i b to ko«ce kopuª
(przy czym a ≤ b), a c to koszt danej kopuªy. Chcemy pozna¢ koszt (i czy si¦ w ogóle
da, maj¡c do dyspozycji dane kopuªy) pokrycia wszystkich odcinków parku, przy czym
ze wzgl¦dów technicznych kopuªy nie mog¡ na siebie nachodzi¢. Nale»y u»y¢ funkcji f(x),
która wyznacza minimalny koszt pokrycia od odcinka 1 do odcinka x oraz poda¢ wzór
rekurencyjny tej funkcji.'''

# sortujemy kopuły po zasiegach

# uzywamy rekurencyjnej funkcji f(i) = najtanszy koszt pokrycia parku do bi z uzyciem kopuły itej

# f(0) = c0
# f(i) = min (po k od 0 do i-1) [ jesli kta kopuła konczy sie tam gdzie zaczyna ita] {f(k) + ci}


def domes(K,park):
    K.sort()

    if K[0][0] > park[0]:
        return False

    n = len(K)
    F = [float('inf') for _ in range(n)]
    F[0] = K[0][2]

    for i in range(1,n):
        for k in range(i):
            if K[k][1] == K[i][0]:
                F[i] = min(F[i], F[k] + K[i][2])

            elif K[i][0] == park[0]:
                F[i] = min(F[i], K[i][2])


    print(F)
    best = float('inf')
    for i in range(n-1, -1, -1):
        if K[i][1] >= park[1]:
            best = min(best, F[i])

    if best == float('inf'):
        return False

    else:
        return best


poczatek_parku_koniec_parku0 = (0,1)
T0 = [(0,0.4,1),(0,1,1500),(0.5,1,1)]
print(domes(T0,poczatek_parku_koniec_parku0))
print("-----")
poczatek_parku_koniec_parku1 = (0,10)
T1 = [(3,4,2),(2.5,5.5,1),(9,10,888),(0,1,2),(0,2.5,1),(7,9,4),(1,3,6),(8,11,8),(4,8,64),(5.5,7,3)]
print(domes(T1,poczatek_parku_koniec_parku1))
print("-----")
T2 = [(0,2,4), (0,1,1), (4,8,1), (1,9,1), (8,10,2), (2,5,2)]
poczatek_parku_koniec_parku2 = (0,10)
print(domes(T2,poczatek_parku_koniec_parku2))
print("-----")
T3 = [(0,1,1), (0,2,4), (1,9,1), (2,8,1), (8,10,2), (8,10,5), (9,10,2)]
poczatek_parku_koniec_parku3 = (0,10)
print(domes(T3,poczatek_parku_koniec_parku3))
