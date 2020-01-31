#Downloaded the file with "wget https://pastebin.com/raw/6nBX6sdE"

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import csv

def which_chromosome(AM):
    return (AM%22) + 1

which_chromosome(1120049) #chr8


gpos100 = (0/255,0/255,0/255)
gpos    = (0/255,0/255,0/255)
gpos75  = (130/255,130/255,130/255)
gpos66  = (160/255,160/255,160/255)
gpos50  = (200/255,200/255,200/255)
gpos33  = (210/255,210/255,210/255)
gpos25  = (200/255,200/255,200/255)
gvar    = (220/255,220/255,220/255)
gneg    = (255/255,255/255,255/255)
acen    = (217/255,47/255,39/255)
stalk   = (100/255,127/255,164/255)
allchroms=[]
chosenchrom=[]
chromosome='chr8'
with open('6nBX6sdE') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for band in reader:
        allchroms.append(dict(band))
for band in allchroms:
    if band['#chrom']==chromosome:
        chosenchrom.append(band)


fig, ax = plt.subplots()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_title(chromosome,fontsize=40)
ax.set_xlim(0,100)
ax.set_ylim(40000000+int(chosenchrom[-1]['chromEnd'],0))
ax.set_facecolor('lightblue')
for i in chosenchrom:
    if i['gieStain']=='gpos100':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos100)
        ax.add_patch(r)
    elif i['gieStain']=='gpos':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos)
        ax.add_patch(r)
    elif i['gieStain']=='gpos75':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos75)
        ax.add_patch(r)
    elif i['gieStain']=='gpos66':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos66)
        ax.add_patch(r)
    elif i['gieStain']=='gpos50':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos50)
        ax.add_patch(r)
    elif i['gieStain']=='gpos33':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos33)
        ax.add_patch(r)
    elif i['gieStain']=='gpos25':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gpos25)
        ax.add_patch(r)
    elif i['gieStain']=='gvar':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gvar)
        ax.add_patch(r)
    elif i['gieStain']=='gneg':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = gneg)
        ax.add_patch(r)
    elif i['gieStain']=='acen':   
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = acen)
        ax.add_patch(r)
    else:
        r = Rectangle((40, 20000000+int(i['chromStart'])), 20, (int(i['chromEnd'])-int(i['chromStart'])), color = stalk)
        ax.add_patch(r)
plt.show()