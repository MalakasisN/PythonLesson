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