'''Zadanie 4. Pewien eksperyment fizyczny generuje bardzo szybko stosunkowo krótkie ciągi liczb całkowitych z przedziału od 0 do 109 −1. Pomiar w eksperymencie polega na okresleniu ile różnych liczb znajduje się
w danym ciągu. Niestety liczby są generowane tak szybko, że konieczne jest zagwarantowanie czasu działania rzędu O(1) na każdy element ciągu (pamięć jest dużo mniej krytycznym zasobem). Ciągi są generowane
błyskawicznie, jeden po drugim. Proszę zaproponować strukturę danych pozwalającą na przeprowadzenie
eksperymentu.'''

#Założenie jest takie, że mamy dużo pamięci, więc tworzymy tablice o długosci 10^9 + 1, gdzie indeksy sa utożsamiane z wartosciami liczb, a na ostatnim polu mamy licznik unikalnych wystapień.
#Zachowujemy sobie równiez, "globalny" licznik nr ciągu (i). Idąc po i-tym ciągu sprawdzamy pole T[wartosc_liczby] jesli nie ma na nim liczby i to ją tam umieszczamy oraz zwiekszamy
#licznik unikalnych liczb w ciągu, jesli wartosc i juz tam jest nie robimy nic. Po przejsciu całego ciagu zczytujemy wynik z ostatniego pola i zerujemy je. Zakładając, że liczba prób
#w wyniku których powstaje ciąg jest skończona (nawet jesli jest bardzo duza) i mamy duzo pamieci to ten sposób jest najlepszym rozwiazaniem.

#od Falisza - "hardkorowo assemblerowo / C"
#tablica liczników wypełniana losowymi wartosciami, a obok tworzymy sobie stos zaimplementowany na tablicy liniowej, zasada jest taka, w kazdym polu tablicy liczników trzymam jakas wartosc
#i wskaznik na numer pola na stosie. poczatkowo stos jest pusty czyli nie mamy na nim nic. Jesli w ciagu zobaczymy np. 3 to patrzymy na indeks 3 w tab liczników, tam mamy np. 7 i wskazanie
# poza stos bo nie mamy przeciez na nim niczego i łatwo mozna sprawdzic, ze tak jest. To nam mówi ze wartosc 7 jest błedna wiec ją mazemy razem z wartoscia wskaznika stosu, zastepujemy
#ją jedynka a wskaznik umieszczamy na poczatek stosu, a w stosie umieszczamy na 1 miejscu wskazanie na ten nasz element z powrotem na pole nr 3, potem sytuacja sie powtarza dla kolejnych el stosu.
#jesli spojrzymy znowu na 3 to zwiekszamy 1 na 2 bo jest ok. Jesli wskaznik prawidłowo wskazuje na stos, ale na stosie jest wskaznik na inna pozycje to tez jest to błedne i naprawiamy to w
#ten sam sposob co wczesniej
#operacja reset to tylko zapamietanie, że na stosie mamy zero wartosci
'''
Zadanie 5. Zakładamy model obliczeń, w którym można dodawać, mnożyć, i porównywać liczby. W tym
modelu pokazano, że sortowanie n liczb ma złożoność Ω(nlog n). Proszę udowodnić, że w tym modelu obliczeń
znalezienie otoczki wypukłej n punktow w 2D ma złożoność Ω(nlog n).
'''

#mapujemy liczby na punkty p(xi, xi^2) - O(n) - jest w docsach, ale nie ogarniam tego xdd
#
#
#
#ogarnac u falisza  !!!!! - nie było :(((
