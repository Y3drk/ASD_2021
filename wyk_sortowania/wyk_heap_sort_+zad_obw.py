def left(i):                      #takie oczywiste oczywistosci w strukturze heap'u ,ale tutaj chce miec to przejrzyscie
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2


def heapify(T,n,i):   # i to jedyny potencjalnie zepsuty węzeł w kopcu, T to nasz kopiec w formie tablicy, n to ilosc elementow w kopcu
    l = left(i)
    r = right(i)
    m = i                      #roboczy wskaznik na naprawiany wezeł w kopcu, chcemy go ustawic na ten z indeksów i,r,l, ktorego wartosc jest najwieksza
    if l < n and T[l] > T[m]:   #pierwszy warunek jest po to aby sprawdzic czy i nie jest końcem kopca (lisciem drzewa), czy jego dziecko po prostu istnieje
        m = l      #zamieniamy - narazie wskazania na pola tablicy by potem zamienic elementy
    if r < n and T[r] > T[m]:
        m = r #jak wyzej

    if m != i:
        T[i],T[m] = T[m], T[i]  #jesli wczesniej doszło do zamiany indeksów (czyli wezeł i faktycznie był zesputy) to zamieniamy miejscami wartosci
        heapify(T,n,m)   #wywołujemy to znowu bo moglismy naprawiajac ten wezeł zepsuc inny

        #powtarzamy, aż nie dojdzie do zamiany - czyli znowu doprowadzimy kopiec to jego poprawnej struktury


def buildheap(T):
    n = len(T)
    for i in range(parent(n - 1), - 1, -1):   #idea jest taka, że połowa elementów jest liscmi, same sa minikopcami, nie trzeba ich naprawiac, bo nie maja dzieci
        heapify(T,n,i)   #stad zaczynamy od parenta ostatniego el. i budujemy kopiec de facto naprawiając go po kolei
        # pierwsze -1 w forze jest spowodowane składnią pythona bo chcemy dojsc az do poczatku tablicy, a range działa jak działa
        # działa w czasie O(n) , ale niestety sam heapsort musi działać w O(nlogn).


def heap_sort(T):
    n = len(T)
    buildheap(T)
    for i in range(n - 1, 0, -1): #skoro zbudowalismy kopiec to na pozycji T[0] jest najwiekszy element
        T[0], T[i] = T[i], T[0]   #wiec ładujemy go na koniec tablicy czyli na jego desygnowane miejsce po sortowaniu
        heapify(T,i,0)  #ale robiac to zepsulismy kopiec, wiec musimy go naprawic, jednak nie chcemy juz dotykac tego elementu, ktory przed chwila przenieslismy
          #wiec skracamy nasz kopiec do i, (ponieważ range dziala jak działa nas poprawny element jest juz bezpieczny)


#ZADANIE OBOWIAZKOWE - zaimplementuj wstawianie dowolnego elementu do kopca
def reverse_heapify(T, i):
    p = parent(i)
    m = i
    if p >= 0 and T[p] < T[i]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify(T,m)


def insert_to_heap(T,el):
    T += [el] #dodajemy nasz element na dół kopca
    n = len(T)
    reverse_heapify(T,n-1) #przegladamy i naprawiamy kopiec idac od dołu do gory uzywajac reverse_heapify

tab = [7, 23, 13,4,5, 29, 19, 8, 2, 1]
#heap_sort(tab)
buildheap(tab)
print(tab)
insert_to_heap(tab,30)
print(tab)