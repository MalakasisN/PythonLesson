from collections import Counter
import operator
reasons=[]
for death in data:
    if death['importance']>2:
        reasons.append(death['reason'])
f=Counter(reasons)
print(max(f.items(), key=operator.itemgetter(1))[0])