def pijany_mag(T):
    # tu umieść swoją implementację
    I = [ 0 for _ in range(26)]

    for i in range(len(T)):
        for j in range(len(T[i])):
            I[ord(T[i][j]) - 97] += 1

    flag, DAG = make_dag(T)
    if not flag:
        #print("dupa")
        return ""

    else:
        #print(DAG)
        #print("wbitka")
        tmp = topologic_sort_DFS(DAG)
        #print(tmp)
        res = "!"
        for i in range(len(tmp)):
            if I[tmp[i]] != 0:
                res += chr(97 + tmp[i])

        #print(res)
        return res[1:]


def make_dag(T):
    DAG = [[] for _ in range(26)]
    n = len(T)
    max_len = 0

    for i in range(n):
        max_len = max(max_len, len(T[i]))

    #print(max_len)
    for j in range(max_len):
        for i in range(n):
            if len(T[i]) > j:
                last = T[i][j]
                for l in range(i+1, n):
                    if len(T[l]) > j:
                        if T[i][j] == T[l][j] == last:
                            pass
                            #print(T[i][j], T[l][j], j, T[i], T[l], "te same")

                        elif T[i][j] == T[l][j] and last != T[l][j] and T[i][:j] == T[l][:j]:
                            #print(T[i][j], T[l][j],j,T[i],T[l]," chuj")
                            return False,None

                        elif T[i][j] != T[l][j]:
                            last = T[l][j]
                            #print(T[i][j], T[l][j], j, T[i], T[l], "dodano",ord(T[i][j]) - 97 , "->",ord(T[l][j]) - 97)
                            DAG[ord(T[i][j]) - 97].append(ord(T[l][j]) - 97)

    return True, DAG


def topologic_sort_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    list_of_tasks = []

    def DFS_visit(G,s):
        nonlocal list_of_tasks
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        list_of_tasks += [s]  #[chr(97+s)]
        return

    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return list_of_tasks[::-1]

#przechodzac po literach robimy daga, który sortujemy topologicznie

# zł. O(ln^2t) gdzie l = długosc alfabetu, n = ilosc słow, t = długosc najdłuzszego słowa ~O(n^2*t)


T1= ["wrt","wrf","er","ett","rftt"]
odp1 = 'wertf'

T2 = ['z','x']
odp2 = 'zx'

T3 = ['z','x','z']
odp3 = ''

tests = [(T1,odp1),(T2,odp2),(T3,odp3)]
for ind,(t,odp) in enumerate(tests):
    print('---------')
    print("test nr",ind)
    print("odpowiedz:",odp)
    a = pijany_mag(t)
    if a != odp:
        print(f"twoja odpowiedz: \"%s\"" % a)
        print("Błd w tescie")
    else:
        print("OK")



