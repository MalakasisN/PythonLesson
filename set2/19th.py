import math
def euc(a,b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def mes(a,b):
	# This function returns 2 numbers! 
	return (a[0]+b[0])/2, (a[1]+b[1])/2
def f(x):
    y=list(x)
    while True:
        dis=[(euc(i,j),i,j) for i in x for j in x if i!=j]
        x.remove(min(dis)[1])
        x.remove(min(dis)[2])
        x.append(mes(min(dis)[1],min(dis)[2]))
        if len(x)==1:
            l=[(euc(x[0],i),y.index(i)) for i in y]
            print(min(l)[1])
            break
    
f([(44, 29),
 (31, 1),
 (-14, 79),
 (98, -78),
 (-2, 34),
 (-80, -27),
 (98, -21),
 (25, -23),
 (33, 45),
 (-85, -40),
 (53, 81),
 (50, -53),
 (42, 56),
 (-30, 100),
 (74, 20),
 (-78, -80),
 (-39, 42),
 (87, 19),
 (15, 98),
 (85, -27)])