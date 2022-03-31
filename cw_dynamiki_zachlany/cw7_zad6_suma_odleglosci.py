'''Zadanie 6. (suma odległości)
Dana jest posortowana tablica A zawierająca n liczb i celem jest wyznaczenie liczby
x takiej, że wartość ∑n−1i=0 |A[i]−x| jest minimalna.
Proszę zaproponować algorytm, uzasadnićjego poprawność oraz ocenić złożoność obliczeniową'''

# idea - wziac x jako srednia liczb z A

# dlaczego to działa?
# wyrazenie |A[i]−x| mozemy potraktowac jako metryke euklidesowa. Oczywistym jest, że wybór liczby mniejszej niz MIN z A lub większej niz MAX z A jest niepoprawne.
# Co z wartosciami pomiędzy ?
# odległość to długosc danego przedziału, warto zauwazyc, że srednia zalezy nie tylko od zakresu danych, ale i od gęstosci ich rozmieszczenia,
# jesli łaczylisbysmy ze soba skrajne liczby w przedziały zauważylibysmy, że srednia miesci się w kazdym tak wyznaczonym przedziale,
# zatem łaczna suma naszych wartosci gdyby x = srednia jest po prostu suma długosci tych przedziałow,
# jesli wybralibysmy inna wartosc, to mogłaby ona nie zawierac sie w któryms z przedziałow i wtedy oprócz ich sumy nalezałoby jeszcze
# dodac odległosc obranego punktu od przedzialów w których sie nie zawiera.

#złożonosc O(n) (dodatkowe O(n) to tylko moja fanaberia, aby jeszcze policzyc ta minimalna sume)


def average(A):
    n = len(A)
    sm = 0
    for i in range(n):
        sm += A[i]

    avg = sm / n
    res = 0
    for j in range(n):
        res += abs(A[j] - avg)

    return avg, res


test = [0,2,7,9,10]
result = average(test)
print("Znaleziona wartosc x:",result[0],"uzyskana minimalna suma:",result[1])

