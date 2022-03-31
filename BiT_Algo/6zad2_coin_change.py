'''W problemie coin change mamy daną kwotę X i chcemy ją rozmienić na monety o wartości 1, 5, 10, 25 i 100.
Podaj algorytm, który obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz ile sztuk każdej monety będzie trzeba użyć.
Można założyć, że każdej monety mamy nieskończenie wiele sztuk.
Czy algorytm zachłanny działa dla zestawu monet 1, 2, 7, 10? Jeśli tak, uzasadnij dlaczego. Jeśli nie, podaj kontrprzykład.
'''

# idea - zachłannie bierzemy największy nominał jaki możemy.
# dlaczego to działa ?
# kazdy nastepny nominał jest wielokrotnoscia poprzednich, zatem nigdy nie zachodzi sytuacja gdy opłaca się wziąć mniejszy nominał,
# bo kazdy wiekszy nominał mozna zastapic tylko wiekszą iloscia nominałów mniejszych
# dodatkowo problem ma właściwosc optymalnej podstruktury, gdyz odejmujac maksymalny nominał od kwoty otrzymujemy mniejszy tego dsamego typu problem

# alg zachłanny nie działa dla podanego zestawu monet bo nie spełniaja "zasady wielokrotnosci".
# kontrprzykład : 14 --> algorytm wybierze 10, 2, 2, podczas gdy optymalne rozwiazanie to 7,7

#złożonosc O(X/srednia elementow * C)


def coin_change(C,X):
    n = len(C)
    counter = 0
    L = [0 for _ in range(n)] #dodamy sb dodatkową tablice aby zliczac ilosc uzytych monet
    tmp = X
    for i in range(n - 1, -1, -1):
        while tmp - C[i] >= 0:
            tmp -= C[i]
            L[i] += 1
            counter += 1

    print("Do wydania kwoty",X,"potrzebujemy:",counter,"monet, w tym..")
    for i in range(n):
        if L[i] > 0:
            print(L[i],"monet o nominale:",C[i])

    exit(0)


C = [1,5,10,25,100]
X = 88
coin_change(C,X)





