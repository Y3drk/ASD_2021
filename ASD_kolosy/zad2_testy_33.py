from zad2_33 import Cyclist

G1 = [(12422,9867),(9867,-1),(888,12422),(98456757,44),(44,1),(99,6),(1,99),(6,-1)]
odp1 = 3

G2 = [(12422,9867),(9867,8),(888,12422),(98456757,44),(44,1),(99,6),(1,99),(6,-1),(8,-1)]
odp2 = 4

G3 = [(12422,9867),(9867,8),(888,12422),(98456757,44),(44,1),(99,6),(1,99),(6,-1),(8,-1),(4444688985,-1)]
odp3 = 1

G4 = []
odp4 = 0

List = [(G1,odp1),(G2,odp2),(G3,odp3),(G4,odp4)]


from random import randint
def runtests(f):
    l = 0
    flag = False
    for cyc, wynik in List:
        print("test nr " + str(l) + " robi brrr")
        no = []
        n = len(cyc)
        l+=1
        for id,n_id in cyc:
            no.append(Cyclist(id,n_id))
        res = f(no,n)
        if res != wynik:
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
