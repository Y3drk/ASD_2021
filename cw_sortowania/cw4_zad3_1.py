'''Zadanie 3. Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
alfabetem długości k, sprawdza czy A i B są swoimi anagramami.
1. Proszę zaproponować rozwiązanie działające w czasie O(n + k).
2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo
większe od n—np. dla alfabetu unicode; złożoność pamięciowa może być rzędu O(n + k)).
Proszę zaimplementować oba algorytmy'''

# Rozwiązanie dla słów ASCII [a...Z]

def check_anagram(A, B, k):
   count_arr = [0] * k
   n = len(A)
   for i in range(n):
       count_arr[ord(A[i]) - ord('A')] += 1   #mamy jedna tablice wystapien i jednoczesnie dodajemy  do niej wystapienia liter w pierwszym słowie i odejmujemy wystapienia
       count_arr[ord(B[i]) - ord('A')] -= 1     # w drugim, jesli na koncu tablica jest samymi zerami to znaczy, że słowo jest anagramem
   for i in range(k):
       if count_arr[i] != 0:
           return False
   return True



#idea na zad 3.2 - sortowanie radix sortem bit po bicie i przejscie po obu słowach sprawdzajac czy dane znaki sa takie same
#rozwiazanie Szymona Gołębiowskiego + upgrade Falisza z asd


def alloc(num): #na potrzeby zadania - podejrzewam, ze chodzi o tablice [0,1,2,3,..,n] ale nwm na pewno
    T = [0 for i in range(num)]
    for i in range(1,num):
        T[i] = i

    return T


def super_solver(w1,w2):
    n = len(w1)
    if n != len(w2):
        return False

    counters = alloc(2**16)

    for i in range(n):   #wyzerujemy sb tylko te elementy których potrzebujemy
        counters[ord(w1[i])] = 0

    for i in range(n):  #działamy dokładnie tak samo jak wyzej
        counters[ord(w1[i])] += 1
        counters[ord(w2[i])] -= 1

    for i in range(n):  #warunek taki sam jak wyzej :))
        if counters[ord(w1[i])] != 0:
            return False

    return True

a = "TAKE"
b = "KETA"
c = "cjehrsggrefh3245689"
d = "9c8j6e5h4r2s3ghgfre"
#print(check_anagram(a, b, ord('z')-ord('A') + 1))
print(super_solver(c,d))
