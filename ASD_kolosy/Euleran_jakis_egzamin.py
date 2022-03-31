'''masz graf zadany lista krawedzi, w której moga byc powtórki, sprawdz czy w grafie istnieje cykl eulera'''

def Euleran(T):
    n = len(T)
    T.sort() #nlogn

    max_vert = 0
    for i in range(n):
        max_vert = max(max_vert, T[i][1])

    print(T)
    deg = [0 for _ in range(max_vert +1)]
    last = (None, None)
    for i in range(n):
        if T[i][0] != last[0] or T[i][1] != last[1]:
            deg[T[i][0]] += 1
            deg[T[i][1]] += 1
            last = (T[i][0], T[i][1])

    print(deg)
    for vert in deg:
        if vert % 2 == 1:
            return False

    return True


T0 = [(1,5),(0,6),(2,6),(0,7),(4,5),(3,4),(3,7),(0,6),(1,2),(5,6),(0,1),(1,5),(6,7),(3,7),(3,5),(2,3),(0,6),(4,5),(3,4),(2,5),(1,7)]
print(Euleran(T0))
print("-----")
T1 = [(0,1),(2,3),(0,1),(1,2),(0,3),(1,2),(2,3),(2,3),(0,3),(0,1)]
print(Euleran(T1))
print("-----")

