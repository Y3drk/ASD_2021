'''Sasza kolekcjonuje rosyjskie lalki - matrioszki.
Każda z nich ma określoną wysokość X i szerokość Y, dane liczbami naturalnymi dodatnimi.
Jedną matrioszkę można włożyć do drugiej, jeżeli ma od niej mniejszą zarówno wysokość, jak i szerokość.
Sasza zastanawia się, jaki jest najdłuższy ciąg matrioszek, które może powkładać w siebie po kolei. Pomóż mu znaleźć odpowiedź na to pytanie.
'''


# jedna idea jest Lukasza i to graf skierowany ze specyficznym DFS'em szukajacym najdluzszej sciezki, gdzie krawedz miedzy wierzchołkami to zachodzenie relacji porzadku

# druga idea - dynamik -->
# 1) sortowanie matrioszek po jednym z wymiarów, np. po X
# 2) funkcja f(i) = najdłuzszy ciag matrioszek, w którym i-ta laleczka jest zewnetrzna (algorytm LIS dla drugiego wymiaru, dla przykładu y)
# f(i) = max (po t od 0 do i) { f(t) + 1}

# Złozonosc - pamieciowa O(n), czasowa O(nlogn)

def Sasha_and_his_dolls(M):
    n = len(M)
    M.sort()  #wewnetrzne sort pythonka posortuje to najpierw po pierwszym elemencie a potem po drugim O(nlogn)
    #print(M)
    #algorytm LiS działajacy w czasie O(nlogn)
    F = []
    F += [M[0]]
    for i in range(1, n):
        l, r = 0, len(F) - 1
        # print("analizowany element:",T[i])
        while l <= r:  # bin search tablicy F
            mid = (l + r) // 2
            # print(F[mid])

            if M[i][1] > F[mid][1]:  # standardowe operajce z binsearcha
                l = mid + 1  # dlaczego min z mida? Bo jesli tak, to analizowany element może przedłuzyc ciag konczacy sie elementem z F[mid], chociazby własnie tym minimalnym
                # i wtedy według naszej logiki powinien byc w kolejnej podtablicy
            elif M[i][1] <= F[mid][1]:  # przeciwny przypadek sytuacji z wyzej, element nie moze przedłuzyc nic z ciagu konczacego sie elementem z F[mid], i powinien byc albo w
                r = mid - 1  # F[mid] albo w podtablicy wczesniejszej dlatego przesuwamy wskaznik bs

        if l < len(F) and M[i][1] <= F[l][1]:  # jesli nie wyszlismy poza zakres tablicy w bs i ww. a element wciaz nie przedłuza ciagu konczacego sie któryms z el. F[mid]
            if M[i][1] < F[l][1] and M[i][0] < F[l][0]:
                F[l] = M[i]  # a jednoczesnie stosujac bs zawezilismy pole poszukiwan do niego to znaczy, ze musimy umiescic go w dokladnie tej podtablicy
        elif l >= len(F) and F[len(F)- 1][0] < M[i][0]:  # wpp element przedłuża ciag konczacy sie któryms z el. F[mid] i mozemy dodac go jako osobna podtablice
            F += [M[i]]

    #print(F)
    return len(F)


test = [(1,1),(3,2),(1,7),(3,3),(4,2),(8,8),(6,9),(2,3),(7,10)]
print(Sasha_and_his_dolls(test))