'''Pierwsze dwa zadania to były zadania obowiazkowe z wykładu

Zad3. Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać własny stos).'''

import random


def partition(T, l, p):
    a = random.randint(l, p)
    pivot = T[a]
    T[a], T[p] = T[p], T[a]
    j = l
    for i in range(l, p):
        if (T[i] <= pivot):
            T[i], T[j] = T[j], T[i]
            j += 1
    T[p], T[j] = T[j], T[p]
    return j


def iter_quicksort(T, l, p):                   #rekurencję usuwamy wykorzystując stos, możemy na niego składac albo lewy i prawy znacznik osobno, albo jako krotki
    if len(T) == 0 or len(T) == 1:          #wg mnie druga opcja jesttroche bardziej przejrzysta (nwm jak ze złożonościa), więc sprobuje sb to pozmieniać
        return T
    stack = [0] * len(T)
    stack[0] = [l,p]
    top = 0
    while top >= 0:
        l, p = stack[top]
        top -= 1
        q = partition(T, l, p)
        if q - 1 > l:
            top += 1
            stack[top] = [l, q -1]   # w zależności od wyniku partition wrzucamy na stos lewą lub prawą czesc tablicy
        if q + 1 < p:
            top += 1
            stack[top] = [q + 1,p]



def iter_quicksort_prettier(T):
    S = []
    l, p = 0 , len(T) - 1
    S.append((l,p))
    while len(S) > 0:
        l,p = S.pop()
        if l < p:
            q = partition(T,l,p)
            S.append((l, q - 1))
            S.append(((q + 1, p)))


def iter_quicksort_mem(T):
    S = []
    l, p = 0 , len(T) - 1
    S.append((l,p))
    while len(S) > 0:
        l,p = S.pop()
        if l < p:
            q = partition(T,l,p)   #ograniczyc ilosc zuzywanej pamieci do O(logn), idea podobna jak w rozwiazaniu rekurencyjnym
            if q - l < p - q:      #w obu przypadkach najpierw odkładamy na stos dłuzsza cześc tablicy
                S.append(((q + 1, p)))  #poniewaz jest on strukturą FIFO to kładac krótsza czesc jako druga, zajmiemy sie nia na poczatku (sciagniemy ja jako pierwsza)
                S.append((l, q - 1))   #tak samo jak w rekurencji wywoływalismy ja najpierw dla krótszej. rekurencji ogonowej tez juz nie mamy zatem zad jest skonczone
            else:
                S.append((l, q - 1))
                S.append((q + 1, p))



T = [random.randint(0, 10) for _ in range(10)]
print(T)
print("----")
iter_quicksort_mem(T)
print(T)

#works w pytkę