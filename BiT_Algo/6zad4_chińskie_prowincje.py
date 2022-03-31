'''W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem.
Prowincję można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę, a wartość 0, że nie można.
Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i, to miasta o indeksach j takich, że abs(i-j) < k są przez nią chronione.
Należy zaproponować algorytm, który stwierdzi ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe.'''

# idea
# stosujemy algorytm zachłanny - stawiamy stację na najdalszej 1, która umozliwia ochrone całego przedzialu od naszej poczatkowej pozycji
# nastepnie przeskakujemy o 2k -1 do przodu i probujemy dalej chronic zakładany obszar, jesli nie wylądujemy na 1
# to cofamy się aż do skutku,
# jesli cofając się dotarlibysmy z powrotem do pola z wczesniej zbudowana stacja to znaczy, że nie mozemy ochronic danego zakresu, zwracamy -1

# jesli przejdziemy i ochronimy cała prowincję zwracamy liczbe stacji

#ciche zał : zasieg stacji zaczyna sie na niej samej a konczy k -1 elementów dalej włącznie

# złożonosc O(n) - po kazdym polu przejdziemy maksymalnie dwa razy


def chineese_stations(P,k):
    # 8 oznacza zbudowana stacje
    n = len(P)
    stations = 0
    ind = n
    prev = n
    for i in range(k - 1,-1,-1): # początkowy przypadek, odrobine rózny od kolejnych bo nie zaczynamy od skoku
        if P[i] == 1:
            stations += 1
            ind = i
            P[i] = 8

    if ind == n:
        return -1
    else:
        #print("Zbudowalismy pierwszą stacje w wiosce:", ind)
        while True:
            prev = ind
            #print("zbudowalismy kolejna stacje w wiosce:",ind)
            #print(P)
            if ind + (2 * k)- 1 < n:
                ind += (2 * k)- 1
            else:
                ind = n - 1

            #print("jestesmy w wiosce:",ind)

            if P[ind] == 1:
                P[ind] = 8
                stations += 1

            else:
                while P[ind] != 8:
                    ind -= 1
                    #print("Sprawdzamy wioske:",ind,"pod stacje")
                    if P[ind] == 1:
                        P[ind] = 8
                        stations += 1
                        break

            if ind == prev:
                #print("wbitka")
                return -1

            if ind + k - 1 >= n - 1:
                return stations


test1 = [0,0,1,0,1,1,0,0,1,0,1,1,0,1]
k = 3
print(chineese_stations(test1,k))
print(test1)
print("-----")
test2 = [0,0,1,0,1,0,0,0,0,0,1,1,0,1]
k = 3
print(chineese_stations(test2,k))
print(test2)







