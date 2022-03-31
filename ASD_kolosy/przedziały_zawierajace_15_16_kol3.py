'''3. Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.'''

# jesli moga na siebie nachodzic, a moga, to sortujemy po poczatkach a potem po koncach i ...
# bierzemy te zaczyajace sie najwczesniej (jesli nie zaczyna sie w 0 to od razu false i elo) i wsród nich szukamy tego konczacego sie najpózniej
# po kazdym przedziale przejdziemy stała liczbe razy (wydaje mi sie ze maksymalnie dwa ale to sie jeszcze sprawdzi) wiec złoznosc jest narzucona przez
#sortowanie O(nlogn)


def covering_with_intervals(T):
    n = len(T)
    T.sort() #O(nlogn)
    chosen = []
    int_cnt = 1

    #print(T)

    if T[0][0] > 0:
        return False

    else:
        ind = 1
        curr_beg = 0
        curr_end = T[0][1]
        curr_int = 0
        while ind < n:
            #print("-----")
            #print(ind, T[ind], int_cnt)
            if T[ind][0] == curr_beg:
                curr_end = T[ind][1]
                curr_int = ind
                ind += 1

            elif T[ind][0] != curr_beg:
                #print('wybieramy nowy przedzial')
                int_cnt += 1
                chosen.append(T[curr_int])
                best = -1
                best_ind = None
                while ind < n and T[ind][0] <= curr_end:
                    #print(ind, T[ind])
                    if best < T[ind][1]:
                        best = T[ind][1]
                        best_ind = ind

                    ind += 1
                    #best = max(best, T[ind][1])

                curr_beg = T[best_ind][0]
                curr_end = best
                curr_int = best_ind

            else:
                ind += 1

    chosen.append(T[curr_int])
    print(chosen)
    if curr_end != 1:
        return False

    else:
        return int_cnt


T0 = [(0.88, 1),(0.65, 0.9),(0,0.15), (0.2, 0.4),(0.1, 0.7), (0.13, 0.85), (0, 0.3)]
odp0 = 4
print("odp:",covering_with_intervals(T0))
print("-----")
T1 = [(0.65, 0.9),(0,0.15), (0.2, 0.4),(0.1, 0.7), (0.13, 0.85), (0, 0.3)]
odp1 = False
print("odp:",covering_with_intervals(T1))
print("-----")
T2 = [(0,0.4),(0.1,0.5),(0,0.2),(0.3,0.7),(0.7,1)]
print(covering_with_intervals(T2))
odp2 = 3
#[(0, 0.4), (0.3, 0.7), (0.7, 1)]
print("-----")
T3 = [(0,0.5),(0.1,0.6),(0.2,0.7),(0.3,0.8),(0.4,0.9),(0.5,1)]
#[(0, 0.5), (0.5, 1)]
odp3 = 2
print(covering_with_intervals(T3))




