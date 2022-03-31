from zad1testy_egz0 import runtests

#wstepnie sprawdzamy słowa czy ich długosc sie zgadza, czy nie sa słowami zerowymi i czy wystepuja w nich te same litery O(n)

# potem dla pierwszego słowa wrzucamy indeks każdej litery na stos odp. danej literze O(nlogn)
# nastepnie dla drugiego słowa idziemy od tyłu i wyciagamy z odp stosu najwiekszy indeks wystapienia tej samej litery O(n)
# jesli odległosc jest wieksza niz t to zwracamy fałsz wpp kontynuujemy. jesli w ten sposob przejdziemy całe drugie słowo to znaczy ze słowa
#sa t-anagrmami

# złozonosc -> czasowa O(n) - wstawianie elementów, obsługa stosu to czas stały ( .pop -> O(1))
# pamięciowa -> O(n) dodatkowe na stosy i tablicę je przechowującą


def checker(x,y): #sprawdzenie czy słowa składaja sie z tych samych liter O(n)
    I = [0 for _ in range(28)]
    for i in range(len(x)):
        I[97 - ord(x[i])] += 1
        I[97 - ord(y[i])] -= 1

    for i in range(len(I)):
        if I[i] != 0:
            return False

    return True


def tanagram(x, y, t):
    if len(x) != len(y):
        return False

    elif len(x) == 0:
        return True

    elif not checker(x,y):
        return False


    if t == 0:
        for i in range(len(x)):
            if ord(x[i]) != ord(y[i]):
                return False

        return True

    from queue import PriorityQueue

    Ix = [[] for _ in range(28)] #uznajemy to za stos
    for i in range(len(x)):
        Ix[97 - ord(x[i])].append(i)

    for j in range(len(y)-1,-1,-1):
        pos = Ix[97 - ord(y[j])].pop()

        if abs(pos - j) > t:
            return False

    return True


runtests( tanagram )


#juz jest git :)