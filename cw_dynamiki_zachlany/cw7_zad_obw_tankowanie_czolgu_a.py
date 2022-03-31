'''czołg ma za zadanie przejechac z punktu A=0 do punktu B = x.
dane:
1. czołg spala dokładnie 1 L na 1 km
2. -||- ma pojemnosc baku równa L.
3. P to tablica cen benzyny na kazdej stacji
4. S to tablica odległosci stacji od punktu '''

# zadanie a)
# zaimplementowac algorytm, dla którego czołg zwróci minimalna ilosc tankowan czołgu na trasie lub -1
# jesli istnieje przerwa miedzy stacjami wieksza niż pojemnosc baku czołgu

# idea - korzystamy z algorytmu zachłannego
# kork zachłanny : jedziemy do najdalszej stacji do jakiej mozemy dotrzec przy danym L i na niej tankujemy do pełna.
# powtarzamy procedure az do dotarcia do punktu B lub gdy nie możemy dojechac do nastepnej stacji pomimo pełnego baku

# ciche założenie : paliwo na poczatku dostalismt za darmo i jest to pelny bak (nie liczymy go jako tankowania)

# dowod poprawnosci :
# 1) krok zachłanny jest zawsze optymalny :
# założmy ze nasz algorytm w pewnym momencie wybrał stacje dalsza (ozn.d2) niż tą znajdująca sie w roziwazniu optymalnym ozn(d1).
# zauwazamy jednak, że skoro w rozwiazaniu optymalnym czołg dotarł do kolejnej stacji ze stacji d1 znajdujacej sie przed stacja d2
# to ze stacji d2 takze mozemy tam dotrzec, zatem mozemy bezkarnie podmienic w rozwiazniu optymalnym stacje d2 i d1 i zachowac jego status

# 2) własnosc optymalnej podstruktury
# zauwazmy, ze po wykonaniu kroku zachłannego stajemy przed tym samym problemem tylko ze pomniejszonym, który znowu musimy rozwiazac optymalnie
# co umozliwia krok zachłanny i zostało to udowodnione w punktcie 1)

# zatem stosujac nasz algorytm otrzymamy rozwiazanie optymalne

# złożonosc : czasowa O(n), pamieciowa in situ


def fewest_refuels(L,S):
    refuels = 0
    n = len(S)
    position = S[0]
    for i in range(1,n):
        if S[i] - position > L:     #przypadek brzegowy gdy nie damy rady dojechać do nastepnej stacji
            return - 1
        elif i < n - 1 and S[i + 1] - position > L:
            #print("refuel num:", refuels + 1, "at:", S[i], "coming from:", position)
            position = S[i]
            refuels += 1

    return refuels

L = 5
S1 = [0,2,3,5,7,11,13,17,21]
S2 = [0,2,3,5,7,11,13,17,25]
S3 = [0,2,3,5,7,11,13,20,22,23]
print(fewest_refuels(L,S1))
print(fewest_refuels(L,S2))
print(fewest_refuels(L,S3))


#tankowanie czołgu b1 jest w code_forces + pierdoły w zestaw5_+wczesniejsze_kolosy


