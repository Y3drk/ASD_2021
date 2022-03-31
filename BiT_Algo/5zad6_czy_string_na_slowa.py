'''Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem danego języka.
Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać spacje do wejściowego stringa,
że ciąg słów który otrzymamy tworzą słowa z danego języka. Np. “alamakotainiemapsa” możemy zapisać jako “ala ma kota i nie ma psa”.
Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe poprawne rozdzielenie stringa spacjami, jeśli oczywiście ono istnieje.
Algorytm ma być szybki, ale najważniejsze, żeby był poprawny!!!.'''

# idea - uzywamy funkcji
# f(i,j) = czy string od i do j da sie podzielic na istniejace słowa

# f(i,j) = suma logiczna ( po k od i + 1 do j -1) { f(i,k) and f(k,j) } lub dict([i:j])
# śpiewka jest taka, że sprawdzamy ofc czy cały wycinek nie jest słowem,
# jesli tak nie jest to patrzymy tez na czesci mniejsze, które potencjalnie moga tworzyc tego stringa
# widac ze "przechodzac" tak po interesujacym nas stringu korzystamy z wczesniej uzyskanych wyników

# proba implementacji, funkcja dict wykonana zostanie pod przykład

def word_checker(S):
    dictionary = ["ala", "ma","a",'ta',"kota","i","nie","ma","psa","kot","lama", "o"]
    if S in dictionary:
        return 1
    else:
        return 0


def string_screwer(S):
    n = len(S)
    F = [[None]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        #print("----")
        for j in range(i, n):
            F[i][j] = word_checker(S[i:j+1])
            #print(".....")
            #print(S[i:j + 1],F[i][j],i,j)
            for k in range(i + 1, j + 1):
                #print(S[i:k],S[k:j+1], (i,k), (k, j))
                if F[i][k - 1] == 1 and F[k][j] == 1:
                    #print("changed")
                    F[i][j] = 1


            '''for row in F:
                print(row)'''

    return F[0][n - 1]

S="alamakotainiemapsa"
S2 = 'alamakota'
print(string_screwer(S))

