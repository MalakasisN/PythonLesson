def f(x):
    import collections
    a=0
    b=0
    l=[(0,0)]
    ll=[]
    for i in x:
        if i=='^':
            b+=1
            l.append((a,b))
        elif i=='>':
            a+=1
            l.append((a,b))
        elif i=='v':
            b-=1
            l.append((a,b))
        elif i=='<':
           a-=1
           l.append((a,b))  
        else:
            print('Bzzzzt error error,self-destruction protocol activated')
            break
    c=collections.Counter(l)
    for i in l:
        if c[i]==1:
            ll.append(i)
    print(len(ll))
f('v>v<vvv<<vv^v<v>vv>v<<<^^^^^<<^<vv>^>v^>^>^>^>^><vvvv<^>^<<^><<<^vvvv>^>^><^v^><^<>^^>^vvv^<vv>>^>^^<>><>^>vvv>>^vv>^<><>^<v^>^>^><vv^vv^>><<^><<v>><>^<^>>vvv>v>>>v<<^<>')