def f(x):
    l=[]
    i=0
    while True:
        if i in l:
            print(len(l[l.index(i):len(l)]))
            break
        else:
            l.append(i)
            i=x[i]
f([0, 3, 3, 5, 5, 5, 1, 1, 8, 6])
            