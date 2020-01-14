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
#exei lathos i ekfwnisi!!