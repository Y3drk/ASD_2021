'''Mamy dany ciąg napisów (słów) S = [s1, ..., sn] oraz pewien napis t. Wiadomo, że t można zapisać jako złączenie pewnej ilości napisów z S (z powtórzeniami).
Na przykład dla S = [s1, s2, s3, s4, s5] gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, napis t = ababbab można zapisać, między innymi, jako s2s4 lub jako s1s1s3s5.
Taki wybór konkretnych si nazywamy reprezentacją. Przez szerokość reprezentacji rozumiemy długość najkrótszego si należącego do reprezentacji
- dla s2s4 szerokość to 3, a dla s1s1s3s5 szerokość to 1.
Zaimplementuj algorytm, który mając na wejściu S oraz t znajdzie maksymalną szerokość reprezentacji t (tzn. najkrótszy napis w jej reprezentacji jest najdłuższy).
 Oszacuj czas działania algorytmu.
'''

# idea - będziemy korzystac z funkcji f(i) = maks. długosc reprezentacji ciagu kończącego się na i
# f(i) = max (po j od 0 do i){d}
# gdzie d = min{f(i - len(s), len(s)}
# zatem ostatecznie f(i) = maks (po j od 0 do i) {min ( po s nalezacym do S) [ f( i - len(s), len(s) ] jesli wzorzec pasuje)}

# złożonosc : O(n*s) gdzie s to ilosc słow w S, a n to długosc napisu t


def longest_repr(S,t):
    n = len(t)
    F = [-1] * (n + 1)
    for i in range(n + 1):
        #print("i:",i)
        for s in S:
            substring = t[i - len(s):i]
            if i > len(s):
                if s == substring: #sprawdzenie czy wzorzec pasuje
                    F[i] = max(F[i], min(len(s), F[i - len(s)]))
            elif i == len(s):
                if s == substring:
                    F[i] = max(F[i], len(s))
    #print(F)
    return F[n]


S = ['ab', 'abab', 'ba', 'bab', 'b']
t = 'ababbab'
print(longest_repr(S,t))
