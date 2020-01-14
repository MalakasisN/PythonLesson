def f(x):
    c=1
    l=[]
    l2=[]
    l3=[]
    k=0
    for i in range(len(x)-2):
        if x[i]=='+':
            if x[i]==x[i+1]:
                c+=1
                if x[i+1]!=x[i+2]:
                    l.append((c,i-c+2))
                    c=1
            elif x[i]!=x[i+1] and x[i]!=x[i-1]:
                l.append((c,i-c+2))
            if i+3==len(x):
                l.append((c+1,i-c+2))
        if x[i]!='+' and x[i]!='-':
            k+=1
    for j in l:
        l2.append(j[0])
    for j in l:
        if j[0]==max(l2):
            l3.append(j[1])
    if k==0:
        print(min(l3))
    else:
        print('error')
        
    
                
f('+-+-++--+----+-+---+-+-+---+----+-++-+-+--++++-++++-+++--++++--+----+----+-+++--+-++-+---++-+-------')
