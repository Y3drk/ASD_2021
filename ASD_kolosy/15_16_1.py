'''. Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:
suma elementów od 0 do n-1 <= suma elementów od n do 2n - 1 <= ... <= suma elementów od n^2 - n do n^2 - 1
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową.'''

# idea -
# 0) mamy dodatkową tablice - jedna z wartoscia sumy i liczbami ją tworzacymi
# 1) przechodzimy po tablicy i zliczamy sumy na ww przedziałach (o stałej długosci n) oraz wpisujemy liczby ją tworzące do nowej tablicy -> O(n^2)
# 2) sortujemy sumy po wartosciach - quicksortem lub radix sortem z count sortem - i tak przejscie po tablicy przykrywa tę złożoność -> O(n*log(n)) / O(n*10)
# 3) przepisujemy liczby tworzace sume do tablicy w odpowiedniej kolejnosci

# Złożonosc O(n^2)


def partition_random_for_sumsort(T, p, r):
    from random import randint
    rdm = randint(p,r)
    T[rdm], T[r] = T[r], T[rdm]

    x = T[r][0]
    i = p - 1
    for j in range(p, r):
        if T[j][0] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_mem2(T,p,r):   #ogolna złożonosc quicksorta O(nlogn)
    while p < r:
        q = partition_random_for_sumsort(T, p, r)
        if q - p <= r - q:
            quick_sort_mem2(T, p, q - 1)
            p = q + 1


        else:
            quick_sort_mem2(T, q + 1, r)

            r = q - 1


def sum_sort(A):
    nsq = len(A)
    I = [[None]* (int(nsq**(1/2)) + 1) for _ in range(int(nsq**(1/2)+ (1/2)*nsq**(1/2)))] # krok (0)
    cnt, sm = 1, 0
    sum_cnt = 0

    for i in range(nsq):
        if cnt == (int(nsq**(1/2)) + 1):
            I[sum_cnt][0] = sm
            cnt = 1
            sm = 0
            sum_cnt += 1

        sm += A[i]
        I[sum_cnt][cnt] = A[i]
        cnt += 1


    I[sum_cnt][0] = sm #case domykajacy ostatnia sume
    #print(I)


    quick_sort_mem2(I,0, sum_cnt)
    #print(I)
    cnt, sum_cnt = 1, 0
    i = 0
    while i < nsq:
        #print("wbitka",i)
        if cnt == (int(nsq**(1/2)) + 1):
            cnt = 1
            sum_cnt += 1

        if I[sum_cnt][cnt] != None:
            A[i] = I[sum_cnt][cnt]
            cnt += 1
            i += 1
        else:
            cnt += 1

    return A


test = [3,6,8,10,11,24,46,45,88,101,2,21,16,7,13,0,17,23,77, 31,33,10,6,37]
#print(len(test))
print(test)
print(sum_sort(test))







