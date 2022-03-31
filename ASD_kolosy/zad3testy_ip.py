from zadania_impatient_bobby_18_19_1_6 import Job

P1 = [Job(1,2),Job(1,6),Job(4,10),Job(9,12)]
odp1 = 2
k1 = 2

P2 = [Job(0,2),Job(0,7),Job(2,10),Job(9,13),Job(11,13),Job(15,17),Job(18,20),Job(21,25)]
odp2 = 1
k2 = 3

P3 = [Job(1,5),Job(2,6)]
odp3 = -1
k3 = 12

P = [(P1,odp1,k1),(P2,odp2,k2),(P3,odp3,k3)]


def runtests(ez):
    git = True
    for Pi,odp,k in P:
        for elem in Pi:
            print(str(elem),end = " ")
        print()
        ret = ez(Pi,len(Pi),k)
        print("otrzymany wynik:" + str(ret))
        print("oczekiwany wynik:" + str(odp))
        print("git" if ret == odp else "Błąd mordo zmien cos")
        if ret != odp:
            git = False
        print("-----------------------------------")
    if not git:
        print("wynik:   tiny.cc/pudzian")
    else:
        print("wynik:   tiny.cc/pudzianv2")
