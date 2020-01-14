from collections import Counter
seasons=[]
for death in data:
    seasons.append(death['season'])
for i in range(1,9):
    if i<7:
        print('Season',i,'deaths per episode:',Counter(seasons)[i]/10)
    if i==7:
        print('Season',i,'deaths per episode:',Counter(seasons)[i]/7)
    if i==8:
        print('Season',i,'deaths per episode:',Counter(seasons)[i]/6)