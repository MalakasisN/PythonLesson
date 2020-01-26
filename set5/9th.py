import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('baseis.xls')

line_1 = df.iloc[0].values
line_2 = df.iloc[1].values

columns = [y if pd.isna(x) else x for x,y in zip(line_1, line_2)]

df.columns = columns
df = df[2:-1]
df['ΚΩΔΙΚΟΣ ΣΧΟΛΗΣ'] = df['ΚΩΔΙΚΟΣ ΣΧΟΛΗΣ'].astype(str)

epitixontes=[]
idrimata=df['ΙΔΡΥΜΑ'].unique()
for i in idrimata:    
    x=(sum(df[df['ΙΔΡΥΜΑ']==i]['ΕΠΙΤ/ΤΕΣ']))
    epitixontes.append(x)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(idrimata,epitixontes,color='y')
ax.legend(labels=["ΕΠΙΤ/ΤΕΣ"])
plt.xticks(idrimata,rotation='vertical')
ax.set_xlabel('ΙΔΡΥΜΑ',fontweight='bold')
plt.show()