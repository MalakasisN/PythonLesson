def f(x):
    y=str(x)
    l=[]
    c=''
    for i in range(len(y)-1):
        if int(y[i])==int(y[i+1])-1:
            if c=='':
                c+=y[i]+y[i+1]
                l.append(int(c))
            else:
                c+=y[i+1]
                l.append(int(c))
        if int(y[i])!=int(y[i+1])-1:
            c=''
    print(max(l),l)
f(25629456287456291)