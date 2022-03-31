'''Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, a reszta tablicy ma wartości None.
 Nie jest dana wartość n. Przedstaw algorytm, który dla danej liczby naturalnej x znajdzie indeks w tablicy, pod którym znajduje się wartość x.
 Jeżeli nie ma jej w tablicy, to należy zwrócić None.'''

#idea  - zaczynamy od indeksu 1 - jesli T[ind] < x to zwiekszamy indeks dwukrotnie. Operacje powtarzamy, ąż trafimy na wieksza liczbe albo na None
#wtedy odpalamy zwykły binary search na przedziale od poprzedniego indeksu do obecnego traktujac None jak infinity


def binary_search(T,x,l,r):
    n = len(T)
    left, right = l, r
    while left <= right:
        mid = (left + right) // 2
        if T[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    if left < n and T[left] == x:
        return left

    return False


def find(T,x):
    ind = 1
    while ind < len(T):   #zał o nieskonczonej tablicy jest troche trudne do fizycznej implementacji, więc ja bede reprezentowac to tak, w zał pętla jest nieskonczona
        #print("wbitka",ind,T[ind])
        if T[ind] == None or T[ind] > x:
            #print("1")
            return binary_search(T,x,ind//2,ind)

        elif T[ind] == x:
            #print("2")
            return ind

        elif T[ind] < x:
            #print("3")
            ind *= 2


test1 = [2,3,5,7,11,13,17,19,23,29,31,37,56,76,88,102,103,111,147,1020,1780]
test2 = [2,3,5,7,11,13,17,19,23,29,31,37,56,76,88]
test3 = [2,3,5,7,11,13,17,19,23,29,31,37,56,76,102,103,111,147,1020,1780]
x = 88
test1 += [None for _ in range(100)]
test2 += [None for _ in range(100)]
test3 += [None for _ in range(100)]
print("test1")
print(find(test1,x))
print("test2")
print(find(test2,x))
print("test3")
print(find(test3,x))
