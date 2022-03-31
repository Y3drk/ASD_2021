'''Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje tę tablicę w czasie O(n).
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
'''

#idea - sortujemy słowa do pudełek wg ich długosci, nastepnie sortujemy stabilnie od najmniej znaczacej litery odpowiednio łącząc ze soba kolejne pudełka tak, by za kazdym razem
#ostatnim kubełkiem branym pod uwage był ten , gdzie sortowanie odbyłoby sie wg ostatniej litery


def count_sort(T,k,ind):   #do radixa potrzebujemy jakiejs innej stabilnej metody sortowania. Ja uzyje tutaj count sorta bo jest po prostu najszybszy, a znamy ilosc liter.
    n = len(T)
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


def sort_words(T): #ciche załozenie, ze nie ma tzw słow pustych, czyli takich o długosci 0
    n = len(T)
    maxi = -1
    for i in range(n):  #znalezienie najdłuzszego słowa
        maxi = max(maxi, len(T[i]))

    B = [[] for _ in range(maxi)]   #stworzenie pudełek

    for i in range(n):  #słowa do pudełek
        B[len(T[i]) - 1] += [T[i]]

    '''for i in range(maxi): #test poprawnosci wstawiania do pudełek
        print(B[i])
    print("....")'''
    for i in range(maxi - 1, -1, -1):
        count_sort(B[i],26,i)
        B[i - 1] += B[i] #łączenie pudełek
        B[i] = [] #opróżnianie tablicy
        '''for j in range(maxi): #test
            print(B[j])
        print("----")'''

    T = B[maxi - 1] #zwracanie wyniku do naszej wyjsciowej tablicy
    return T


test = ["chuj", "idiota", "debil","konsternacja","siatkowka","honda","aleksandra", "falisz", "to", "najwiekszy", "szef", "bez", "kitu", "kozak","i","tyle"]
print(sort_words(test))

#Konieczena modyfikacja - zamiast pudeł od długosci słów sortowanie słów po długosci, żeby nie miec sytacji skipowania miliona kubełków !!!!
# piotrek to rozwiązał i asymptotycznie wychodzi to samo

