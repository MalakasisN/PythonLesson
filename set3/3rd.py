from  collections import Counter
seasonkill=[]
for death in data:
    if death['importance']>1 and death['killer']=='Jon Snow':
        seasonkill.append(death['season'])
x=Counter(seasonkill)
y = dict((v,k) for k,v in x.items())
print(y[max(y)])