import numpy as np
import scipy as sp
p_better = 150
p_total = 400
p_same = p_total-p_better
n_better  = 250
n_total = 600
n_same = n_total-n_better
obs = np.array([[n_better, p_better], [n_same, p_same]])
odds, p = sp.stats.fisher_exact(obs,'greater')
a=0.01
if p<a:
    print('p-value:',p,'The drug is statistically effective')
else:
    print('p-value:',p,'The drug is not statistically effective')