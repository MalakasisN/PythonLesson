kills=0
for death in data:
    if death['importance']>1 and death['killer']=='Arya Stark':
        kills+=1
print(kills)