import math

def getC(a,b):
    c = math.sqrt(a**2 + b**2)

    if c == int(c):
        return c
    else: return None

for a in range(1,500):
    for b in range(1,a):
        c = getC(a,b)
        if c!=None:
            sum_list = a + b + c
            mul_list = a*b*c
            if sum_list == 1000:
                print(mul_list)
                
