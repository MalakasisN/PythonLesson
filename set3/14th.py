temp=[]
differencescore=[]
c=0
for i in data:
    temp.append((i['to_country'],i['televote_points']-i['jury_points']))
temp=sorted(temp)
for j in range(len(temp)-1):
    if temp[j][0]==temp[j+1][0]:
        c+=temp[j][1]
        if j==len(temp)-2:
            c+=temp[j+1][1]
            differencescore.append((c,temp[j+1][0]))
    else:
        c+=temp[j][1]
        differencescore.append((c,temp[j][0]))
        c=0
print('The greatest difference between viewer vote scores and jury vote scores for a certain country was:',max(differencescore)[0],'\n','This country was',max(differencescore)[1])