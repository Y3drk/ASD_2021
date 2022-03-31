'''Proszę zaimplementować funkcję sortującą (rosnąco) listę jednokierunkową metodą
QuickerSort. Algorytm QuickerSort to odmiana algorytmu QuickSort, w której funkcja
podziału dzieli sortowane dane według przyjętej wartości x na trzy grupy: mniejsze od x, równe
x, oraz większe od x. Następnie rekurencyjnie sortowane są grupy pierwsza i trzecia. Państwa
funkcja powinna mieć następujący prototyp:
struct Node { Node* next; int val; };
Node* QuickerSort ( Node* head )
Argumentem funkcji jest wskaźnik na głowę listy do posortowania a wynikiem powinien być
wskaźnik na głowę listy posortowanej. Sortowanie powinno polegać na porównywaniu wartości
val list oraz przepinaniu wskaźników next.
'''

