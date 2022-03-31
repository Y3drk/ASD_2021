'''Zadanie 2. (spójność krawędziowa) Dany jest graf nieskierowany G = (V, E). Mówimy, że spójność
krawędziowa G wynosi k jeśli usunięcie pewnych k krawędzi powoduje, że G jest niespójny, ale usunięcie
dowolnych k − 1 krawędzi nie rozspójnia go. Proszę podać algorytm, który oblicza spójność krawędziową
danego grafu.'''

# ustalamy jedno zródło, a krawedziom nadajemy wage 1, z niego puszczamy przepływ do kazdego innego wierzchołka, z tego najwieksza wartosc bedzie odpowiedzia


'''Zadanie 3. (Formuły logiczne z dwoma wystąpieniami zmiennej) Dana jest formuła logiczna
postaci: C1 ∧ C2 ∧ ⋯ ∧ Cm, gdzie każda Ci to klauzula będąca alternatywą zmiennych i/lub ich zaprzeczeń.
Wiadomo, że każda zmienna występuje w formule dokładnie dwa razy, raz zanegowana i raz niezanegowana.
Na przykład poniższa formuła stanowi dopuszczalne wejście:
(x ∨ y ∨ z) ∧ (y ∨ w) ∧ (z ∨ v) ∧ (x ∨ w) ∧ (v).
Proszę podać algorytm, który oblicza takie wartości zmiennych, że formuła jest prawdziwa.'''

# nie było na ćwiczeniach


'''Zadanie 5. (rozłączne ścieżki) Dany jest graf skierowany G = (V, E) oraz wierzchołki s i t. Proszę
zaproponować algorytm znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.
'''

# kazda krawedz ma wage 1, odpalamy pzepływ, wartosc jest odpowiedzia

