temp=[]
totalranking=[]
viewersranking=[]
c=0
d=0
for i in data:
    temp.append((i['to_country'],i['televote_points'],i['jury_points']))
temp=sorted(temp)
for j in range(len(temp)-1):
    if temp[j][0]==temp[j+1][0]:
        c+=temp[j][1]
        d+=temp[j][2]
        if j==len(temp)-2:
            c+=temp[j+1][1]
            d+=temp[j+1][2]
            viewersranking.append((c,temp[j+1][0]))
            totalranking.append((c+d,temp[j+1][0]))
    else:
        c+=temp[j][1]
        d+=temp[j][2]
        viewersranking.append((c,temp[j][0]))
        totalranking.append((c+d,temp[j][0]))
        c=0
        d=0
viewersranking.sort(reverse=True)
totalranking.sort(reverse=True)
unfairrank=[((totalranking.index(j)-viewersranking.index(i)),i[1])for i in viewersranking for j in totalranking if i[1]==j[1]]
print('The country that got scammed the most by the jury was',max(unfairrank)[1],',which was',max(unfairrank)[0],'ranks higher in the viewers voting ranking compared to the final ranking!')