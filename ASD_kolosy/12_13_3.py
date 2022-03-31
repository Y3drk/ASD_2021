# 12_13_2 było na ciwczeniach i jest otagowane jako cw3_zad5_NOT_WORKS - bo struktura miała byc inna
#dwa kopce - min i max składające sie ze wszystkich elementow kazdy i przechowujace inormacje o połozeniu tego samego elementu w drugim kopcu

''' Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu.'''

# idea -
# 0) zakładamy ze alkojujemy tablice wystapien jak w C - w czasie stałym, ruszac bedziemy tylko konkretne elementy, dzięki temu nie zepsujemy złożoności
# 0.1) jesli len(w) > len(u) + len(v) to od razu zwracamy false, jesli len(w) == 0 od razu zwracamy true
# 1) zerujemy wszystkie pola wystapien liter ze słów u, v i w
# 2) przechodzac po kazdym słowie odpowiednio inkrementujemy lub dekrementujemy opd indeksy tablicy wystapien ( dla u i v inkrementujemy, dla w dekrementujemy)
# 3) przechodzac po słowie w sprawdzamy czy wszystkie indeksy odp liter w tablicy wystapien sa >=0. Jesli tak zwracamy true, bo starczy nam liter z u i v do zbudowania w
# wpp zwracamy false


def alloc(num):  # umowna realizacja naszego cichego założenia o alokacji w czasie stałym
    T = [0 for i in range(num)]
    for i in range(1,num):
        T[i] = i

    return T


def possible_construction(cw1,cw2,fw):
    I = alloc(126)  #krok (0)

    l1, l2, lf = len(cw1), len(cw2), len(fw)

    if lf == 0:  # krok (0.1)
        return True
    elif lf > l1 + l2:
        return False



    for i in range(l1):  #krok (1)
        I[ord(cw1[i])] = 0

    for i in range(l2):  #dla kazdego słowa jest osobna petla bo nie mamy żadnego założenia na długosc słów
        I[ord(cw2[i])] = 0

    for i in range(lf):
        I[ord(fw[i])] = 0

    for i in range(l1):  # krok (2)
        I[ord(cw1[i])] += 1

    for i in range(l2):  # analogiczna sytuacja do powyzszej
        I[ord(cw2[i])] += 1

    for i in range(lf):
        I[ord(fw[i])] -= 1

    for i in range(lf):
        if I[ord(fw[i])] < 0:
            return False

    return True


w1 = "KIA"
w2 = "ALFAROMEO"
w3 = "HONDA"
w4 = "HYUNDAI"
w5 = ""
w6 = "PORSCHEPANAMERA"

print(possible_construction(w1,w2,w3))
print(possible_construction(w1,w4,w3))
print(possible_construction(w4,w2,w3))
print(possible_construction(w1,w2,w5))
print(possible_construction(w1,w2,w6))



