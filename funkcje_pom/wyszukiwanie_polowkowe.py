def binary_search(tab,el):
    l, r = 0, len(tab) - 1

    while l <= r:
        mid = (l + r) // 2

        if el > tab[mid]:
            l = mid + 1

        else:
            r = mid - 1

    if l < len(tab) and el == tab[l]:
        return l

    return False

print(binary_search([2,3,5,7,11,13,17,19,23,31,37],23))