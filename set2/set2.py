#1
import math
sum([math.sqrt(i) for i in range(3000) if (i%3==0 and i%2!=0)])

#2
sum([k-l for k in range(2,1001) for l in range(2,1001) if k%l==0 and k!=l])

#3
def f():
    return lambda:lambda:['Kostas',lambda:'Μήτσος','Maria']
        

f()()()[1]()

#4
def f():
    return [lambda x:x+1,lambda x:x+2,lambda x:x+3,lambda x:x+4,lambda x:x+5,lambda x:x+6,lambda x:x+7,lambda x:x+8,lambda x:x+9,lambda x:x+10]

f()[9](10)

#5
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

#6
def f(x,y):
    z=''
    y=list(y)
    k=0
    for i in range(len(x)):
        if x[i]=='+':
            z+=' '
        elif x[i]=='-':
            z+=y[0]
            y.remove(y[0])
            if y==[]:
                y=[' ']
        else:
            k+=1   
    if k==0:    
        print(z)
    else:
        print('error')
        
f('++-+--+-+++++++++++++-+-+++++-++--++-++++-+---++-++-+--++---++-+-++-------+-+++---+---++-+-+++-+-+++','ZABARAKATRANEMIA')
#7
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

#8
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
#9
def compress(x):
    c = 1
    s=''
    for i in range(1,len(x)+1):
        if i==len(x):
            s+=x[i-1]+str(c)
            break
        else:
            if x[i-1] == x[i]:
                c+= 1
            else:
                s+=x[i-1]+str(c)
                c=1
    print(s)
compress('aahtoootoootttuuuu-----------o')

def decompress(y):
    s=''
    nums='1234567890'
    c=''
    for i in range(0,len(y)+1):
        if i==len(y)-1:
            c+=y[i]
            s+=int(c)*y[i-len(c)]
            break
        if not y[i] in nums:
            if c=='':
                continue
            else:
                s+=int(c)*y[i-len(c)-1]
                c=''
        if y[i] in nums:
            c+=y[i]
    print(s)
decompress('a2h1t1o3t1o3t3u4-11o1')
#10
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

#11
def f(x):
    l=[]
    c=0
    for i in range(len(x)):
        c+=x[i]
        l.append(c)
    ll=[(l[i]-l[j],j,i) for i in range(len(l)) for j in range(len(l)) if i>j]
    print((max(ll)[1],max(ll)[2]))#oxi (28,56),einai lathos,pame mia thesi pisw
        
f([31, -28, 14, -12, -4, 44, 47, 2, -48, -5, -43, 32, 0, -4, 24, -46, -12, 38, -38, -27, -23, -26, 10, 42, 26, -20, -43, -50, 
2, 42, 32, 17, -33, 5, 42, 28, 2, 12, 9, -33, 22, 10, 3, 34, 12, 17, 21, 17, 24, 22, 21, -35, 33, 12, -43, 49, -17, 3, -2, 
-25, -29, -35, -26, -25, -22, -33, 10, 26, -41, 29, 6, -10, 15, -28, -23, -35, -1, -16, 24, -45, -50, -17, 20, 12, -32, 48, 
-48, 2, -41, 4, 5, 29, -36, -46, -6, -17, -18, 16, 42, 42])
#12
import itertools
combo=[]
butters=[82, 88, 88, 71, 79, 74]
eggs=[73, 91, 82, 98, 95, 90, 70, 73]
milks=[97, 90, 89, 81, 99]
for i in range(len(butters)):
    for j in range(len(eggs)):
        for k in range(len(milks)):
            combo+=itertools.combinations((butters[i],eggs[j],milks[k]),3) 
cost=list(map(sum,combo))
median=(sum(cost)/len(cost))
print(median)
#13->exei lathos i ekfwnisi!!
def f(x):
    import collections
    l=[]
    l2=[]
    l3=[]
    for i in x:
        l+=range(i[0],i[1]+1)
    c=collections.Counter(l)
    c2=list((v,k) for k,v in c.items())
    for j in c2:
        l2.append(j[0])
    for j in c2:
        if j[0]==max(l2):
            l3.append(j[1])
    print(l3)
f([(22, 34), (66, 75), (35, 46), (45, 59), (77, 87), (38, 58), (51, 58), (81, 90), (52, 70), (53, 65), 
(53, 72), (50, 63), (80, 100), (0, 12), (68, 81), (35, 51), (27, 34), (69, 87), (39, 47), (0, 8)])

#14
def f(x):
   c=''
   from collections import Counter
   for i in range(len(x)-1):
       a=(Counter(x[i])&Counter(x[i+1]))
       b=list(a)
       d=c.join(b)
       x[i+1]=d
   if b==[]:
       print('No common characters found')
   else:    
       print('Common characters are:',b)
       
f(['επιστρέφει',
    'παίρνει',
    'υπάρχουν ',
    'που'])
#15
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
    print(max(l))
f(25629456287456291)
#16
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
f([5, 0, 6, 6, 9, 3, 4, 0, 4, 3])
            
#17
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
#18
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
    print(unvisitedspots)
f('v>v<vvv<<vv^v<v>vv>v<<<^^^^^<<^<vv>^>v^>^>^>^>^><vvvv<^>^<<^><<<^vvvv>^>^><^v^><^<>^^>^vvv^<vv>>^>^^<>><>^>vvv>>^vv>^<><>^<v^>^>^><vv^vv^>><<^><<v>><>^<^>>vvv>v>>>v<<^<>')
#19
import math
def euc(a,b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def mes(a,b):
	# This function returns 2 numbers! 
	return (a[0]+b[0])/2, (a[1]+b[1])/2
def f(x):
    y=list(x)
    while True:
        dis=[(euc(i,j),i,j) for i in x for j in x if i!=j]
        x.remove(min(dis)[1])
        x.remove(min(dis)[2])
        x.append(mes(min(dis)[1],min(dis)[2]))
        if len(x)==1:
            l=[(euc(x[0],i),y.index(i)) for i in y]
            print(min(l)[1])
            break
    
f([(44, 29),
 (31, 1),
 (-14, 79),
 (98, -78),
 (-2, 34),
 (-80, -27),
 (98, -21),
 (25, -23),
 (33, 45),
 (-85, -40),
 (53, 81),
 (50, -53),
 (42, 56),
 (-30, 100),
 (74, 20),
 (-78, -80),
 (-39, 42),
 (87, 19),
 (15, 98),
 (85, -27)])
#20
routes=[]
def find_paths(curr,prev,cities,path,x,distance):
    path.append(curr)
    if len(path)>1:
        if curr<prev:
            distance+=x[curr][prev]
        else:
            distance+=x[prev][curr]
    if len(cities)==len(path):
        global routes
        routes.append([distance,path+[0]])
        return
    for city in cities:
        if city not in path:
            find_paths(city,curr,cities,list(path),x,distance)

def f(x):
    cities=list(range(len(x)+1))
    for i in range(len(x)):
        x[i]=['mitsos']*(i+1)+x[i]
    find_paths(0,0,cities,[],x,0)
    print('\n') 
    if len(routes)!=0:
        print(min(routes)[1])
    else:
        print('Error')
f([[673, 517, 674, 834, 991, 458, 558, 538, 990],
 [758, 469, 850, 940, 889, 937, 978, 703],
 [925, 838, 595, 880, 767, 685, 659],
 [589, 455, 858, 808, 748, 837],
 [586, 994, 875, 779, 945],
 [979, 685, 661, 817],
 [498, 814, 940],
 [597, 687],
 [844]])
    