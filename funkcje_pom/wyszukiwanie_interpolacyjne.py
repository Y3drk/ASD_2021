def interpolation_search(tab, el):  #bs tylko dużo szybciej zawęza przedział
    import math
    l, r = 0, len(tab) - 1

    while l <= r:
        #print(":)")
        #print("Left value:", tab[l])
        #print("right value:", tab[r])

        if tab[l] <= el <= tab[r]:
            mid = l + math.floor(((el - tab[l])*(r - l))/(tab[r]-tab[l]))
            #print('mid:', mid)

            if el > tab[mid]:
                l = mid + 1

            else:
                r = mid - 1

        #print("----")

    if l < len(tab) and el == tab[l]:
        return l

    return False