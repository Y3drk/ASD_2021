#sortujemy cyklistów wg  ich numerów
# przechodzac po kolejnych cyklistach łaczymy ich w linklisty za pomoca pola prev, do znajdywania odp cyklistów uzywamy binary searcha
# potem dla kazdego lidera ( cyklisty o n_id == -1) liczymy długosc listy, poniewaz kazdy kolarz jest tylko w 1 liscie zajmuje to czas O(n)

# całkowita złozonosc O(nlogn) narzucona zarówno przez sortowanie jak i łaczenie

# PS - japierdole jak mozna dawac test bez kolarzy <3


class Cyclist:
    def __init__(self,id,n_id): # prosze nie usuwac tej funkcji(uzywaja ja testy w takiej formie jak jest)
        self.id = id
        self.n_id = n_id
        self.prev = None


def binary_search(tab,el):
    l, r = 0, len(tab) - 1

    while l <= r:
        mid = (l + r) // 2

        if el > tab[mid][0]:
            l = mid + 1

        else:
            r = mid - 1

    if l < len(tab) and el == tab[l][0]:
        return l

    return False


def get_len(wsk):
    l = 0
    p = wsk
    while p != None:
        l += 1
        p = p.prev

    return l


def smallestGroup(cyclist_list, n):
    # tutaj powinna znalezc sie implementacja
    T = []
    Specials = []
    for cyclist in cyclist_list:
        T += [(cyclist.id, cyclist.n_id, cyclist)]
        if cyclist.n_id == -1:
            Specials += [cyclist]

    T.sort(key=lambda x: x[0])  # sortowanie po nr cyklistów O(nlogn)

    for cyc in T:  #łaczenie odp cyklistów z pomoca binary searcha O(nlogn)

        if cyc[1] == -1:
            continue

        else:
            tmp = binary_search(T,cyc[1])
            lider = T[tmp][2]
            lider.prev = cyc[2]


    animals_attack = float('inf')
    for lider in Specials:
        curr = get_len(lider)
        if curr < animals_attack:
            animals_attack = curr

    if animals_attack == float('inf'):
        return 0
    else:
        return animals_attack


if __name__ == "__main__":
    from zad2_testy_33 import runtests
    runtests(smallestGroup)
