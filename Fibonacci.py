import math

def alg(n):
    f = 0
    y = 0
    
    fib_org = []
    fib_add = []

    for i in range(n):

        f = i
        
        if len(fib_org)>1:
            f = fib_org[-2] + fib_org[-1]

        if f%2 == 0:
            fib_add.append(f)
            
        fib_org.append(f)

        if f>4000000:
            break

    print("Original Fibonacci sequence: \n %s \n" % fib_org)
    

    return fib_add

print(sum(alg(100)))

