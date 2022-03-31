'''Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować algorytm,
 który usunie ze stringa duplikaty tak, że otrzymany string będzie leksykograficznie najmniejszy.
Przykład: cbacdcbc, odpowiedzią jest acdb.

Wskazówka:
ord(“a”) = 97; ord(“b”) = 98; ... ; ord(“z”) = 122
'''

# idea - zliczymy wystąpienia liter szukając duplikatów
# uzywamy stosu
# przechodzimy po literach i sprawdzamy nastepujace warunki, jednoczesnie odpowiednio zmniejszajac liczbe wystapien znaku
# (1) czy stos jest pusty ?
# (2) czy sprawdzana wartosc jest mniejsza od tej na górze stosu?
# (3) czy -||- ma jakies duplikaty?
# (4) czy znak jest juz w stosie ?

# (1) jesli tak to musimy dodac element na stos
# (2) jesli tak to i jednoczesnie wartosc z góry stosu ma jeszcze duplikaty, to usuwamy ja i dodajemy obecnie sprawdzany element
# (4) wtedy nie wpisujemy znaku na stos


# ciche zał. uzywamy tylko małych liter alfabetu łacinskiego (ułatwia implementacje, mozna ofc sobie poradzic i z tym problemem)


def delete_duplicates(S):
    n = len(S)
    in_stack = [0 for _ in range(26)]
    D = [0 for i in range(26)]
    Stack = []

    for i in range(n):   #zliczanie wystapień
        D[ord(S[i]) - 97] += 1

    #print("Duplikaty:",D)

    for i in range(n):
        #print("Sprawdzna litera:",S[i],"na pozycji:",i)
        if len(Stack) == 0:
            Stack += [S[i]]
            D[ord(S[i]) - 97] -= 1
            in_stack[ord(S[i]) - 97] = 1

        elif in_stack[ord(S[i]) - 97] == 1:
            #print("wbitka 0")
            tmp = Stack[len(Stack) - 1]
            if D[ord(tmp) - 97] > 0 and ord(tmp) > ord(S[i]):
                Stack.pop()
                in_stack[ord(tmp) - 97] = 0
                D[ord(S[i]) - 97] -= 1

        else:
            tmp = Stack[len(Stack) - 1]
            #print("top stacka:",tmp)
            if D[ord(tmp) - 97] > 0 and ord(tmp) > ord(S[i]):
                #print("wbitka 1")
                Stack.pop()
                in_stack[ord(tmp) - 97] = 0
                Stack += [S[i]]
                D[ord(S[i]) - 97] -= 1
                in_stack[ord(S[i]) - 97] = 1

            elif D[ord(tmp) - 97] == 0 or ord(tmp) < ord(S[i]):
                #print("wbitka 2")
                Stack += [S[i]]
                D[ord(S[i]) - 97] -= 1
                in_stack[ord(S[i]) - 97] = 1


        #print(Stack)
        #print("----")

    for i in range(len(Stack)):
        print(Stack[i],end=', ')
    print()

    return


test1 = 'cbacdcbc'
test2 = 'cbacdcbcd'
delete_duplicates(test1)
print("----")
delete_duplicates(test2)


