voters=[]
participants=[]
temp=[]
temp2=[]
lines=[]
linesfinal=[]
for i in data:
    if not i['from_country'] in voters:
        voters.append(i['from_country'])
    if not i['to_country'] in participants:
        participants.append(i['to_country'])
voters.sort()
participants.sort()
participants.append([])
for j in participants:
    temp.sort()
    lines.append(temp)
    temp=[]
    for k in voters:
        for i in data:
            if i['from_country']==k and i['to_country']==j:
                if temp==[]:
                    temp.append((j,0))
                    temp.append((k,i['jury_points']+i['televote_points']))
                else:
                    temp.append((k,i['jury_points']+i['televote_points']))
lines.remove(lines[0])
participants.remove([])
for i in lines:
    for (j,k) in i:
        temp2.append(k)
        if i.index((j,k))==len(i)-1:
            linesfinal.append(temp2)
            temp2=[]
voters=['COUNTRY']+voters
for i in range(len(participants)):
    linesfinal[i]=[participants[i]]+linesfinal[i]
with open('17th.txt','w') as f:
    f.write(",".join([str(j) for j in voters]))
    f.write('\n')
    for i in linesfinal:
        f.write(",".join([str(j) for j in i]))
        f.write('\n')