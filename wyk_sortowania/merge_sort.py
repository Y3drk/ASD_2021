def mergesort(T):
    #print("Tu proszę napisać swoją funckję")
    n = len(T)
    if n > 1:
        mid = n // 2
        left = T[:mid]                  #podział tablicy wejsciowej na dwie (na mniejsze podproblemy) -> dziel
        right = T[mid:]
        mergesort(left)                 #sortowanie utworzonych tablic -> zwyciezaj
        mergesort(right)

        j, k = 0, 0                      #zmienne sterujace, które beda przechodzic po left i right podczas scalania
        guard_l, guard_r = 10**3, 10**3  #staznicy którzy sprawiają, że nie wychodzimy poza podtablice ( 10^3 reprezentuje tu "nieskonczonosc" - element tak duży
        left += [guard_l]               #że nie pojawi sie jako dana, którą mamy posortowac) dodajemy ich na koniec posortowanego podproblemu
        right += [guard_r]
        for i in range(n):                #proces scalania - bierzemy mniejsza liczbe z dwoch posortowanych tablic (wczesniejszych podproblemów)
            if left[j] <= right[k]:         #i wstawiamy do tablicy T; nastepnie odpowiednio przesuwamy zmienne sterujace w left i right
                T[i] = left[j]              # ze straznikami mamy n+2 elementow i poniewaz oni sa na końcu tablicy lewej i prawej to na pewno nie wstawimy ich do
                j += 1                      #naszego ostatecznego rozwiaznia
            else:
                T[i] = right[k]
                k += 1
    return T


tab = [7, 23, 13, 29, 19, 8, 2, 1]
print(mergesort(tab))