import numpy as np
import matplotlib.pyplot as plt
import hashlib 
def unique_8x8(s):
      
    result = hashlib.md5(s.encode()) 
    h = result.hexdigest()[-16:]
    l = ['{a:0>8b}'.format(a=bytearray.fromhex(h[i:i+2])[0]) for i in range(0, len(h), 2)]
    
    k = np.array([[int(y) for y in x] for x in l])
    return k
a=unique_8x8('Αλέξανδρος Καντεράκης')
for i in range(5):
    b=np.flip(a,axis=0)
    c=np.vstack([b,a])
    d=np.flip(c,axis=1)
    a=np.hstack([d,c])
    
plt.imshow(a,cmap='gray')