#Problem maksymalnego przepływu z wieloma źródłami i ujsciami można sprowadzić do do zwykłego problemu maksymalnego przepływu,
# odpowiednio przekształcając zadaną sieć, poprzez dodanie superźródła i superujścia, czyli dodatkowych wierzchołków. Pierwszy z nich jest połaczony z wszystkimi
# zwykłymi źródłami, a drugi ze wszystkimi zwykłymi ujsciami. Kazda powstała w ten sposób krawędż ma przepustowość +infinity, krawedzie sa skierowane od superzrodła do
# zrodeł i od ujsc do superujscia. Tak powstały problem jest równoważny z ww. zadaniem

#Cormen str. 727

# zad1 _ fabryki i sklepy:
# idea jak powyzej, jedynie w kraedziach do super ujscia jako przepustowosci wpisujemy wartosci podanych sklepów
