def f(x):
    a=''
    for i in range(len(x)-1):
        for j in range(len(min([x[i],x[i+1]]))):
            if x[i][j]==x[i+1][j]:
               a+=x[i][j]
               if a==x[i] or a==x[i+1]:
                   x[i+1]=a
                   a=''
                   break
            if not x[i][j]==x[i+1][j]:
               x[i+1]=a
               a=''
               break
        if x[i]=='':
            x=['','']
    print(x[len(x)-1])
f([
   'Alekos',
   'Aleksandra',
   'Aleksandros',
])
