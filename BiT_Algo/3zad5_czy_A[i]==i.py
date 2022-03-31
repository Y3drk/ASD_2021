'''Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne. Podaj algorytm, który sprawdzi, czy jest taki indeks i, że
A[i] == i.
Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?
'''

# dla elementów naturalnych (i zera) - sprawdzamy pierwszą pozycję, czemu ? Bo liczby są parami rózne i moga rosnac minimalnie o 1, wiec jesli T[0] != 0 to dalaj również nie
#zajdzie równość


def check_for_naturals(T): #magiczna złożoność O(1)
    return T[0] == 0

# dla elementów całkowitych - robimy binary search tylko sprawdzamy inny warunek ( T[i] < i przesuwamy sie w prawo, T[i] > i przesuwamy sie w prawo


def binary_search_special(T):
    n = len(T)
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if T[mid] < mid:
            left = mid + 1

        else:
            right = mid - 1

    if left < n and T[left] == left:
        return True

    return False


testN1 = [0, 1, 2, 3, 4]
testN2 = [3, 4, 7, 8, 10]
testZ1 = [-7, -6, -4, 0, 3, 4, 8, 9, 10]
testZ2 = [-3, -2, -1, 0, 2, 4, 6, 8, 10]
print("test1:")
print(check_for_naturals(testN1))
print("test2:")
print(check_for_naturals(testN2))
print("test3:")
print(binary_search_special(testZ1))
print("test4:")
print(binary_search_special(testZ2))

