'''Zadanie 3. (ładowanie przyczepy)
Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunkówo wagach w1, . . . , wn.
Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K=27).
Proszę podać algorytm zachłanny (iuzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
(ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków.
(Ale jeśli da się np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K−1 używając jednego ładunku,
to lepsze jest to pierwsze rozwiązanie)'''

# zadanie a) wi sa potegami 2

# idea - zachłannie bierzemy najwiekszy możliwy ładunek

# czemu to działa / dowód poprawnosci
# falisz dowodził dodawaniem binarnym, a z polskiego na nasze uzywajac mniejszych ładunków w miejsce najwiekszego to mozemy albo
# uzyskac taka sama mase zuzywajac wiecej ładunków, albo nie uzyskać jej wgl co juz jest dramatycznie gorsze.

# ciche założenie : wagi ładunków w tablicy Loads sa juz posortowane niemalejąco

# złożoność : O(ładownosc + ładunki) , bo kazdy ładunek rozwazymy maksymalnie raz


def lorry_load(Capacity,Loads):
    n = len(Loads)
    for i in range(n):
        Loads[i] = [Loads[i],0]

    in_truck = []
    weight = 0
    ind = n - 1
    while Capacity > 0:
        #print("pozostało ładownosci:",Capacity)
        for i in range(ind, -1, -1):
            if Loads[i][0] <= Capacity and Loads[i][1] != 1:
                in_truck += [Loads[i][0]]
                weight += Loads[i][0]
                Loads[i][1] = 1
                Capacity -= Loads[i][0]
                ind = i - 1
                break

            elif i == 0:
                ind = -1

        if Capacity != 0 and ind == -1:
            break

    return weight, in_truck


test = [2,2,2,8,8,16,32,32,128]
k = 41
result = lorry_load(k,test)
print("Rozwiazanie a")
print("Załadowana waga:",result[0],"i załadowane paczki:",result[1])


# rozwiazanie b - pewne podobieństwo do problemu plecakowego
# dosłownie plecakowy z dwoma róznicami, (1) zamiast maksymalnej wagi jest ładownosc ciezarówki oraz (2) jesli wagi w podroziwazanu sa takie same to wolimy ta ktora mozna uzyskac mniejsza iloscia przedmiotów

def ambitious_lorry_loading(Weights,Capacity):
    n = len(Weights)
    F = [[[0, 0]]*(Capacity + 1) for _ in range(n)]

    for w in range(Weights[0], Capacity + 1):
        F[0][w] = [Weights[0],1]

    for i in range(1,n):
        for w in range(1, Capacity + 1):
            F[i][w] = F[i - 1][w]
            if w >= Weights[i]:
                if F[i][w][0] == F[i - 1][w - Weights[i]][0] + Weights[i]: #(2)
                    if F[i][w][1] > F[i - 1][w - Weights[i]][1] + 1:
                        F[i][w] = [F[i - 1][w - Weights[i]][0] + Weights[i],F[i - 1][w - Weights[i]][1] + 1]

                elif F[i][w][0] < F[i - 1][w - Weights[i]][0] + Weights[i]:
                    F[i][w] = [F[i - 1][w - Weights[i]][0] + Weights[i], F[i - 1][w - Weights[i]][1] + 1]


    '''for h in range(n):
        print(F[h]) #testowe printy
    print("-------------")'''

    #wyciaganie wyniku
    for i in range(Capacity,0,-1):
        if F[n-1][i][1] <= Capacity:
            return F[n-1][i]

    return


test = [2,2,2,8,8,16,32,32,128]
test2 = [2,5,8,10,13,17,23,46,56]
k = 58
result = ambitious_lorry_loading(test2,k)
print("Rozwiazanie b")
print("Załadowana waga:",result[0],"i załadowane paczki:",result[1])

