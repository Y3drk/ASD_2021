
G1 = [[(2, 10), (4, 10000), (5, 213)], [(4, 5), (5, 98), (0, 123455)], [(3, 987), (4, 111)], [], [(5, 1)], [(3, 444)], [(5, 2)], []]
s1 = 1
odp1 = [1,0,1,1,1,1,0,0]


G2 = [[(1, 1)], [(2, 1)], [(3, 1)], [(4, 1)], [(5, 1)], [(6, 1)], [(7, 1)], [(8, 1)], [(9, 1)], [(10, 1)], [(11, 1)], [(0, 1)]]
s2 = 0
odp2 = [0,1,1,1,1,1,1,1,1,1,1,1]

G3 = [[(1, 100), (2, 2), (3, 3), (4, 4), (5, 2)], [(0, 100), (2, 1)], [(0, 2), (1, 1), (3, 2), (5, 4)], [(0, 3), (2, 2), (4, 3)], [(0, 4), (3, 3), (5, 2)], [(0, 2), (4, 2), (2, 4)]]
s3 = 5
odp3 = [1,2,2,2,1,0]

etst= [(G1,s1,odp1),(G2,s2,odp2), (G3,s3,odp3)]

random_wrong = ["https://www.youtube.com/watch?v=Gz0rVvVG4jY  nie jestes tu pudzianem(bad)",
        "https://www.youtube.com/watch?v=UlCCg93okG0  tym gosciem nie jestes(bad)",
        "https://www.youtube.com/watch?v=8AwVRlXsxlA  nawet jakbym wygral, to by nic nie dalo (bad)",
        "https://www.youtube.com/watch?v=lj4EP3i_nkc  tak sie nie robi(bad)",
        "Tak dziala twoj program: https://www.youtube.com/watch?v=80Ms8hoqm6s - nie dziala",
        "https://www.youtube.com/watch?v=giT3DZmy2tk tu nie pojedziesz bo masz zle",
        "https://www.youtube.com/watch?v=blA6y6cvcvY ona by to lepiej zrobila takie realia (źle)",
        "https://www.youtube.com/watch?v=3C-gs1fwJC4  do tego nie trzeba okreslac czy masz zle",
        "https://www.youtube.com/watch?v=2rEcXkJggWs  jakies ciastka czy placki, a ty masz źle",
        "https://www.youtube.com/watch?v=j_59a20ea3A  cos jest nie tak w kodzie",
        "https://www.youtube.com/watch?v=ptr7WSfE1wg  JAAAPIERDDOLEEEE, nie dziala",
        "https://www.youtube.com/watch?v=tKP1pxF7J5Q  tak sie nie robi"]


random_good = [ "https://www.youtube.com/watch?v=UhqaHD1hCJc gites co moge powiedziec",
        "https://www.youtube.com/watch?v=_SrJfyQPQlk  Jak zapomniec tak dobry wynik(dobrze)",
        "https://www.youtube.com/watch?v=TOk0wqcU3hs juz za dzieciaka chcialem czarne lamborghini, z takim programem tez mozesz miec (good), oversexualised teledysk",
        "https://www.youtube.com/watch?v=wGeFVtLo1RA  you know the drill AGH gurom(good)",
        "https://www.youtube.com/watch?v=RPIQNktKfOw     POLONEZZZZZZZ(good)",
        "https://www.youtube.com/watch?v=KOY_05KwJYk bo jestes ty i masz dobrze zrobiony ten test",
        "https://www.youtube.com/watch?v=GXzPgIxlrjg  wszystko gites"
        ]

from random import randint
def runtests(f):
    l = 0
    flag = False
    for G,s,odp in etst:
        print("test nr " + str(l) + " robi brrr")
        oo = f(G,s)
        #print(oo)
        l+=1
        if odp != oo:
            flag = True
            print("zle")
        else:
            print("dobnrze")
    if flag:
        i = randint(0,len(random_wrong))
        print(random_wrong[i])
    else:
        i = randint(0,len(random_good))
        print(random_good[i])



