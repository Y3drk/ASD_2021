'''Alicja chce zorganizować przyjęcie i zastanawia się, kogo zaprosić spośród n znajomych. Stworzyła już listę par osób które się znają.
Chce wybrać możliwie jak najwięcej osób, tak aby spełnione były dwa warunki: na przyjęciu każda osoba powinna znać co najmniej 5 osób oraz co najmniej 5 osób nie znać.
Zaproponuj algorytm który przyjmuje na wejściu listę n osób oraz listę par osób które się znają, a na wyjściu daje możliwie najdłuższą listę gości.
'''


# idea -  tworzymy tablice z 3 rodzajami danych [ is_invited - czy osoba jest zaproszona, counter - ilosc osob które ona zna i sa zaproszone, lista znajmoych]
# uzupełniamy ta liste odpowiednio na podstawie par, ktore otrzymalismy jako wejscie
# nastepnie usuwamy dana osobe jesli zna zbyt wiele ( > n - 5) lub zbyt mało ( < 5) osob - zamieniamy is invited na 0 i zmniejszamy counter wszystkich osob które ja znają

#ciche zał: osoby sa indeksowane od 0, znajmomosci sa mutualne

def alices_party(F, n):
    T = [[1,0] for i in range(n)]

    for i in range(len(F)):
        p1, p2 = F[i][0], F[i][1]
        T[p1][1] += 1
        T[p1] += [p2]
        T[p2][1] += 1
        T[p2] += [p1]

    '''for person in T:
        print(person)
    print("----")'''
    for i in range(n):
        if T[i][1] < 2 or T[i][1] > n - 2 - 1:   #zgodnie z trescia zamiast dwójki powinna byc 5, zmieniłem aby łatwiej było wymyslic przykład, dod. -1 bo zakładamy ze zna sama siebe
            T[i][0] = 0
            for j in range(2,len(T[i])):
                T[T[i][j]][1] -= 1

    '''for person in T:
        print(person)'''

    counter = 0
    for i in range(n):
        if T[i][0] == 1:
            counter += 1

    return counter


test1 = [(0,1),(4,3),(2,3),(1,4),(2,0), (4,0),(8,3),(7,2),(9,1),(6,2),(4,8),(6,5),(5,7),(5,0),(6,1),(2,8),(5,2),(2,1),(2,4)]
print(alices_party(test1,10))

#WYDAJE SIE DZIALAC ALE CIEZKO WYMYSLIC SENSOWNY PRZYKLAD

