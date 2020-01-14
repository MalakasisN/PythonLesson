def f(x):
    import collections
    a=0
    b=0
    l=[(0,0)]
    la=[0]
    lb=[0]
    for i in x:
        if i=='^':
            b+=1
            l.append((a,b))
            lb.append(b)
        elif i=='>':
            a+=1
            l.append((a,b))
            la.append(a)
        elif i=='v':
            b-=1
            l.append((a,b))
            lb.append(b)
        elif i=='<':
           a-=1
           l.append((a,b))  
           la.append(a)
        else:
            print('Bzzzzt error error,self-destruction protocol activated')
            break
    visitedspots=len(list(collections.Counter(l)))
    totalspots=(max(la)-min(la)+1)*(max(lb)-min(lb)+1)
    unvisitedspots=totalspots-visitedspots
    print(collections.Counter(l),max(la),min(la),max(lb),min(lb),unvisitedspots)
f('v>v<vvv<<vv^v<v>vv>v<<<^^^^^<<^<vv>^>v^>^>^>^>^><vvvv<^>^<<^><<<^vvvv>^>^><^v^><^<>^^>^vvv^<vv>>^>^^<>><>^>vvv>>^vv>^<><>^<v^>^>^><vv^vv^>><<^><<v>><>^<^>>vvv>v>>>v<<^<>')