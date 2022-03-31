def nadgorliwy_mag(G) -> list:
    # tu zaimplementuj funkcję :))
    pass


G_1 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

G_2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0]]

G_3 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]






# niżej proszę nie patrzeć :))




odp_1 = 3
odp_2 = 2
odp_3 = 4






































































































def valid_cycle(G, cycle):
    if len(cycle) == 1:
        return True
    i, j = 0, 1
    n = len(cycle)
    while j < n:
        if G[cycle[i]][cycle[j]] == 0:
            return False
        i += 1
        j += 1
    return True


def check_solution(G, solution, correct):
    if solution == None:
        return 2
    n = len(solution)
    i = 0
    counter = 0
    while i < n:
        first = solution[i]
        cycle = [first]
        temp = i
        i += 1
        while i < n and solution[i] != first:
            cycle.append(solution[i])
            i += 1
        if i == n and temp != n-1:
            return 2
        if not valid_cycle(G, cycle):
            return 3
        if i == n - 1:
            return True
        if i < n and G[first][solution[i + 1]] == 0:
            return 4
        i += 1
        counter += 1
    if counter != correct:
        return 5
    return True


if __name__ == "__main__":
    test = [(G_1, odp_1), (G_2, odp_2), (G_3, odp_3)]
    problem = False
    for i in range(len(test)):
        result = check_solution(test[i][0], nadgorliwy_mag(test[i][0]), test[i][1])
        if result == 2:
            print("Test", i + 1, ": nieprawidłowa odpowiedź.")
            problem = True
        elif result == 3:
            print("Test", i + 1, ": prawdopodobnie błędne przypisanie wież do jednego rytuału.")
            problem = True
        elif result == 4:
            print("Test", i + 1, ": próba przejścia pomiędzy wieżami nieistniejącym teleportem.")
            problem = True
        elif result == 5:
            print("Test", i + 1, ": niewłaściwa liczba rytuałów.")
            problem = True
        else:
            print("Test", i + 1, "ok.")
    if not problem:
        print("Wszystko ok <3")
