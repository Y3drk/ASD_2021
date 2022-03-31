def digit(num, n):
    import math
    dl = math.floor(math.log10(num) + 1)

    return (num // 10 ** (dl - n) ) % 10**( n - 1)

print(digit(1234,2))