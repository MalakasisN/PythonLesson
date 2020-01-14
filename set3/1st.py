impdeaths=0
for death in data:
    if death['importance']>1:
        impdeaths+=1
print(impdeaths)