'''Zadanie 7. (sklejanie odcinków) Dany jest ciąg przedziałów postaci [ai
, bi]. Dwa przedziały można
skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.
'''

# 7.1
# idea - sortujemy przedzialy po poczatkach i poczatki oraz konce oznaczamy liczbami naturalnymi (bedzie łatwiej zaklepac)
# f(i, j) = minimalna liczba przedziałów, które trzeba skleić, żeby powstał przedział od punktu i do punktu j

# wynik to maks wartosc j - i gdy wynikiem jest k

# f(i, j) = min ( f(i,k) + f(k,j)) + 1 | jesli to jest możliwe

# złożonosc algorytmu O(n^3)
# wyciaganie wyniku O(n^2)


