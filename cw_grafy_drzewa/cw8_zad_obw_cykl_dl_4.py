''' Proszę podać jak najszybszy algorytm, który znajduje w grafie
cykl długości dokładnie 4 (trywialny algorytm ma złożoność O(n^4), gdzie
n to liczba wierzchołków---chodzi o rozwiązanie szybsze)

PS. W zadaniu 2 chodzi o reprezentację grafu przez macierz sąsiedztwa'''


# idea - graf reprezentujemy jako liste sasiedztwa
# jesli nie zakładamy ze sasiedzi kazdego wierzchołka są posortowani to lepiej to zrobić -> można countsortem bo znamy ogr na liczbe wierzchołków - O(n^2),
# bo potencjalnie możemy miec do czynienia z grafem pełnym

# potem dla kazdej możliwej pary wierzchołków szukamy ich wspolnych sasiadów. Liczba znalezionych w ten sposób cykli możemy wyrazić wzorem:
# max(0, wspólni sasiedzi - 1)
# nasza para w założeniu jest wierzchołkami przeciwnymi w cyklu (na rysunku moglibysmy je połaczyc "przekątną"), zatem ten sam cykl znajdziemy dwa razy
# zatem na koncu nalezy jeszcze wynik podzielic przez dwa

# złożonośc to O(n^3) , gdzie n = |V|


# sortowanie -> jesli potrzebne (brak zał o posortowanej liscie sasiadów)

def count_sort(T,k):   #gdzie k oznacza zasieg waystepowania wartosci (od 0 do k-1)
    n = len(T)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[T[i]] += 1

    for j in range(1,k):
        C[j] += C[j - 1]

    for l in range(n - 1, -1, -1):
        C[T[l]] -= 1
        B[C[T[l]]] = T[l]

    for i in range(n):
        T[i] = B[i]



def find_cycles_l4(Graph):
    n = len(Graph)
    for i in range(n):
        count_sort(Graph[i],n)

    print(Graph)
    #właściwy mechanizm znajdywania cyklu
    cycles = 0
    for v1 in range(n):
        for v2 in range(v1+1,n):   #trzeba uważać, żeby nie sprawdzać danej pary dwa razy, ale tak czy siak możemy znaleźć ten sam cykl dwa razy
            common_neigbours = 0
            p1, p2 = 0, 0
            tmp = [v1]
            flag = False
            while p1 < len(Graph[v1]) and p2 < len(Graph[v2]):
                if Graph[v1][p1] < Graph[v2][p2]:
                    p1 += 1

                elif Graph[v1][p1] > Graph[v2][p2]:
                    p2 += 1

                else:
                    common_neigbours += 1
                    tmp += [Graph[v1][p1]]
                    if flag:
                        tmp += [v1]
                        flag = False
                    else:
                        tmp += [v2]
                        flag = True
                    p1 += 1

            if len(tmp) >= 4:
                print("Sprawdzalismy:",v1,v2)
                print(tmp)  # jesli sprawdzane wierzchołki sa składowymi wiecej niz jednego cyklu to print bedzie brzydszy, ale na pewno mozna to poprawic - TO IMPROVE, szczegół implementacyjny
                print("----")
            cycles += max(0,common_neigbours - 1)

    return cycles // 2


test = [[1,2],[0,6],[0,6,3,5],[2,4],[3,5],[2,7,6,4],[1,2,5],[5,8],[10,7,9],[8,10],[8,9,11],[10]]
print(find_cycles_l4(test))

