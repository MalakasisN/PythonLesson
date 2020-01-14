from collections import Counter
import operator
categories=[]
temp=[]
allegpercat=[]
for death in data:
    if not death['method_cat'] in categories:
        categories.append(death['method_cat'])
for category in categories:    
    for death in data:
        if category==death['method_cat'] and death['importance']>1:
            temp.append((category,death['allegiance']))
    if temp==[]:
        temp.append((category,'None important death in this category'))
    allegpercat.append(temp)
    temp=[]

for category in allegpercat:
    f=Counter(category)
    print(max(f.items(), key=operator.itemgetter(1))[0])
