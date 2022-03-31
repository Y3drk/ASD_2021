#odpada countosrt, bo mamy potencjalnie nieograniczona liczbe srednich ( a przynajmniej bardzo duza) oraz bucket sort bo nie mamy informacji o
# równomiernym rozkładzie
# samo przejscie po takiej tablicy to mn

#na pewno zadziałałby quicksort i przejscie po tablicy ale byłoby O(mnlogn)

# dobra chuj z tym
# partition gdzie pivotem jest ocena studentki i chuj
# na kazdym wierszu taka zabawa to O(mn) i potem mozemy albo jak dzbany przejsc po tablicy albo zrobic to sprytnie

def partition_studentek(T, p, r, std):   # pivotem jest ocena naszej babeczki
    T[std], T[r] = T[r], T[std]

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] >= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1  # ta wartosc jest połozeniem naszej studenki w tablicy


def stypendia(T,A,k):
    m = len(T)
    n = len(T[0])
    # tu umieść swoją implementację
    points = 0
    for i in range(m):
        points += max(0,10 - abs(n// 4 - partition_studentek(T[i],0,n-1,A)))

    if points >= k:
        return True

    return False


T = [[5.0, 5.0, 3.75, 4.5, 4.3, 4.1, 3.9, 4.9, 3.6, 2.0, 2.0, 2.0],
     [5.0, 4.6, 4.9, 4.2, 3.7, 4.0, 3.8, 4.01, 3.6, 3.5, 3.4, 2.0],
     [5.0, 4.7, 3.0, 3.5, 2.8, 2.7, 2.5, 2.0, 2.3, 2.2, 2.1, 2.4]]
print(stypendia(T,7,19) == True)
print(stypendia(T,7,21) == False)

