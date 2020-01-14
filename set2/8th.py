def f(x):
    import scipy.special
    for i in range(x+1):
        if i==0:
           print('a^',x,'+', end='', sep='')
        elif i==x:
            print('b^',x, end='',sep='')
        else:
           print(int(scipy.special.binom(x,i)),'a^',x-i,'b^',i,'+', end='',sep='')
f(10)