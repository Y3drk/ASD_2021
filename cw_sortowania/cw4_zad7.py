'''Zadanie 7. Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
szukamy najkrótszego przedziału z wszystkimi kolorami).
'''


def colours(T, k):
    Count = [0] * k    #tablica wystapien kolorów na danym przedziale
    i = 0           #ustawiamy wszystkie konieczne wskaźniki
    ile_k = 0       #ile unikalnych kolorów mamy w naszym przedziale
    dlg = 0        #długosc naszego przedziału
    start = 0      #obecny poczatek przedziału
    min = len(T)    #przechowywanie najkrótszego przedziału
    min_start = -1  #wskazania na poczatek i koniec najkrótszego przedziału
    min_stop = -1
    while i < len(T):                 #idziemy po tablicy dodajac kolejne elementy do tablicy wystapien i zwiekszajac długosc
        print(Count, i, start, dlg, ile_k, min)
        dlg += 1
        if Count[T[i]] == 0:     #jesli kolor pojawia sie po raz pierwszy zwiekszamy ilosc unikalnych kolorów
            ile_k += 1
        Count[T[i]] += 1
        if ile_k == k:         #jesli w naszym przedziale kazdy kolor wystepuje juz co najmniej raz, idac do startu do przodu probujemy go zawezić
            while start <= i:
                Count[T[start]] -= 1
                dlg -= 1
                if Count[T[start]] == 0:   #jesli sprawimy ze którys kolor całkowicie zniknął z tablicy konczymy ruszanie startem...
                    ile_k = k - 1
                    start += 1
                    if dlg + 1 < min:   #i sprawdzamy czy nasz przedział przed usunieciem koloru był najkrótszy, jesli tak to zapisujemy jego długosc i wskazania na poczatek i koniec
                        min_start = start - 1
                        min_stop = i
                        min = dlg + 1
                    break
                start += 1
        i += 1
    return min, min_start, min_stop


T = [1, 2, 1, 0, 1, 4, 3, 1, 2, 4, 3, 2, 1, 0]
print(colours(T, 5))