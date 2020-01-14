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
    if i['importance']>=2:#for importance > 2 more than one graphs are produced
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