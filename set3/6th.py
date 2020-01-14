from collections import Counter
killers=[]
for death in data:
    if death['importance']>1:
        killers.append(death['killer'])
x=Counter(killers)
y = dict((v,k) for k,v in x.items())
y.pop(max(y))
print(y[max(y)])