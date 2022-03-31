'''Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
każdej z liczb'''

# korzystamy niemalże z pomysłu z bit algo

# f(i,j) = minimalna liczba skoków do i-tego kamienia, mając dokładnie j energii po zjedzieniu ciastka z A[i]

# f(i, 0 do A[0]) = 0
# f(i, od A[0] + 1) = inf bo nie da sie

# pomysł z bitu - f(i,j) = min (po k od 1 do i) { f(i-k,max{y+k-a[y],0})} + 1
# pomysł z asd - f(i,j) = min (po k od 0 do i) { f(k, j + i - k - A[i]) | j + i - k - A[i] >= 0} + 1

# ogl do zaklepania, cos sie jebie

