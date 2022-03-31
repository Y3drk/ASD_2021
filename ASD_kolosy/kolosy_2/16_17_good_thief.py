def good_thief(T):
    n = len(T)
    steal_things = [-1 for _ in range(n)]
    to_steal = [[-1,False] for _ in range(n)]

    steal_things[0] = T[0]
    to_steal[0][1] = True

    if T[1] > T[0]:
        steal_things[1] = T[1]
        to_steal[1][1] = True
    else:
        steal_things[1] = T[0]
        to_steal[1][0] = 0
        to_steal[1][1] = False

    for i in range(2,n):
        if steal_things[i - 1] < steal_things[i - 2] + T[i]:
            steal_things[i] = steal_things[i - 2] + T[i]
            to_steal[i][0] = i - 2
            to_steal[i][1] = True
        else:
            steal_things[i] = steal_things[i - 1]
            to_steal[i][0] = i - 1

    return steal_things[n-1], to_steal


def print_solution(P,ind):
    if ind != -1:
        print_solution(P,P[ind][0])

    if P[ind][1] == True and ind != -1:
        print(ind,end=', ')


test = [4,11,5,2,10]
res = good_thief(test)
print(res[0],res[1])
print_solution(res[1],len(test) -1)
print("----")

T1 = [10,2,2,10] #20
res1 = good_thief(T1)
print(res1[0],res1[1])
print_solution(res1[1],len(T1) -1)
print("----")
T2 = [2,10,1,1,1,100] #111
res2 = good_thief(T2)
print(res2[0],res2[1])
print_solution(res2[1],len(T2) -1)
print("----")
T3 = [2,39,1,1,50,1] #89
res3 = good_thief(T3)
print(res3[0],res3[1])
print_solution(res3[1],len(T3) -1)
print("----")
