import numpy as np
def f(n):
    matrix=n*np.ones([2*n-1,2*n-1])
    for i in range(n,0,-1):
        matrix[n-1-i:n+i,n-1-i:n+i]=i+1
    matrix[n-1,n-1]=1
    return matrix
print(f(5))