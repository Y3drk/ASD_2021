def zamiana_systemow(a,b):
    pom = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    pom2 = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  "A",  "B",  "C",  "D", "E", "F"]
    index = -1
    tab = []
    n = 0
    while b** n <= a:
        tab += [0]
        n += 1

    while a != 0:
        tab[index] = pom2[a % b]
        a //= b
        index -= 1

    return tab

print(zamiana_systemow(88,2))


