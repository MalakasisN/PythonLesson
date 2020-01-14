from collections import Counter
totalepisodes=[]
temp=[]
deathlessepisodes=[]
for death in data:
        temp.append((death['season'],death['episode']))
episodeswithdeaths=list(Counter(temp))
for season in range(1,7):
    for episode in range(1,11):
        totalepisodes.append((season,episode))
for episode in range(1,8):
    totalepisodes.append((7,episode))
for episode in range(1,7):
    totalepisodes.append((8,episode))
for episode in totalepisodes:
    if not episode in episodeswithdeaths:
        deathlessepisodes.append(episode)
for episode in deathlessepisodes:
    print('Season:',episode[0],'Episode:',episode[1])
