def count_inversions_with_merge(T):
    global inv
    n = len(T)
    if n > 1:
        mid = n // 2
        left = T[:mid]
        right = T[mid:]
        count_inversions_with_merge(left)
        count_inversions_with_merge(right)

        j, k = 0, 0
        guard_l, guard_r = 10 ** 3, 10 ** 3
        left += [guard_l]
        right += [guard_r]
        for i in range(n):
            if left[j] <= right[k]:
                T[i] = left[j]
                j += 1
            else:
                T[i] = right[k]
                k += 1              #na geeks for geeks jest (mid - j + 1) ale u nas to zadziała bez tego, bo inaczej liczylibyśmy strażnika
                inv += (mid - j)  #jesli bierzemy element z prawej strony to oznacza, że jest srodek - lewy indeks inwersji, bo...
    return T                        # obie strony sa posortowane, zatem jesli juz znajdziemy taki moment , ze left[j] > right[k] to wszystkie
                                    #elementy w lewej stronie sa wieksze od right[k] czyli miałby te inwesje az do srodka


test1 = [6, 9, 7, 1, 5, 8, 10, 13, 30, 70, 16, 88, 11]
test2 = [1, 20, 6, 4, 5]
inv = 0
count_inversions_with_merge(test2)
print(inv)
