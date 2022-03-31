'''Dana jest tablica A oraz liczba k. Znaleźć liczbę różnych par elementów z tablicy A o różnicy równej k.

Przykład: Dla tablicy [7,11,3,7,3,9,5] oraz k = 4 odpowiedź to 3
'''

# idea - sortujemy tablice, potem przechodzimy po niej "gąsienicą" odpowiednio przesuwając dwa wskaźniki. Jeśli T[j]- T[i] == k i T[i] + T[j] nie jest identyczna
# z suma, ktora wczesniej spełniała zał. to znalexlismy kolejna unikalna pare, zatem zwiekszamy counter


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


def caterpillar(T,k):
    n = len(T)
    quick_sort_mem2(T,0, n-1)
    i, j = 0, 1
    counter = 0
    last_sum = 0
    while j < n:
        if T[j] - T[i] < k:
            j += 1

        elif T[j] - T[i] > k:
            i += 1

        else:
            if T[j] - T[i] == k and T[j] + T[i] != last_sum:
                counter += 1
                last_sum = T[j] + T[i]  #czemu to zadziała? - dla okreslonej róznicy k, okreslona suma liczb jednoznacznie okresla parę.
                i += 1

            else:
                i += 1

    return counter


test = [7,11,3,7,3,9,5]
print(caterpillar(test,4))
