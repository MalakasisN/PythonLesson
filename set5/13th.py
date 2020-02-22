import numpy as np
men=np.random.normal(1.77,0.07,1000000)
women=np.random.normal(1.65,0.06,1000000)
print('The probability for a random greek woman to be taller than a random greek man is p=',len(women[women>men])/len(women))