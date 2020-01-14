def f(x,y):
    z=''
    y=list(y)
    k=0
    for i in range(len(x)):
        if x[i]=='+':
            z+=' '
        elif x[i]=='-':
            z+=y[0]
            y.remove(y[0])
            if y==[]:
                y=[' ']
        else:
            k+=1   
    if k==0:    
        print(z)
    else:
        print('error')
        
f('++-+--+-+++++++++++++-+-+++++-++--++-++++-+---++-++-+--++---++-+-++-------+-+++---+---++-+-+++-+-+++','ZABARAKATRANEMIA')