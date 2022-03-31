def count_sort(T,k):   #gdzie k oznacza zasieg waystepowania wartosci (od 0 do k-1)
    n = len(T)
    C = [0 for _ in range(k)]   #tworzymy sobie roboczą tablice w ktorej bedziemy przechowywali inf. ile razy dana liczba (indeks = liczba) wystepuje w T -- tablica liczników
    B = [0 for _ in range(n)]   #B bedzie tablicą w której bedziemy tworzyc wynik, narazie zostawiamy ją "pustą"

    for i in range(n):
        C[T[i]] += 1     #uzupełniamy nasza tablice C by spełniała ww. założenie

    for j in range(1,k):     #teraz chcemy inf o ilosci przekształcic na wiedze ile liczb w tablicy T jest mniejsze lub równe liczbie j, zaczynamy od 1 bo wartosc dla 0 jest zawsze poprawna
        C[j] += C[j - 1]       #za kazdym razem dodajemy poprzednia wartosc do nowej i tak to powastaje ( co ma ens, bo wszystkie liczby mniejsze lub równe np. 3 sa tez mnejsze od 4)

    for l in range(n - 1, -1, -1):  #przeglądamy tablice T od tyłu i pytamy ile jest elementów mniejszy lub równych T[l]. Umieszczamy go na pozycji C[T[l]] - 1 (ze wzgledu na indeksowanie od 0)
        C[T[l]] -= 1            #ważna jest redukcja C[l] aby dobrze rozmieszczac liczby i rozrózniac liczby, które już były
        B[C[T[l]]] = T[l]     #warto zauwazyc ze jesli liczby sie powtarzaja to przez to ze idziemy od tyłu to na wiekszym indeksie w B znajdzie sie liczba która wystepowała na wiekszym indeksie w A
    #zatem nasz algorytm jest stabilny

    for i in range(n):   #pozostało już tylko przepisac wynik do naszej tablicy wejściowej
        T[i] = B[i]


test = [1, 3, 2, 4, 0,3,2]   #n elementów z zakresu od 0 do k-1
k = 5
print(test)
print("....")
count_sort(test,k)
print(test)
