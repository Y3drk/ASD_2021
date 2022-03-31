def search_sum(T,x):
    l, r = 0, len(T) - 1
    while l < r:
        if T[l] + T[r] == x:
            return True

        elif T[l] + T[r] > x:
            r -= 1

        else:
            l += 1

    return False

test = [1,2,3,4,5,6,7,8,100]
print(search_sum(test, 108))

#ponieważ tablica jest posortowana to przesuwajac w zalznosci od rozmiaru sumy T[l] + T[r] przejdziemy po wszystkich mozliwych sumach