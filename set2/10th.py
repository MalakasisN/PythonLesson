def f(x):
    l=[]
    c=0
    for i in range(len(x)):
        c+=x[i]
        l.append(c)
    for i in range(len(l)):
        if l[i]==max(l):
            print(i)
f([31, -28, 14, -12, -4, 44, 47, 2, -48, -5, -43, 32, 0, -4, 24, -46, -12, 38, -38, -27, -23, -26, 10, 42, 26, -20, -43, -50, 
2, 42, 32, 17, -33, 5, 42, 28, 2, 12, 9, -33, 22, 10, 3, 34, 12, 17, 21, 17, 24, 22, 21, -35, 33, 12, -43, 49, -17, 3, -2, 
-25, -29, -35, -26, -25, -22, -33, 10, 26, -41, 29, 6, -10, 15, -28, -23, -35, -1, -16, 24, -45, -50, -17, 20, 12, -32, 48, 
-48, 2, -41, 4, 5, 29, -36, -46, -6, -17, -18, 16, 42, 42])