def MINMAX(tab):
    n = len(tab)
    #i = 2
    i = 0
    if(n>=2):                   #ustawienie minimum i maximum za pomoca dwoch pierwszy elementow
        '''if tab[0] > tab[1]:
            MIN = tab[1]
            MAX = tab[0]
        else:
            MIN = tab[0]
            MAX = tab[1]'''

        MAX, MIN = tab[n-1], tab[n-1]  #dzieki temu nie potrzebujemy przypadku gdy n jest nieparzyste jak rowniez nie musimy rozwazac tego co wyzej

        while i <= n - 2:
            if tab[i] > tab[i+1]:    #n/2 porownan (porownujemy kolejne pary)
                if tab[i] > MAX:     # kolejne n/2 porownan jednego z elementow z maxem- to samo tylko w innym przypadku w *
                    MAX = tab[i]
                if tab[i+1] < MIN:  ## kolejne n/2 porownan jednego z elementow z minem - to samo tylko w innym przypadku w ^
                    MIN = tab[i+1]
            else:
                if tab[i] < MIN:   # ^   #tych ifów nie trzeba powtarzac, ale pomimo tego ze jest mniej zgrabnie to jest szybciej
                    MIN = tab[i]
                if tab[i+1] > MAX:  # *
                    MAX = tab[i+1]
            i += 2

        '''if n%2 == 1:           #w przypadkach gdy długosc tablicy jest nieparzysta wykonujemy dwa dodatkowe porownania
            if tab[i] > MAX:
                MAX = tab[i]
            if tab[i] < MIN:
                MIN = tab[i]'''

    elif n == 1:                       #skarjny przypadek gdy n==1
        MIN = MAX = tab[0]
    else:
        return

    print(MIN,MAX)

tab = [7, 23, 13, 29, 19, 8, 2, 1,78]
MINMAX(tab)
