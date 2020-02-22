from sklearn.decomposition import PCA
import numpy as np
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
disgen=[]
congen=[]
for i in disease:
    temp=[]
    for j in range(2,len(disease[i]['Samples']),3):
        x=disease[i]['Samples'][j-2] + disease[i]['Samples'][j-1] + disease[i]['Samples'][j]
        if x=='100':
            temp.append(0)
        if x=='010':
            temp.append(1)
        if x=='001':
            temp.append(2)
    disgen.append(temp)
for i in control:
    temp=[]
    for j in range(2,len(control[i]['Samples']),3):
        x=control[i]['Samples'][j-2] + control[i]['Samples'][j-1] + control[i]['Samples'][j]
        if x=='100':
            temp.append(0)
        if x=='010':
            temp.append(1)
        if x=='001':
            temp.append(2)
    congen.append(temp)

disgen_array = np.array(disgen).T
congen_array = np.array(congen).T
totalgen_array=np.vstack((disgen_array,congen_array))
pca = PCA(n_components=2)
pca.fit(totalgen_array)
genotypes_PCA = pca.transform(totalgen_array)
plt.plot(genotypes_PCA[:100,0], genotypes_PCA[:100,1], '.', color="black")
plt.plot(genotypes_PCA[100:,0], genotypes_PCA[100:,1], '.', color="red")
plt.show()