#idea - sortujemy tablice, nie mamy zadnych przesłanek o zakresie lub potencjalnym rozkładzie jednostajnym wiec pozostaje quicksort
# nastepnie dla kazdej liczby sprawdzamy sume w nastepujacy sposób
# 1- bierzemy dwie zmienne sterujace left = 0 i right = n -1 , gdzie n to długosc tablicy
# 2- sprawdzamy wartosc sumy elementów spod zmiennych sterujacych jesli left != indeks liczby sprawdzanej != right
# 3- jesli suma jest mniejsza przesuwamy left o 1 w prawo, jesli wieksza to przesuwamy right o 1  lewo
# 4 - konczymy gdy znajdziemy sume równa sprawdzanej liczbie lub wskazniki sie spotkaja, w drugim przypadku oznacza to ze istnieje liczba ktorej nie da sie przedstawic jako
#sumy dwoch innych wiec mozemy od razu zwrócic false

#złożonośc - quicksort sortuje w czasie O(nlogn), ale prawdziwa złożonosc narzuca metoda sprawdzania. Przejscie po kazdej liczbie to n, ale do tego dochodzi jeszcze
#sprawdzenie sumy. Zmienne sterujace przesuniemy maksymalnie n-1 razy a jest to zagniezdzona petla while wiec wymusza ona złożonosc O(n^2)


def partition_random(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[
            j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):
    while p < r:
        q = partition_random(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1

        else:
            quick_sort_mem2(T, q + 1, r)
            r = q - 1


def sums(T):
    n = len(T)
    quick_sort_mem2(T,0, n-1)
    #print(T)
    for i in range(n):
        value = T[i]
        #print(value)
        left, right = 0, n-1
        while left < right:

            if T[left] + T[right] == value:
                #print(left,right, T[left],T[right])
                break

            elif T[left] + T[right] < value:
                left += 1

            else:
                right -= 1

            if left == i:
                left += 1
            if right == i:
                right -= 1
        else:
            return False

    return True


test = [-5,-6,0,34,56,11,23,5,4,7,9,-2,-6,11,22]
test2 = [0,1]
test3 = [-5, -3, -2, 1, 2, 3, 5]
print(sums(test))
print(sums(test2))
print(sums(test3))

#0.5 pkt od Lukasza