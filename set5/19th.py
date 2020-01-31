import numpy as np,re
from matplotlib.pyplot import imshow, figure
ll=[]
lll=[]
temp=''
alleles=2692
with open('A_gen.txt') as f:
    contents=f.read()
    l=re.findall(r'A\*.*',contents)
for i in l:
    ll.append(i[18:].replace(' ','').replace('|','').replace('\n',''))
for i in range(1,alleles):
    for j in range(i,len(ll),alleles):
        temp+=ll[j]
    lll.append(temp)
    temp=''
figure(num=None, figsize=(10, 10), dpi=160,)
image = np.zeros((len(lll),len(lll[0]), 3), dtype=np.int16)
for i in range(len(lll)):
    for j in range(len(lll[i])):
        if lll[i][j]=='*':
            image[i,j,0] = 255
            image[i,j,1] = 255
            image[i,j,2] = 255 
        elif lll[i][j]=='-':
            image[i,j,0] = 0
            image[i,j,1] = 255
            image[i,j,2] = 0
        elif lll[i][j]=='.':
            image[i,j,0] = 0
            image[i,j,1] = 0
            image[i,j,2] = 255
        else:
            image[i,j,0] = 255
            image[i,j,1] = 0
            image[i,j,2] = 0
imshow(image)