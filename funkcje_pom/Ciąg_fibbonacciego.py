def fibbonacci(x):
    k = 0
    x1, x2 = 1, 1
    fib =[0,1]

    while k <= x:
        x_next = x1 + x2
        x1, x2 = x2, x_next
        fib.append(x_next)
        k +=1

    return fib