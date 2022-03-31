def is_prime(x):
    if x == 2 or x == 3:
        return True

    if (x % 2 == 0 and x != 2) or x == 1:
        return False

    licz = 3
    while licz <= x ** (1/2):
        if x % licz == 0:
            return False
        else:
            licz += 2

    return True

print(is_prime(18))