'''
0.Lider to liczba/ klucz który występuje w tablicy/ciągu conajmniej w ilości: (n/2) + 1
1.Początkowo zakładamy, że liderem jest pierwszy element w tablicy
2.Przesuwamy się po tablicy, jeśli sprawdzana liczba jest liderem to do countera dodajemy jeden, w przeciwnym wypadku odejmujemy jeden
3.Jeśli counter osiągnie -1 to zmieniamy lidera na element obecnie sprawdzany
4.Jeśli po przejściu przez całą tablice lider jest dodatni to znaczy, że taki lider istnieje'''


def leader(T):
    n = len(T)
    leader, counter = T[0], 1
    ending_counter = 0
    for i in range(1, n):
        if T[i] == leader:
            counter += 1
        else:
            counter -= 1

        if counter == -1:
            leader = T[i]
            counter = 1

    for i in range(n):
        if T[i] == leader:
            ending_counter += 1


    if ending_counter >= (len(T) + 1) // 2:                #bo musi byc n/2 + 1 pozycji zajetych przez lidera
        print(leader)
        return True
    else:
        return False

test1 = [2,1,2,3,2,3]
test2 = [2,1,1,3,4,5,6,7,2,8]
test3 = [2,1,2,2,1,2,1,2,3]
test4 = [1,2,3]
print(leader(test1))
print("-----")
print(leader(test2))
print("-----")
print(leader(test3))
print("-----")
print(leader(test4))


