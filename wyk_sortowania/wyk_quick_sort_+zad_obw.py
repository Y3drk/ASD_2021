def partition(T,p,r):   #ta funkcja nam robi głowna robote w sorcie, układa elementy w odpowiedniej koljnosci
    x = T[r]            # x to nasz pivot wzgledem ktorego układamy elementy
    i = p - 1
    for j in range(p,r):   #porownujemy kolejne elementy ze sobą
        if T[j] <= x:           # jesli element po lewej stronie od pivota jest od niego mniejszy to przesuwamy go na jego lewa strone, zamianiajac go z pierwszym el. wiekszym od x ktorym jest T[i]
            i += 1                          #indeks i przesunie sie tyle razy ile zamian dokonamy, wiec bedzie idealnie (i cały czas) wskazywał na ostatni element <= x
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]   # wstawiamy pivota na odpowiednie miejsce

    return i + 1        #zwracamy połozenie pivota , bo wg niego dzielimy potem tablice


def quick_sort(T, p, r):
    if p < r:
        q = partition_random(T,p,r)   #wstepne sortowanie wg jakiegos piwota i dzielenie tablicy wzgledem niego
        quick_sort(T,p, q - 1)
        quick_sort(T, q + 1, r)  #sortowanie podzielonych tablic, zauwazmy ze pivota juz nie sortujemy, gdyz jest on juz na swoim miejscu




# jednak ma on swoje wady, dla niekorzystynych danych bedzie działał w czasie O(n^2), a co gorsza gdy dane sa duze to nasze O(n) wywołań rekurencyjnych
# prawdopodobnie przepełni nam stos systemowy i nam sie algorytm spieprzy, co jest duzo gorsze niz wolniejszy czas działania *1
#z problemem czasu można zawalczyć wybierając pivota losowo, czyli swapujac T[r] z jakims losowym elementem
# i tutaj sprobuje to zrobić...


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]    #dokonujemy wyboru losowego elementu i zamieniamy go z ostatnim elementem

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


# *1 - ale z tym można sobie poradzic i w ramach zadania domowego sprobuje to zrobić

# ZADANIE OBOWIĄZKOWE - zaimplementuj quicksort aby nigdy nie zuzywał wiecej niż O(logn) dodatkowej pamieci

def quick_sort_mem1(T,p,r):
    while p < r:        #zamiast wywoływac funkcje kolejny raz, "wciągamy" tą pętlę do środka
        q = partition_random(T,p,r)
        quick_sort_mem1(T,p, q - 1)
        p = q + 1   #zauważamy ,ze wczesniej wywoływalismy drugi raz quick sorta dla el, od q + 1 do r, r sie nie zmienia, a to jest nowa wartosc p

                    #jest już dużo lepiej, ale wciąz mozliwy jest najgorszy scenariusz (pivot wypada na ostatni element i tablica jest juz posortowana)
        # wiec cały czas mozemy uzyc O(n) dodatkowej pamięci, jak to pokonać ?

def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:   # zawsze wywołujemy quicksorta dla mniejszej czesci powstałej po podziale, a dla wiekszej czesci wracamy do poczatku pętli
            quick_sort_mem2(T, p, q - 1)
            p = q + 1 #i wywołujemy dla niej partition jeszcze raz

        else:
            quick_sort_mem2(T, q + 1, r)   #jak wyżej tylko tutaj mamy przypadek gdy prawa czesc jest mniejsza
            r = q - 1

#dzieki temu nawet gdy wystapi najgorszy dla nas przypadek ( w kwestii pamieci, czyli paradoksalnie wczesniej najlepszy, bo chodzi o idealny podział tablicy na pół)
# to użyjemy O(logn) pamieci. Bedzie to mozna zobrazowac drzewem binarnym podobnym do tego z mergesortu na wykładzie

tab = [7, 23, 13, 29, 19, 8, 2, 1,88, 30, 24]
quick_sort_mem2(tab, 0, len(tab) - 1)
print(tab)


