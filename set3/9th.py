from collections import Counter
temp1=[]
temp2=[]
temp3=[]
for death in data:
        temp1.append((death['character_killed'],death['killer']))
        temp2.append((death['killer'],death['character_killed']))
for i in temp1:
    if i in temp2:
        temp3.append(i)
dblkill=list(Counter(temp3))
##ama thelw non-mirrored stoixia##
#for i in dblkill:
#    for j in dblkill:
#        if i!=j and i[0]==j[1] and j[0]==i[1]:
#            dblkill.remove(i)
print(len(dblkill))