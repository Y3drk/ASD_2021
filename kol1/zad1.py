# Jędrzej Ziebura

# Opis algorytmu:
# 1) Przepisujemy wszystkie elementy do nowej roboczej tablicy I (złożoność O(n^2) i O(n^2) dodatkowej pamieci).
# 2) Chcemy znaleźć n elementów które umieścimy na przekątnej głównej, więc wykonujemy dwukrotnie quickselect na tablicy I, raz dla elementu (n^2 - n)/ 2
# a raz dla elementu (n^2 + n)/2. Są to pozycje odp. pierwszego z elementów spełniających warunki umieszczenia na przekątnej głównej i pierwszy element większy od
# wczesniej wymienionych elementów. Dzięki partition wewnątrz quickselect'a mamy pewność, że w przedziale [(n^2 -n)/2, (n^2 + n)/2) znajda się poprawne wartośći. Zapamiętujemy
# Zapamiętujemy ww. pozycje (złożoność O(2*n^2) + O(1) pamięci na dwa "wskaźniki") .
# 3) Odpowiednio wpisujemy elementy z powrotem do tablicy T, czyli w i-tym wierszu, dla pól przed T[i][i] wpisujemy elementy z początkowej części tablicy, element T[i][i] to element z ww. zakresu
# [(n^2 -n)/2, (n^2 + n)/2), a elementy po T[i][i] z końcowej części tablicy I (złożoność O(n^2) + O(1) dodatkowej pamięci na sterowanie wstawianiem elementów)

# Złożoność:
# czasowa - O(n^2)
# pamięciowa - O(n^2)


from zad1testy import runtests


def partition_spec(T, l, r,ind):  # przerobione tak aby mogło przyjmowac indeks elementu którego chcemy przyjąc za pivota
    x = T[ind]
    T[ind], T[r] = T[r], T[ind]
    i = l - 1
    for j in range(l, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quickselect(T, p, r, k):  # przystosowany by zwracac obecny indeks połozenia tej liczby
    if p == r:
        return p

    q = partition_spec(T, p, r, r)

    if q == k:
        return q

    elif k < q:
        return quickselect(T, p, q - 1, k)

    else:
        return quickselect(T, q + 1, r, k)


def Median(T):

    n = len(T)

    if n == 1:
        return

    I = [0 for i in range(n*n)]
    ind = 0
    for i in range(n):
        for j in range(n):
            I[ind] = T[i][j]
            ind += 1

    beg = quickselect(I,0,n*n - 1,int((n*n - n)/2))
    end = quickselect(I,beg + 1,n*n - 1, int((n*n + n)/2))

    lower, mid, higher = 0, beg, end

    for i in range(n):
        for j in range(n):
            if j < i:
                T[i][j] = I[lower]
                lower += 1
            elif j == i:
                T[i][j] = I[beg]
                beg += 1
            else:
                T[i][j] = I[higher]
                higher += 1

    # tu prosze wpisac wlasna implementacje
    return

runtests( Median )
