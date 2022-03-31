# zad3 to lider ciagu

'''Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb naturalnych długości n o zakresie wartości [0, k].
 Ma ona posiadać metodę count_num_in_range(a, b) - ma ona zwracać informację o tym, ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1).
Można założyć, że zawsze a >= 1, b <= k.
'''

#idea - tworzymy  tablice wystapien jak w countsorcie bo mamy gwarancje ze liczby w tablicy sa z zakresu [0, k ], ilosc wystapien w przedziale to C[b] - C[a] i elo jak to mówi łukasz


def structure(T,k):
    C = [0 for _ in range(k + 1)]
    for i in range(len(T)):
        C[T[i]] += 1

    for i in range(1,k+1):
        C[i] += C[i -1]

    return C


def count_num_in_range(a,b, T,k):
    I = structure(T,k)
    if a == 0:
        return I[b]
    if a != 0:
        return I[b] - I[a - 1]


test = [0,2,4,5,8, 2,3, 1, 6,7,4,2,1]
print(count_num_in_range(3,8,test,8))
