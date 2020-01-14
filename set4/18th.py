import numpy as np
x=np.random.random(100000)
y=np.random.random(100000)
centerx=0.5
centery=0.5
distance=np.sqrt((x-centerx)**2+(y-centery)**2)
validdarts=len(distance[abs(distance)<0.5])
totaldarts=100000
Percentage=(validdarts/totaldarts)*100
print(Percentage,'% of the darts are distanced 0.5 meters or less from the center.\n The Percentage times 4 is:',4*Percentage)