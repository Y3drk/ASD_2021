'''Cersei i Jaime mają 3 - letniego syna. Przygotowali listę N aktywności podanych jako pary,
reprezentujące czas rozpoczęcia i zakończenia danej aktywności. Zaimplementuj algorytm, który przyporządkuje każdej aktywności literę C lub J,
oznaczającą, że daną aktywność z synem wykona odpowiednio Cersei lub Jaime, w taki sposób,
że żaden rodzic nie wykonuje pokrywających się czasowo aktywności. Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca “IMPOSSIBLE”,
a jeśli istnieje, to zwraca odpowiedniego stringa.

Przykładowo: (99, 150), (1, 100), (100, 301), (2,5), (150, 250) - odpowiedź to JCC JJ (lub CJJ CC). to chyba tak nie moze jednak byc
bo jedno z ostatnich dwoch zadan zawiera sie w drugim
'''

#idea - rozdzielenie aktywnosci na poczatki i konce oraz ich sortowanie, nastepnie bierzemy kolejne wydarzenia i jesli sa poczatkiem sprawdzamy czy
# ktores z rodziców moze je zaczac, jesli tak to dajemy im je do wykonania, wpp, zwracamy impossible, jelsi trafimy na koniec to odejmujemy zadanie od odp rodzica

#ciche zał. rodzic moze wykonac oba zadania jesli jedno konczy sie a drugie zaczyna w tym samym czasie

def Cersei_and_Jaime(Tasks):
    n = len(Tasks)
    TMP = []
    for i in range(n):
        # 1 oznacza poczatek 2 oznacza koniec - struktura [nr zadania, czas wydarzenia, typ]
        TMP += [[i,Tasks[i][0],1]]
        TMP += [[i, Tasks[i][1], 2]]

    quick_sort_mem2(TMP,0,len(TMP) - 1)
    #print(TMP)

    Cersei_busy = 0
    Cersei_doing = None
    Jaime_busy = 0
    Jaime_doing = None
    Fair_share = []
    for i in range(len(TMP)):
        if TMP[i][2] == 1: #jesli wydarzenie jest poczatkiem
            if Jaime_busy == Cersei_busy == 1:
                print("IMPOSSIBLE")
                return

            elif Cersei_busy == 0:
                Fair_share += ["C"]
                Cersei_busy = 1
                Cersei_doing = TMP[i][0]

            elif Jaime_busy == 0:
                Fair_share += ["J"]
                Jaime_busy = 1
                Jaime_doing = TMP[i][0]

        if TMP[i][2] == 2:  # jesli wydarzenie jest koncem
            if TMP[i][0] == Jaime_doing:
                Jaime_busy = 0

            elif TMP[i][0] == Cersei_doing:
                Cersei_busy = 0

    #print(Fair_share)
    for i in range(len(Fair_share)):
        print(Fair_share[i],end='')

    return


def partition_random_tasks(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x1 = T[r][1]
    x2 = T[r][2]
    i = p - 1
    for j in range(p, r):
        if T[j][1] < x1:
            i += 1
            T[i], T[j] = T[j], T[i]

        elif T[j][1] == x1 and T[j][2] > x2:
            i += 1
            T[i], T[j] = T[j], T[i]


    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random_tasks(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


test = [(99, 150), (1, 100), (100, 301), (2,5), (150, 250)]
Cersei_and_Jaime(test)


