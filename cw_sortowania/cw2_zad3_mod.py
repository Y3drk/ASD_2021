def find_sum(A):
    n = len(A)
    if n < 4:     # wszystkie wejscia ktore nie mają opcji zadziałac odrzucamy z buta
        return False

    for pocz in range(n):             #druga para elementów może znajdowac się tylko pomiędzy tymi wybranymi wczesniej
        for kon in range(pocz+1, n):     #wiec przechodzimy po wszystkich mozliwych wyborach i szukamy miedzy nimi innej pary o tej samej sumie
            x = A[pocz] + A[kon]
            i = pocz + 1
            j = kon - 1
            while i < j:
                if x == A[i] + A[j]:
                    return True
                if x > A[i] + A[j]:
                    i += 1
                else:
                    j -= 1
                   
    return False


test = [0,0,1,1,1,4,5,6,7,8]
print(find_sum(test))