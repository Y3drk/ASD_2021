# Jędrzej Ziebura

# Opis Algorytmu:
# 0) Będziemy przemieszczać się po liście analizując k + 1 elementów naraz ("przedziały" [i,...,k + 1 + i], ponieważ wśród nich musi znajdować się element,
# który po posortowaniu powinien być na pozycji i-tej. Po każdej sekwencji operacji opisanych w pkt 3 "przedział" będziemy przesuwać o 1 w strone końca listy.
# 1) Pierwszy "przedział" posortujemy, dla małych k można to zrobić, którymś z sortowań prostych, ze względu na niską stałą, ja zrobię to quicksortem, bo prawdę mówiąc mam
# go przygotowanego z zadania offline (złożoność O(stała) dla odp. małych k, O(k*logk) dla większych k i quicksorta).
# 2) Wykonamy n-k przesunięć "przedziału" i w każdym przesunięciu...
# 3) Wstawimy w odpowiednie miejsce przedziału nowy element, który wszedł do niego po przesunięciu (złoż. O(k)) i
# 3.1) "Odłożymy" do wynikowej listy pierwszy element z przedziału. (złożoność O(1))
# 4) gdy dojdziemy do k ostatnich elementów, cały (już posortowany) przedział dołączymy do listy wynikowej (złoż. O(1)).

# *** - w tworzeniu wynikowej listy pomagam sobie strażnikiem, do wstawiania używam funkcji add_to_interval

# Złożoność:
# k = teta(1) - sortowanie początkowego przedziału to O(1), wykonujemy n przesunieć (O(n)) i odpowiednio układamy element w czasie O(1) - w ogólnym rozrachunku O(n)
# k = teta(logn) - sortowanie początkowego przedziału to O(logn*log(logn)), wykonujemy n - logn przesunieć (O(n - logn)) i odpowiednio układamy element w czasie O(logn)
# - w ogólnym rozrachunku O((n - logn)*logn)
# k = teta(n) - sortowanie początkowego przedziału to O(nlogn), wykonujemy stałą liczbę ( n - (~n)) przesunięć (O(1)) i odpowiednio układamy element w czasie O(n)
# - w ogólnym rozrachunku O(nlogn)


from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None


def qsort(L):

    def find_end(L):
        while L.next is not None:
            L = L.next
        return L

    def quicksort_ll(start, beg, end):
        new_start, new_beg_ls, new_end_ls, new_beg_bg, new_end_bg = new_partition(start, beg, end)

        if new_beg_ls != None and new_end_ls != None and new_end_ls != new_beg_ls:
            new_start = quicksort_ll(new_start, new_beg_ls, new_end_ls)

        if new_beg_bg != None and new_end_bg != None and new_end_bg != new_beg_bg:
            new_start = quicksort_ll(new_start, new_beg_bg, new_end_bg)

        return new_start

    def new_partition(start, beg, end):
        new_beg_ls, new_end_ls, new_beg_bg, new_end_bg = None, None, None, None
        holder_t = end.next
        end.next = None
        holder_h = None

        if start != beg:
            holder_h = start
            while start.next != beg:
                start = start.next

            start.next = None

        pivot = end.val
        pointer = beg
        g_ls, g_eq, g_bg = Node(), Node(), Node()
        g_ls.val, g_eq.val, g_bg.val = "less", "equal", "bigger"
        ls, eq, bg = g_ls, g_eq, g_bg

        while pointer.val != None and pointer != end:
            if pointer.val > pivot:
                bg.next = pointer
                bg = bg.next
            elif pointer.val < pivot:
                ls.next = pointer
                ls = ls.next
            else:
                eq.next = pointer
                eq = eq.next

            if pointer.next != None:
                pointer = pointer.next
            else:
                break

        eq.next = end  # przepiecie pivota do equal
        eq = eq.next
        ls.next, eq.next, bg.next = None, None, None

        if g_ls.next == None:
            new_beg_ls = None
            new_end_ls = None
        else:
            new_beg_ls = g_ls.next
            new_end_ls = ls

        if g_bg.next == None:
            new_beg_bg = None
            new_end_bg = None
        else:
            new_beg_bg = g_bg.next
            new_end_bg = bg

        beg = g_ls
        ls.next = g_eq.next

        if g_bg.next != None:
            eq.next = g_bg.next
            bg.next = holder_t
        else:
            eq.next = holder_t
        beg = beg.next

        if holder_h != None:
            start.next = beg
            return holder_h, new_beg_ls, new_end_ls, new_beg_bg, new_end_bg

        return beg, new_beg_ls, new_end_ls, new_beg_bg, new_end_bg

    end = find_end(L)
    L = quicksort_ll(L, L, end)
    return L


def add_to_interval(el,interval):
    prev, curr = None, interval

    while curr != None and curr.val <= el.val:
        prev = curr
        curr = curr.next

    if prev == None: #gdy musimy wstawic element na poczatek
        el.next = interval
        return el

    prev.next = el
    el.next = curr
    return interval


def SortH(p,k):

    if k == 0:
        return p

    guardian = Node()
    guardian.val = "!"
    pointer = guardian
    prev, curr = None, p
    cnt = 1
    interval = curr

    while cnt <= k + 1  and curr != None:
        prev = curr
        curr = curr.next
        cnt += 1

    prev.next = None
    interval = qsort(interval)

    guardian.next = interval
    interval = interval.next
    pointer = guardian.next
    pointer.next = None

    while curr != None:
        new = curr
        curr = curr.next
        new.next = None

        interval = add_to_interval(new, interval)

        pointer.next = interval
        interval = interval.next
        pointer = pointer.next
        pointer.next = None

    pointer.next = interval
    return guardian.next

    # tu prosze wpisac wlasna implementacje
    pass


runtests( SortH )

