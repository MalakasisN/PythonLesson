import math

def is_prime(N):
    for k in range(2, int(math.sqrt(N))+1):
        if not N%k:
            return False
    return True

def compositegen():
    c=1
    while True:
        if not is_prime(c):
            yield c
        c+=1
g=compositegen()

def running_total():
    i=0
    while True:
        i+=next(g)
        yield i
        
gen = running_total()
for i in range(10):
    print (next(gen))