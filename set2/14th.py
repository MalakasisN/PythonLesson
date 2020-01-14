def f(x):
   c=''
   from collections import Counter
   for i in range(len(x)-1):
       a=(Counter(x[i])&Counter(x[i+1]))
       b=list(a)
       d=c.join(b)
       x[i+1]=d
   if b==[]:
       print('No common characters found')
   else:    
       print('Common characters are:',b)
       
f(['επιστρέφει',
    'παίρνει',
    'υπάρχουν ',
    'που'])