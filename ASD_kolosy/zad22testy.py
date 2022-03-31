P1 = [(1,2,10),(2,5,2),(1,5,20)]
odp1 = 12
prz1 = 1,5

P2 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1)]
odp2 = -1
prz2 = 2.8,3

P3 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1)]
odp3 = -1
prz3 = 1,1251

P4 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1),(3,7,2),(7,10,12),(1,10,36)]
odp4 = 34
prz4 = 1,10

P5 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1)]
odp5 = -1
prz5 = 1,4

P = [P1,P2,P3,P4,P5]
odp = [odp1,odp2,odp3,odp4,odp5]
prz = [prz1,prz2,prz3,prz4,prz5]

def runtests(ez):
    git = True
    for i in range(len(P)):
        print(P[i])
        ret = ez(P[i],prz[i])
        print("otrzymany wynik:" + str(ret))
        print("oczekiwany wynik:" + str(odp[i]))
        print("git" if ret == odp[i] else "Błąd mordo zmien cos")
        if ret != odp[i]:
            git = False
        print("-----------------------------------")
    if not git:
        print("wynik:   tiny.cc/pudzian")
    else:
        print("wynik:   tiny.cc/pudzianv2")



