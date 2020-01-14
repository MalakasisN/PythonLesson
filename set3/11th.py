from collections import Counter
killers=[]
killed=[]
alive=[]
for death in data:
    killers.append(death['killer'])
    killed.append(death['character_killed'])
for killer in killers:
    if not killer in killed and killer not in alive:
        alive.append(killer)
print(len(alive))
#exei lathakia to dataset(Theon Grejoy)
