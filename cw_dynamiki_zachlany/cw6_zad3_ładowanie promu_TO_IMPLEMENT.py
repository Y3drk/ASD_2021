'''Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.'''

# UWAGA MOZNA SB TUTAJ PORADZIC TABLICA 2D

# ale ten pomysł jest w 3D

# idea - f(i,g,d) = funkcja boolowska { 1 gdy pierwsze i samochodów można rozmiescic na promie tak, że zostaje g maiejsca na górze i d na dole, 0 wpp }

# odp = max (po n,g ,d gdy g, d >= 0) { i | (jesli) f(i,g,d) = 1}

# f(i,g,d) = f(i - 1, g + A[i], d) lub f(i, g, d + A[i])

# polecana implementacja jako rekurencja ze spamiętywaniem
