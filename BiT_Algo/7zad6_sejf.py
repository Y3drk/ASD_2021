'''Dostałeś sejf, ktory odblokowuje sie 4 cyfrowym pinem (od 0000 do 9999).
Zamiast pin-pada mamy dostepny wyswietlacz, na którym znajduje sie kilka liczb od 1 do 9999.
Sejf jest bardzo orginalny. Wcisniecie danego przycisku powoduje dodanie liczby na nim do aktualnej wartosci, a w przypadku
przekroczenia wartosci 9999 pierwsza cyfra zostaje obcieta (%10^4).
Dane są PIN i liczby na wyswietlaczu oraz wartosc poczatkowa,znajdź najkrótsza sekwencje nacisnięć, która pozwoli na wpisanie pinu lub zwroci None jesli jest to ]
niemożliwe'''

# idea - modyfikujemy BFS'a, olewamy visit, zakładamy ze ten sam przycisk mozna kliknąc kilka razy z rzedu wiec ignorujemy takze pole parent, zamiast tego
# utrzymujemy dosyc duża aczkolwiek o stałej wielkości tablice wystąpień wartosci. Jesli jakas liczba już wczesniej sie pojawiła to nie wykonamy działania,
# które dałoby ja po raz kolejny, olewamy takze distance, a zamiast tego do kolejki dodajemy krotki.
# jesli znajdziemy pin przerywamy i zwracamy ilosc kliknietych liczb.
# jak rozpoznac, że stworzenie pinu jest niemozliwe ? Prawodpodobnie można tak uznac, gdy kolejka stanie sie pusta, ergo nie bedziemy mogli stworzyc zadnej
# nowej liczby, a nie osiagniemy pinu

# tutaj jako reprezentacja powinna de facto wystarczyc Tablica liczb


def PIN_BFS(G,start,PIN):
    from queue import Queue
    distance = 0
    values = [False for _ in range(10**4)]
    Q = Queue()
    values[start] = True
    Q.put((start,distance))

    while not Q.empty():
        base,d = Q.get()
        for v in G:
            new = base + v
            if new > 9999:
                new = new % 10000

            if not values[new]:
                distance = d + 1
                values[new] = True
                if new == PIN:
                    return distance
                else:
                    Q.put((new,distance))

    return None


panels = [13,223,782,3902]
start1 = 67
PIN1 = 888
start2 = 1234
PIN2 = 4747
print(PIN_BFS(panels,start1,PIN1))
print(PIN_BFS(panels,start2,PIN2))

#chyba działa
