import numpy as np
import scipy.stats as stats 
import matplotlib.pyplot as plt

with open('chr6.cases.gen') as f1:
    linesd=f1.readlines()
disease={}
for line in linesd:
    line_splitted = line.strip().split()
    disease[linesd.index(line)]={'snpid':line_splitted[1],'Position':line_splitted[2],'Samples':line_splitted[5:]}
with open('chr6.controls.gen') as f2:
    linesc=f2.readlines()
control={}
for line in linesc:
    line_splitted = line.strip().split()
    control[linesc.index(line)]={'snpid':line_splitted[1],'Position':line_splitted[2],'Samples':line_splitted[5:]}
for i in disease:
    AA=0
    Aa=0
    aa=0
    for j in range(2,len(disease[i]['Samples']),3):
        x=disease[i]['Samples'][j-2] + disease[i]['Samples'][j-1] + disease[i]['Samples'][j]
        if x=='100':
            AA+=1
        if x=='010':
            Aa+=1
        if x=='001':
            aa+=1
    disease[i]['AA']=AA
    disease[i]['Aa']=Aa
    disease[i]['aa']=aa
for i in control:
    AA=0
    Aa=0
    aa=0
    for j in range(2,len(control[i]['Samples']),3):
        x=control[i]['Samples'][j-2] + control[i]['Samples'][j-1] + control[i]['Samples'][j]
        if x=='100':
            AA+=1
        if x=='010':
            Aa+=1
        if x=='001':
            aa+=1
    control[i]['AA']=AA
    control[i]['Aa']=Aa
    control[i]['aa']=aa
pvals=[]
for i in range(len(control)):
    DA=2*disease[i]['AA']+disease[i]['Aa']
    CA=2*control[i]['AA']+control[i]['Aa']
    Da=2*disease[i]['aa']+disease[i]['Aa']
    Ca=2*control[i]['aa']+control[i]['Aa']
    obs=np.array([[DA,CA],[Da,Ca]])
    try:
        chi2, p, dof, ex=stats.chi2_contingency(obs)
        pvals.append((p,control[i]['snpid'],control[i]['Position']))
    except:
        pass
a=0.0001
for mut in pvals:
    if mut[0]<a:
        print('The mutation with SNP ID:',mut[1],',positioned on chromosome 6 at the position ',mut[2],'is significantly(threshold 0.0001) correlated with the disease.','\n P-value:',mut[0])

#Extra
logp=[]
pos=[]
for i in pvals:
    logp.append(-np.log10(i[0]))
    pos.append(i[2])

fig,ax=plt.subplots()
ax.scatter(pos,logp,c='g',s=5)
ax.axes.get_xaxis().set_visible(False)
ax.set_xlim([0,max(pos)])
ax.set_ylabel('minuslog10pvalue')
ax.set_title('Chromosome 6')
plt.show()