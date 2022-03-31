'''Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.'''


#idea -
# 1) przepisujemy wszystkie podciagi długosci k do nowej tablicy  O(n)
# 2) wykonujemy radix sorta na nowej tablicy - O(m) gdzie m to liczba powastałych ciagów ( zawsze mniejsza lub równa n, jesli k = 0 zwracamy słowo zerowe - None)
# 3) wiemy ze te same ciagi sa po sobie wiec zliczamy ich ilosc, utrzymuja zmienna z najwieksza iloscia wystapien i ciag ktory tak wystepował.


def count_sort(T,k,ind):
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


def radix_sort(T,k):
    #n = len(T)
    '''for i in range(n):    #dodatkowy case jesli komuś sie zachce duzych liter w słowie
        T[i] = T[i].lower()'''

    for j in range(k - 1,-1, -1):  #sortujemy stabilnie dla kazdej pozycji osobno, zaczynajac od najmniej znaczacej
        count_sort(T,2,j)

    return T


def longest_substring(T,k):
    if k == 0:
        return None

    n = len(T)
    I = []      #nowa tablica   #abbaaaabba -> aba bab aba baa ...  zawsze n - k + 1
    for i in range(2, n):  # krok 1
        I += [T[i-(k - 1):i+1]]  #czy slicing tu jest ok ? - dla k <<< n tak dla wiekszych nie

    #print(I)
    radix_sort(I,k)  #krok 2
    #print(I)

    most = 1
    top = None
    tmp = I[0]
    cnt = 1
    for i in range(1,len(I)):
        if I[i] == tmp:
            cnt += 1
            if cnt > most:
                top = tmp
                most = cnt
        else:
            tmp = I[i]
            cnt = 1

    return top


test = 'ababaaaabb'
print(longest_substring(test,3))


#chyba works
# Złozonosc O(n) chyba ze slicing cos psuje


