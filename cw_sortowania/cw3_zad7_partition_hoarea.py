'''Zad7.
(Partition Hoare’a) Proszę zaimplementować funkcję partition z algorytmu QuickSort
według pomysłu Hoare’a (tj. mamy dwa indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka
i zamieniamy elementy tablicy pod nimi jeśli mniejszy indeks wskazuje na wartość większą od piwota, a
większy na mniejszą.
'''


def HoraePartition(T, l, r):
    mid = (l + r) // 2   #pivota możemy wybrac losowo, ale tutaj akurat wzielismy ze srodka i tez jest spoko
    pivot = T[mid]
    i = l - 1       #mamy dwa indeksy sterujące narazie ustawione poza zakres bo bedziemy je przesuwac w petli
    j = r + 1
    while True:
        i += 1  #jak wspomniane przesuwamy nasze indeksy
        while (T[i] < pivot):  #lewy przesuwamy tak długo jak element na nim jest mniejszy do pivota
            i += 1

        j -= 1
        while (T[j] > pivot):  #prawy przesuwamy tak długo jak element na nim jest wiekszy do pivota
            j -= 1

        if (i >= j):  #jesli doszlismy to sytuacji w której indeksy się spotykaja lub przecinaja oznacza ze obie strony sa dobrze poustawiane względem pivota
            return j

        T[i], T[j] = T[j], T[i] #jesli nie doszło do powyższej sytuacji to musimy cos jeszcze przestawic, zamieniamy miejscami el. na które trafilismy w while
        #wyzej. dzieki temu sa poprawnie ustawione wzgledem pivota. Potem petla rusza od nowa (z tym ze zaczyna od tych i oraz j ktore zostały ustawione tu)


def quicksort(T, l, r):
    if l < r:
        q = HoraePartition(T, l, r)
        quicksort(T, l, q)     #tutaj jest jedyna różnica ze zwykłym quicksortem (q zamiast q+1) bo nie mamy 100% pewnosci gdzie skończy sie ruch indeksu j
        quicksort(T, q + 1, r)


tab = [7, 23, 13, 29, 19, 8, 2, 1,88, 30, 24]
quicksort(tab, 0, len(tab) - 1)
print(tab)