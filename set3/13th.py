l=[(abs(i['jury_points']-i['televote_points']),i['from_country'],i['to_country'])for i in data]
l.sort(reverse=True)
for j in l[0:10]:
    print('The difference between the points given by the voters and the jury(scandal meter) from',j[1],'to',j[2],'is',j[0])


#temp=[]
#disagreementscores=[]
#for i in range(len(data)-1):
#    if data[i]['from_country']==data[i+1]['from_country']:
#        temp.append(abs(data[i]['jury_points']-data[i]['televote_points']))        
#        if i==(len(data)-2):
#            temp.append(abs(data[i+1]['jury_points']-data[i+1]['televote_points']))
#            disagreementscores.append((sum(temp),data[i]['from_country']))
#    else:
#        temp.append(abs(data[i]['jury_points']-data[i]['televote_points']))
#        disagreementscores.append((sum(temp),data[i]['from_country']))
#        temp=[]
#disagreementscores.sort()
#top10=disagreementscores[len(disagreementscores)-10:]
#for j in top10:
#    print('Rank',abs(top10.index(j)-10),':The difference in points given by the jury and the viewers is', j[0],'for the country', j[1])       