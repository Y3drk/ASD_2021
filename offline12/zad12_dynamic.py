# korzystamy z dynamicznej funkcji f(i) = maksymalna wysokosc wieży skaładajacej sie z kolcków od 0 do i oraz konczacej sie klockiem itym
# f(0) = wysokosc zerowego klocka
# f(i) = (po k od 0 do i - 1)  max [jezeli klocki sie zaczepiaja] {f(k)} + wysykosc itego klocka

# złożonosc :
# czasowa O(n^2)
# pamieciowa O(n)

def block_height(K):
    n = len(K)
    F = [0 for _ in range(n)]
    F[0] = K[0][2]

    for i in range(1,n):
        maxi = 0
        for j in range(i):
            if K[j][0] <= K[i][1] <= K[j][1] or K[j][1] >= K[i][0] >= K[j][0]:
                maxi = max(maxi,F[j])

        F[i] = maxi + K[i][2]

    #print(F)
    return max(F)


K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R1 = 5

K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R2 = 6

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")
