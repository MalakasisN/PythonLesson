routes=[]
def find_paths(curr,prev,cities,path,x,distance):
    path.append(curr)
    if len(path)>1:
        if curr<prev:
            distance+=x[curr][prev]
        else:
            distance+=x[prev][curr]
    if len(cities)==len(path):
        global routes
        routes.append([distance,path+[0]])
        return
    for city in cities:
        if city not in path:
            find_paths(city,curr,cities,list(path),x,distance)

def f(x):
    cities=list(range(len(x)+1))
    for i in range(len(x)):
        x[i]=['mitsos']*(i+1)+x[i]
    find_paths(0,0,cities,[],x,0)

    print(min(routes)[1])
f([[518, 711, 908, 526, 431, 731, 898, 661, 487],
 [586, 634, 850, 668, 441, 624, 699, 728],
 [910, 895, 928, 536, 875, 747, 477],
 [679, 909, 572, 543, 728, 734],
 [871, 599, 615, 836, 715],
 [739, 874, 994, 544],
 [859, 624, 742],
 [886, 528],
 [740]])