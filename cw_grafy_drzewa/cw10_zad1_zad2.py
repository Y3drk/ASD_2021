# zad3 to wymiana walut z bitu, wiec implementacja jest tam,
# zad1 i zad2 sa koncepcyjne bo opieraja sie na formułach logicznych i byłby to straszny gruz do implementowania, wiec opisze je tu koncepcyjnie

'''Zadanie 1. (SAT-2CNF) Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest
koniunkcją klauzuli, gdzie każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej
negacja. Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest:
(x ∨ y) ∧ (x ∨ z) ∧ (z ∨ y).
Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie spełniające
formułę.'''

#kazda alternatywe przerabiamy na implikacje i wg tego tworzymy krawedź, nastepnie z krawędzi tworzymy graf skierowany.]
# jesli nie istnieje silnie spójna składowa zawierająca literały komplementarne to formuła jest spełnialna



'''Zadanie 2. (wyścigi) Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi
mają się odbywać po trasach zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji.
Król chce, żeby każde miasto było zaangażowane w dokładnie jeden wyścig. W tym celu należy sprawdzić,
czy da się wynająć odpowiednie odcinki autostad. Należy jednak pamiętać o następujących ograniczeniach:
1. w Bitocji wszystkie autostrady są jednokierunkowe,
2. z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
miast,
3. do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
miast,
Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.
'''

#de facto problem pokrycia cyklami prostymi, tylko uproszczony przez zał. 2 i 3
# z kazdego wierzchołka tylko jedna krawedz wychodzaca i wchodzaca maja byc uzyte, a może byc ich max 2
# zatem dla kazdego wierzchołka mozemy zapisac cztery formuły (aleternatywy) po dwie do krawedzi wchodzacych i dwie do wychodzacych
# tak aby kazda odpiwednio warunkowała stan, który jak wczesniej ustalilismy, musi zachodzić.
# i zebrac je w formułe CNF, a następnie rozwiązac tak jak zadanie pierwsze.