def del_1st_dig(x):
    import math
    lght = math.floor(math.log10(x))
    tmp = x % (10 ** lght)
    return tmp

print(delete_1st_dig(123))