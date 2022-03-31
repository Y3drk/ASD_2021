'''Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n].
 Proszę napisać algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich GCD jest różny od 1.
 Algorytm powinien działać jak najszybciej.'''

# tworzymy tablice n+1 elementów. tam wklepujemy liczby, których dzielnikiem jest indeks pola, na koniec przechodzimy po niej raz szukajac najwiekszej długości


def dividers(x):   #dla kazdej liczby - O(sqrt(num))
    divs = []
    i = 1
    if x == 1:
        return [1]

    while i <= x*(1/2):
        if x % i == 0:
            if i not in divs:
                divs += [i]
            if x // i not in divs:
                divs += [x // i]

        i += 1

    return divs


def finding_GCD(T):
    n = len(T)
    D = [[] for _ in range(n+1)]   #tablic dzielników
    for i in range(n):
        tmp = dividers(T[i])   #znajdujemy dzielniki
        print("liczba i dzielniki:",T[i],tmp)
        for elem in tmp:       #wpisujemy liczbe do tablicy dzielników  #wszystko co jest podzielne przez 4 jest tez podzielne przez 2 wiec zbior bedzie ofc liczniejszy
            #print(elem)     #dlatego tą pętle mozna zoptymalizowac stosujac sito erastotenesa na przedziale [0,n]
            D[elem] += [T[i]]

    max = None  #takie dodatkowe rzeczy dla mnie
    GCD = 0
    len_max = 0
    for i in range(2,n+1):    #moznaby to zrobic ładniej gdyby chciec tylko długość  -> ( max(len_max, len(D[i]))
        if len(D[i]) > len_max:
            max = D[i]
            len_max = len(D[i])
            GCD = i

    print("GCD:",GCD)
    print("Liczby ze zbioru:",max)
    return len_max


#from random import randint
#n = int(input("podaj zakres i ilosc (jednoczesnie): "))
#test = [randint(0,n) for i in range(n)]
test2 = [3, 8, 16, 19, 6, 20, 17, 15, 5, 2, 11, 0, 13, 1, 18,10, 9, 4, 12, 14]
print(test2)
print(finding_GCD(test2))

