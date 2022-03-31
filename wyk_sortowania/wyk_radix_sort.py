def count_sort(T,k,ind):   #do radixa potrzebujemy jakiejs innej stabilnej metody sortowania. Ja uzyje tutaj count sorta bo jest po prostu
    n = len(T)          #najszybszy. Pewnie bedą potrzebne modyfikacje więc zaraz je zrobię
    C = [0 for _ in range(k)]  #załozymy, ze wszystkie sortowane słowa sa w lowercase, poza tym jest jakas metoda w pythonie która łatwo to zmienia
    B = [0 for _ in range(n)]

    for i in range(n):
        C[ord(T[i][ind])- 97] += 1

    for j in range(1,k):
        C[j] += C[j - 1]

    for l in range(n - 1, -1, -1):
        C[ord(T[l][ind])- 97] -= 1
        B[C[ord(T[l][ind])- 97]] = T[l]

    for i in range(n):
        T[i] = B[i]


def radix_sort(T):
    n = len(T)
    s = len(T[0])   #ciche założenie, ze wszystkie słowa / elementy (w zaleznosci od potrzeb) maja tę samą długość, na to ofc też mozna coś poradzić
    for i in range(n):    #dodatkowy case jesli komuś sie zachce duzych liter w słowie
        T[i] = T[i].lower()

    for j in range(s - 1,-1, -1):  #sortujemy stabilnie dla kazdej pozycji osobno, zaczynajac od najmniej znaczacej
        count_sort(T,26,j)

    return T


test = ["kra", "art", "kot", "kit", "ati", "kil"]
print(radix_sort(test))
