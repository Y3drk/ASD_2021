'''Zadanie 6. Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
których A[i + 1] − A[i] jest największe).'''


#Idea - rozdzielamy elementy do kubełków o odpowiednio małym zasiegu, dzięki temu wiemy, że szukane przez nas liczby nie są w jednym kubełku. Sortujemy kubełki.
#sprawdzamy zatem max z poprzedniego kubełka i min z nastepnego. jesli jakis kubełek jest pusty to zwieksza to szanse, że odp sa elementy przed nim i po nim

# co jest lepsze - normalizacja kubełków względem najwiekszej liczby czy jej długości ?
#sprobujmy normalizowac wzgledem liczby

def insert_sort(T): #bez wartownika
    n = len(T)
    for i in range(1, n):
        tmp = T[i]
        j = i - 1
        while (j >= 0) and (tmp < T[j]):
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = tmp

    return T


def max_span(T):
    n = len(T)
    maxi = -1
    mini = 100000000

    for l in range(n):
        if T[l] > maxi:
            maxi = T[l]
        if T[l] < mini:
            mini = T[l]

    B = [[] for _ in range(n)]
    x = (maxi + mini)/n    #zasieg kubełka
    for i in range(n):                 #elementy do kubełków
        B[int((T[i] - mini)/x)] += [T[i]] #!!!!!


    diff = 0
    prev_max = max(B[0])
    x, y = prev_max, None
    for l in range(1,n):  #sortowanie kubełków jest nieopłacalne bo max znajdujemy liniowo, a sort kubełka jest no powiedzmy nlogn
        if len(B[l]) != 0:

            act_min = min(B[l])

            if diff < act_min - prev_max:
                diff = act_min - prev_max
                x, y = prev_max, act_min

            prev_max = max(B[l])

    return diff, x, y


test = [ 0.45, 0.3, 0.01, 0.11, 0.91, 0.7, 0.2, 0.13]
print(max_span(test))
print(insert_sort(test))