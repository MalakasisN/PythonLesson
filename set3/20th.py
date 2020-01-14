def sieve(n): 
    nNew =int((n-2)/2) 
    primes=[] 
    marked=[0]*(nNew+1)
    for i in range(1,nNew+1): 
        j=i; 
        while((i+j+2*i*j)<=nNew): 
            marked[i+j+2*i*j] = 1 
            j += 1; 
    if (n>2): 
        primes.append(2)
   
    for i in range(1,nNew + 1): 
        if (marked[i]==0): 
            primes.append(2*i+1)
    return primes
            
primes=sieve(1000000)

seqlength=0
largestsolution=0
primeslen=len(primes)
for i in range(len(primes)):
    for j in range(i+seqlength,primeslen):
        solution = sum(primes[i:j])
        if solution < 1000000:
            if solution in primes:
                consecutiveprimelist=primes[i:j]
                seqlength=len(consecutiveprimelist)
                largestsolution=solution
        else:
            primeslen=j+1
            break
    
print('The prime number',largestsolution,'can be written as the sum of',seqlength,'consecutive primes.','\n','Analytically,the list of the consecutive primes mentioned above is:',consecutiveprimelist)
