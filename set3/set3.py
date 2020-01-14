#gameofthrones
import csv

order_index = 0
season_index = 1
episode_index = 2
character_killed_index = 3
killer_index = 4
method_index = 5
method_cat_index = 6
reason_index = 7
location_index = 8
allegiance_index = 9
importance_index = 10

data = []
with open('game-of-thrones-deaths-data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    header = f.readline().strip().split(',')
    for ls in reader:
        d = {
            'order': int(ls[order_index]),
            'season': int(ls[season_index]),
            'episode': int(ls[episode_index]),
            'character_killed': ls[character_killed_index],
            'killer': ls[killer_index],
            'method': ls[method_index],
            'method_cat': ls[method_cat_index],
            'reason': ls[reason_index],
            'location': ls[location_index],
            'allegiance': ls[allegiance_index],
            'importance': int(ls[importance_index]) if ls[importance_index] else 1,
        }
        data.append(d)
#1
impdeaths=0
for death in data:
    if death['importance']>1:
        impdeaths+=1
print(impdeaths)
#2
kills=0
for death in data:
    if death['importance']>1 and death['killer']=='Arya Stark':
        kills+=1
print(kills)
#3
from  collections import Counter
seasonkill=[]
for death in data:
    if death['importance']>1 and death['killer']=='Jon Snow':
        seasonkill.append(death['season'])
x=Counter(seasonkill)
y = dict((v,k) for k,v in x.items())
print(y[max(y)])
#4
categories=[]
for death in data:
    if not death['method_cat'] in categories:
        categories.append(death['method_cat'])
print(len(categories))
#5
from collections import Counter
import operator
categories=[]
temp=[]
allegpercat=[]
for death in data:
    if not death['method_cat'] in categories:
        categories.append(death['method_cat'])
for category in categories:    
    for death in data:
        if category==death['method_cat'] and death['importance']>1:
            temp.append((category,death['allegiance']))
    if temp==[]:
        temp.append((category,'None important death in this category'))
    allegpercat.append(temp)
    temp=[]

for category in allegpercat:
    f=Counter(category)
    print(max(f.items(), key=operator.itemgetter(1))[0])
#6
from collections import Counter
killers=[]
for death in data:
    if death['importance']>1:
        killers.append(death['killer'])
x=Counter(killers)
y = dict((v,k) for k,v in x.items())
y.pop(max(y))
print(y[max(y)])
#7
from collections import Counter
import operator
reasons=[]
for death in data:
    if death['importance']>2:
        reasons.append(death['reason'])
f=Counter(reasons)
print(max(f.items(), key=operator.itemgetter(1))[0])
#8
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
#9
from collections import Counter
temp1=[]
temp2=[]
temp3=[]
for death in data:
        temp1.append((death['character_killed'],death['killer']))
        temp2.append((death['killer'],death['character_killed']))
for i in temp1:
    if i in temp2:
        temp3.append(i)
dblkill=list(Counter(temp3))
print(len(dblkill))
#10
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
#11
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
#12
from collections import defaultdict
l=[]
all_paths=[]
def DFS(G,v,seen=None,path=None):
    if seen is None:
        seen = []
    if path is None:
        path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths

for i in data:
    if i['importance']>=2:#for importance > 2 more than one chains are produced
        l.append([i['character_killed'],i['killer']])
G = defaultdict(list)
for (s,t) in l:
    G[s].append(t)

for j in l:
    all_paths+=(DFS(G,j[0]))
max_len= max(len(p) for p in all_paths)
max_paths = [p for p in all_paths if len(p) == max_len]
print('The longest chain(s) of killing incidents in Game of Thrones is',max_len-1,'kills long.')
print('Analytically:')
for k in range(len(max_paths[0])-1):
    print(max_paths[0][k],'was killed by',max_paths[0][k+1])
#eurovision
import pandas as pd

df = pd.read_excel('ESC-2016-grand_final-full_results.xls') # Αγνοήστε τα warnings..

data = []

for k,v in df.to_dict('index').items():
    if k==0:
        continue
    
    d = {
        'from_country': v['Eurovision Song Contest 2016 Grand Final'],
        'to_country': v['Unnamed: 1'],
        'jury_points': 0 if v['Unnamed: 9']=='\n' else int(v['Unnamed: 9']),
        'televote_points': 0 if v['Unnamed: 10']=='\n' else int(v['Unnamed: 10']),
    }
    
    data.append(d)
#13
l=[(abs(i['jury_points']-i['televote_points']),i['from_country'],i['to_country'])for i in data]
l.sort(reverse=True)
for j in l[0:10]:
    print('The difference between the points given by the voters and the jury(scandal meter) from',j[1],'to',j[2],'is',j[0])

#14
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
#15
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
#16
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
#17
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
#18
import math

def is_prime(N):
    for k in range(2, int(math.sqrt(N))+1):
        if not N%k:
            return False
    return True

def compositegen():
    c=1
    while True:
        if not is_prime(c):
            yield c
        c+=1

gen=compositegen()
for i in range(10):
    print(next(gen))
#19
import math

def is_prime(N):
    for k in range(2, int(math.sqrt(N))+1):
        if not N%k:
            return False
    return True

def compositegen():
    c=1
    while True:
        if not is_prime(c):
            yield c
        c+=1
g=compositegen()

def running_total():
    i=0
    while True:
        i+=next(g)
        yield i
        
gen = running_total()
for i in range(10):
    print (next(gen))
#20
def sieve(n): 
    nNew =int((n-2)/2) 
    primes=[] 
    marked=[0]*(nNew+1)
    for i in range(1,nNew+1): 
        j=i; 
        while((i+j+2*i*j)<=nNew): 
            marked[i+j+2*i*j] = 1 
            j += 1; 
    if (n>2): 
        primes.append(2)
   
    for i in range(1,nNew + 1): 
        if (marked[i]==0): 
            primes.append(2*i+1)
    return primes
            
primes=sieve(1000000)

seqlength=0
largestsolution=0
primeslen=len(primes)
for i in range(len(primes)):
    for j in range(i+seqlength,primeslen):
        solution = sum(primes[i:j])
        if solution < 1000000:
            if solution in primes:
                consecutiveprimelist=primes[i:j]
                seqlength=len(consecutiveprimelist)
                largestsolution=solution
        else:
            primeslen=j+1
            break
    
print('The prime number',largestsolution,'can be written as the sum of',seqlength,'consecutive primes.','\n','Analytically,the list of the consecutive primes mentioned above is:',consecutiveprimelist)
