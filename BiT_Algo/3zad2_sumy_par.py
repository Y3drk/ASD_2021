'''Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te liczby na n par w taki sposób,
że podział będzie miał najmniejszą maksymalną sumę liczb w parze.
Przykładowo, dla liczb (1, 3, 5, 9) możemy mieć podziały ((1,3),(5,9)), ((1,5),(3,9)), oraz ((1,9),(3,5)).
Sumy par dla tych podziałów to (4, 14), (6, 12) oraz (10, 8),
 w związku z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego, że ostatni podział ma najmniejszą maksymalną sumę.'''

#idea - algorytm zachłanny - sortujemy tablice i tworzymy pary z elementu najmniejszego i najwiekszego ( i oraz n - 1 - i). Wtedy maksymalna suma bedzie najmniejsza
#dowód jest dosyc skomplikowany dlatego po prostu go tu przekleje
'''Dowód nie wprost: Załóżmy, że nasza strategia nie jest optymalna, tzn. da się tak połączyć elementy w pary, że maksymalna suma byłaby mniejsza.
Oznaczmy przez (a[i], a[j]) parę o maksymalnej sumie wg oryginalnej strategii. Gdyby dało się połączyć elementy w pary, tak, że maksymalna suma byłaby mniejsza, 
oznaczałoby to, że a[i] musielibyśmy połączyć z a[k]: a[k] < a[j]. Podobnie a[j] musielibyśmy połączyć z a[l]: < a[i]. 
W ten sposób zostanie bez pary więcej elementów większych od a[j] niż elementów mniejszych od a[i].
Będziemy więc musieli tak łączyć elementy w pary, że powstanie choć jedna para taka (a[x],a[y]), że a[x] > a[i] oraz a[y] > a[j], skąd a[x] + a[y] > a[i]+a[j],
więc maksymalna suma jest większa niż w oryginalnej strategii. Sprzeczność.'''

def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[
            j] <= x:
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


def mini_maxi_sum_of_pair(T):  #założenie - ilosc liczb jest parzysta
    n = len(T)
    quick_sort_mem2(T, 0, n - 1)
    print(T)
    maximal = -1
    max_pair = None  #tak dla mnie informacyjnie
    for i in range((n//2) + 1):
        sum_of_pair = T[i] + T[n - 1 - i]
        if sum_of_pair > maximal:           #możnaby zastąpic -> maximal = max(maximal, sum_of_pair)
            maximal = sum_of_pair
            max_pair = (T[i], T[n - 1 - i])

    print(max_pair)
    return maximal


from random import randint

test = [randint(0,100) for _ in range(20)]
print(mini_maxi_sum_of_pair(test))
