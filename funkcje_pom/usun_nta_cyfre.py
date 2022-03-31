def del_n_dig(num,n):
    import math
    dl = math.floor(math.log10(num) + 1)

    left_side = num // 10**(dl - n + 1)
    print(left_side)
    right_side = num % 10**(dl - n)
    print(right_side)
    new = left_side*10**(dl - n) + right_side

    return new

print(del_n_dig(9876,4))
