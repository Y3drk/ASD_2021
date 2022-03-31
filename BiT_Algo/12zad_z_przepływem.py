#Zad2 - kafejka internetowa

'''W kafejce internetowej jest K komputerów i A aplikacji na płytach CD.
Na każdym komputerze może być zainstalowana maksymalnie jedna aplikacja.
Każda aplikacja ma listę komputerów na których może działać, a na pozostałych nie może z powodu wymagań sprzętowych.
Jesteś właścicielem kafejki i wiesz, ilu klientów (możliwie zero) będzie chciało jutro skorzystać z danej aplikacji. Zakładamy, że każdy klient zajmuje komputer na cały dzień.
Jaką aplikację powinieneś zainstalować na każdym z komputerów, aby wszyscy klienci mogli skorzystać z tej aplikacji,
którą chcą? Jeżeli takie przyporządkowanie nie istnieje, algorytm powinien to stwierdzić.
'''

#idea - mamy graf dwudzielny, jednym zbiorem wierzchołków sa aplikacje a drugim komputery. Krawedzie maja wage jeden i sa skierowane od aplikacji do komputera
# na ktorym mozemy ja zainstalowac. Ustawiamy superźródło i superujście. Przepustowosci krawedzi z superzrodla do aplikacji ustawiamy na tyle ilu klientów chce skorzystac
# z danej aplikacji a z komputerów do superujscia na 1. Jesli przepływ jest równy ilosci klientów to takie przyporzadkowanie istnieje, wpp nie istnieje.
# wskazac, które aplikacje do których komputerów mozemy zrobic badajac siec residualna


#Zad5 Sabotaż

'''W pewnym kraju trwa wojna domowa. W ramach sabotażu rebelianci chcą uniemożliwić komunikację telegraficzną z miasta A do B.
Otrzymujemy listę miast i linii telegraficznych między nimi. Linie telegraficzne są skierowane. Każda z linii ma przypisany koszt zniszczenia jej.
Chcemy wybrać zbiór połączeń do zniszczenia o łącznym minimalnym koszcie. Interesuje nas nie tylko koszt, ale które konkretnie linie telegraficzne mamy zniszczyć.'''


# idea - wagi w krafie to koszt przeciecia linii. Robimy maksymalny przepływ od A do B i
# z sieci residualnej juz gotowej szukamy krawedzi łaczących S i T w minimalnym przekroju i je własnie zwracamy