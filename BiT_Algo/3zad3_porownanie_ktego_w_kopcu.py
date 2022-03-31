'''Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based heap).
 Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x.'''

# nieoptymalnie - usuwamy element z korzenia i odpalamy heapify- tak k - 1 razy i sprawdzamy root'a. O(klogn)

#idea - optymalna - zaczynajac od korzenia schodzimy maksymalnie w lewo sprawdzajac warunek x < T[i], jednoczesnie zwiekszajac licznik elementów, które sprawdzilismy
#robimy tak dopóki :
# a) znajdziemy przynajmniej k wierzchołków o wartości < x; jeżeli tak się stanie, to k-ty wierzchołek musiał być mniejszy od x, a więc zwracamy fałsz
# b) wyczerpiemy wierzchołki o wartości < x, zanim znaleźliśmy ich k; jeżeli tak się stanie, to dalsze wierzchołki muszą być >= x, a zatem k-ty też, więc zwracamy prawdę

#Złożoność: sprawdzamy tylko dzieci wierzchołków o wartości < x, a tych jest co najwyżej k (jeżeli byłoby więcej, to przerywamy zgodnie z opisem powyżej);
#każde może mieć co najwyżej 2 dzieci, więc odwiedzamy co najwyżej 3k wierzchołków, a więc mamy O(k).


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2


def compare_kth_to_x(T,k,x,ind):
    n = len(T)
    global counter
    print("actual:", T[ind], ind, counter)

    if counter >= k:   # opcja a)
        return False

    if left(ind) >= n:  #jesli nie możemy pojsc już w dół
        return


    '''if left(ind) >= n:    #powrót w góre kopca   #bez sensu , musielibysmy wprowadzic jakies oznaczenie w jakim węźle juz bylismy
        return compare_kth_to_x(T,k,x,parent(ind))'''

    if T[left(ind)] < x:   #zejscie w dół w lewo
        counter += 1
        res_l = compare_kth_to_x(T,k,x,left(ind))
        if res_l == False:
            return False

    if right(ind) < n and T[right(ind)] < x:  #zejscie w dół w prawo
        counter += 1
        res_r = compare_kth_to_x(T,k,x,right(ind))
        if res_r == False:
            return False

    if T[left(ind)] >= x and (right(ind) < n and T[right(ind)] >= x):  #znajdujemy juz elementy wieksze
        return


def laucher(T,x,k):
    global counter
    if T[0] >= x:
        return True
    else:
        counter += 1
        if compare_kth_to_x(T,k,x,0) != False:
            return True
        else:
            return False


test = [2,4,3,7,5,6,5,8,10,17]
k = 4
x = 6
counter = 0
print(laucher(test,x,k))