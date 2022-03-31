'''W planie szkolnym mamy n zajęć, każde trwało od ai do bi
, należy zaimplementować taki algorytm
dynamiczny, który sprawdzi, czy można wybrać k zajęć tak, by żadne zajęcia się na siebie nie nakładały
i sumaryczna długość wszystkich przerw między nimi była jak najmniejsza.'''

# zał. otrzymane zadania sa posortowane po poczatkach i koncach (w tej kolejnosci)

#idea - skorzystamy z funkcji dynamicznej f(i,j) = najmniejsza przerwa miedzy j zajeciami konczacymi sie i-tymi zajeciami
# warunki brzegowe
# f(0,j) = 0
# f(i,0) = 0

# f(i,j) = min (po l od 0 do i-1) {jesli zajecia lte i ite na siebie nie nachodza} [ f(l,j-1) + poczatek itych - koniec ltych ]

# złożonosc O(n^2*k)


class Job:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __str__(self):
        return "( " + str(self.start) + " - " + str(self.end) + " )"


def impatientBobby(J,n,k):
    # tu umiesc implementacje
    F = [[float('inf') for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        F[i][0] = 0
        F[i][1] = 0

    for j in range(2,k+1):
        for i in range(1,n):
            for l in range(i):
                if J[l].end <= J[i].start:
                    F[i][j] = min(F[i][j], F[l][j - 1] + J[i].start - J[l].end)

    '''for row in F:
        print(row)

    print("-----")'''

    best = float('inf')
    for i in range(n):
        #print(i,k)
        #print(F[i][k])
        best = min(best, F[i][k])

    if best == float('inf'):
        return -1

    else:
        return best

J = [Job(1,2),Job(2,3)]
k = 2
print(impatientBobby(J,len(J),k))

if __name__ == "__main__":
    from zad3testy_ip import runtests
    runtests(impatientBobby)
