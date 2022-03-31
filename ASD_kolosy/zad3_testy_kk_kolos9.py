graph1 = [
   [111, 111, 111],
    [111, 111, 111],
    [111, 111, 111]
]
leng1 = 333
possible_odp1 = [[0, 1, 2]]

graph2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 3, 0, 2, 0, 1],
    [0, 1, 0, 1, 0, 5, 0, 0],
    [0, 3, 1, 0, 2, 15, 0, 0],
    [0, 0, 0, 2, 0, 1, 0, 0],
    [0, 2, 5, 15, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0]]
leng2 = 5
possible_odp2 = [[1, 2, 3]]

graph3 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 2, 0, 1],
    [0, 1, 0, 1, 0, 5, 0, 0],
    [0, 0, 1, 0, 2, 15, 0, 0],
    [0, 0, 0, 2, 0, 1, 0, 0],
    [0, 2, 5, 15, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0]]
leng3 = 7
possible_odp3 = [[1, 2, 3, 4, 5]]

graph4 = [
    [0, 1, 3, 4, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 2],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0]
]
leng4 = None
possible_odp4 = None

graph5 = [
    [0, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 4, 4],
    [0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 21, 0],
    [6, 4, 0, 21, 0, 0],
    [0, 4, 0, 0, 0, 0]]
leng5 = 32
possible_odp5 = [[0, 3, 4]]

graph6 = [
    [0, 0, 1, 5, 6, 16],
    [0, 0, 0, 0, 4, 4],
    [1, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 21, 0],
    [6, 4, 0, 21, 0, 0],
    [16, 4, 0, 0, 0, 0]]
leng6 = 32
possible_odp6 = [[0, 3, 4]]

graph7 = [
    [0, 1, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 0, 0, 0, 0, 0],
    [2, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0]]
leng7 = 5
possible_odp7 = [[4, 5, 6, 7, 8]]

graph8 = [
    [0, 1, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 0, 0, 0, 0, 0],
    [2, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 0, 1],
    [0, 0, 0, 0, 2, 0, 1, 0, 0],
    [0, 0, 0, 0, 2, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0]]
leng8 = 5
possible_odp8 = [[4, 5, 6, 7, 8], [4, 6, 7, 8]]


tests = [(graph1, leng1, possible_odp1), (graph2, leng2, possible_odp2), (graph3, leng3, possible_odp3), (graph4, leng4, possible_odp4), (graph5, leng5, possible_odp5), (graph6, leng6, possible_odp6), (graph7, leng7, possible_odp7), (graph8, leng8, possible_odp8)]

def check_cycle(cycle1: list, cycle2: list):
    n = len(cycle1)
    if len(cycle1) != len(cycle2):
        return False

    try:
        i = cycle2.index(cycle1[0])
    except ValueError:
        return False
    
    if cycle2[i-1] == cycle1[1]:
        cycle2.reverse()
        i = cycle2.index(cycle1[0])

    for j in range(len(cycle1)):
        if cycle1[j] != cycle2[(j+i)%n]:
            return False
    

    return True
    


    
def run_tests(f):
    def run_test(graph, leng, possible_odp):
        ans = f(graph)
        if ans is None:
            return False
        if len(ans) != 2:
            return False

        ans_leng, ans_cycle = ans
        print("Zwrócona długość odpowiedzi:", ans_leng)
        print("Zwróczona odpowiedz:", ans_cycle)
        
        if leng is None and (ans_leng is not None or ans_cycle is not None):
            return False 
        if leng is None and ans_cycle is None and ans_cycle is None:
            return True

        if ans_leng != leng:
            return False
        
        for cycle in possible_odp:
            if check_cycle(cycle, ans_cycle):
                return True
        
        return False
        
    good = 0
    for i, (graph, leng, possible_odp) in enumerate(tests):
        print("---------------------------------")
        print("Test", i)
        if run_test(graph, leng, possible_odp):
            good += 1
            print("Dobrze")
        else:
            print("Poprawna długość odpowiedzi:", leng)
            print("Przykładowe poprawne odpowiedzi:", possible_odp)
            print("Źle")

    
        print("---------------------------------")
    

    if good == len(tests):
        print("Wszystko git")
    else:
        print("BŁĘDY! https://youtu.be/EFwa5Owp0-k")


