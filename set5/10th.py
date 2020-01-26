import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('baseis.xls')

line_1 = df.iloc[0].values
line_2 = df.iloc[1].values

columns = [y if pd.isna(x) else x for x,y in zip(line_1, line_2)]

df.columns = columns
df = df[2:-1]
df['ΚΩΔΙΚΟΣ ΣΧΟΛΗΣ'] = df['ΚΩΔΙΚΟΣ ΣΧΟΛΗΣ'].astype(str)

df=df[df['ΕΙΔΟΣ ΘΕΣΗΣ']=="ΓΕΛ ΓΕΝIKH ΣΕΙΡΑ ΗΜ."]
df=df[df['ΒΑΘΜΟΣ ΠΡΩΤΟΥ']<20000]
df['ΕΠΙΤ/ΤΕΣ']=df['ΕΠΙΤ/ΤΕΣ'].astype(float)
dfkriti=df[df['ΙΔΡΥΜΑ'].str.contains("ΚΡΗΤΗ")]
dfothers=df[df['ΙΔΡΥΜΑ'].str.contains("^((?!ΚΡΗΤΗ).)*$")]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(dfothers['ΒΑΘΜΟΣ ΤΕΛΕΥΤΑΙΟΥ'],dfothers['ΒΑΘΜΟΣ ΠΡΩΤΟΥ'],c='black',s=dfothers["ΕΠΙΤ/ΤΕΣ"]**2/1000)
ax.scatter(dfkriti['ΒΑΘΜΟΣ ΤΕΛΕΥΤΑΙΟΥ'],dfkriti['ΒΑΘΜΟΣ ΠΡΩΤΟΥ'],c='red',s=dfkriti["ΕΠΙΤ/ΤΕΣ"]**2/1000)
ax.legend(['asd'],labels=["OTHERS",'KRHTH',])
ax.set_xlabel('ΒΑΘΜΟΣ ΤΕΛΕΥΤΑΙΟΥ',fontweight='bold')
ax.set_ylabel('ΒΑΘΜΟΣ ΠΡΩΤΟΥ',fontweight='bold')
ax.text(10000,6800,'dot scale represents ΕΠΙΤ/ΤΕΣ',fontweight='bold')
plt.show()