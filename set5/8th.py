import pandas as pd
df = pd.read_excel('baseis.xls')

line_1 = df.iloc[0].values
line_2 = df.iloc[1].values

columns = [y if pd.isna(x) else x for x,y in zip(line_1, line_2)]

df.columns = columns
df = df[2:-1]
df['ΚΩΔΙΚΟΣ ΣΧΟΛΗΣ'] = df['ΚΩΔΙΚΟΣ ΣΧΟΛΗΣ'].astype(str)

l=[]
df=df[df['ΕΙΔΟΣ ΘΕΣΗΣ']=="ΓΕΛ ΓΕΝIKH ΣΕΙΡΑ ΗΜ."]
idrimata=df['ΙΔΡΥΜΑ'].unique()
for i in idrimata:    
    x=(sum(df[df['ΙΔΡΥΜΑ']==i]['ΒΑΘΜΟΣ ΤΕΛΕΥΤΑΙΟΥ'])/len(df[df['ΙΔΡΥΜΑ']==i]),i)
    l.append(x)
df['Difference']=(df['ΒΑΘΜΟΣ ΠΡΩΤΟΥ']-df['ΒΑΘΜΟΣ ΤΕΛΕΥΤΑΙΟΥ'])
print('To idrima me to megalitero meso oro einai to',max(l)[1],'me meso oro',max(l)[0])
print('To idrima me to mikrotero meso oro einai to',min(l)[1],'me meso oro',min(l)[0])
print('H sxoli me ti megaliteri diafora prwtou kai teleutaiou einai h',df.sort_values(by=['Difference']).iloc[-1]['ΟΝΟΜΑ ΣΧΟΛΗΣ'],'me diafora',df.sort_values(by=['Difference']).iloc[-1]['Difference'])
print('To athroisma twn epitixontwn gia sxoles me vasi katw apo 10000 einai',sum(df[df['ΒΑΘΜΟΣ ΤΕΛΕΥΤΑΙΟΥ']<10000]['ΕΠΙΤ/ΤΕΣ']))