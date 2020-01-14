temp=[]
l=[]
ll=[]
for i in data:
    temp.append((i['to_country'],i['televote_points']+i['jury_points'],i['from_country']))
temp.sort(reverse=True)
for j in range(len(temp)-1):
        if temp[j][0]==temp[j+1][0]:
            l.append(temp[j][2])
            if j==len(temp)-2:
                l.append(temp[j+1][2])
                ll.append((temp[j+1][0],l))
        else:
            l.append(temp[j][2])
            ll.append((temp[j][0],l))
            l=[]
pointsranking=dict(ll)
print (pointsranking['Australia'])