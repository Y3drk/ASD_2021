# 16_17_1 to bucket sort na listach

'''. Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).'''

#podobna sytuacja jak w żołnierzach, tak samo najpierw znajdziemy indeksy elemntów from i to, a potem przechodzac przez ten fragment dodamy elementy.
# Wiemy, że wszystkie elementy miedzy from i to beda poprawne, ponieważ partition wewnątrz quickselecta przeniesie el < from na lewa strone from i el> to na prawa strone to
# algorytm mozna usprawnic magicznymi piątkami, ale nasze założenie kolosowe jest takie, że quickselect działa w czasie liniowym


def partition_random(T, p, r):  #bonus zeby łatwiej było sprawdzac wynik
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


def sum_from_to(T,beg, end):
    n = len(T)
    beg = quickselect(T, 0, n - 1, beg)
    print("beg:",beg, T[beg])
    end = quickselect(T, beg, n - 1, end)
    print("end:", end, T[end])
    sum_from_to = 0
    for i in range(beg,end+1):
        sum_from_to += T[i]

    return sum_from_to


#Złożoność - dwókrotnie wywołujemy quickselecta i raz przechodzimy po fragmencie tablicy, zatem O(3n)

test = [17, 31, 3, 8, 11, 19, 2, 5, 23, 13, 7, 29]
test_ctrl = [17, 31, 3, 8, 11, 19, 2, 5, 23, 13, 7, 29]
quick_sort_mem2(test_ctrl,0, len(test_ctrl)- 1)
print(test_ctrl)
print(sum_from_to(test,3,6))