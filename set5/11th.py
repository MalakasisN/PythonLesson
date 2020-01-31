#unfinished

import numpy as np
import scipy as sp
p_better = 150
p_total = 400
p_same = p_total-p_better
n_better  = 250
n_total = 600
n_same = n_total-n_better
better_total = p_better + n_better
same_total = p_same + n_same
total = p_total + n_total
p_perc = p_better/p_total
n_perc = n_better/n_total
found_difference = n_perc-p_perc

obs = np.array([[p_better, n_better], [p_same, n_same]])
chi2, p, dof, expected = sp.stats.chi2_contingency(obs)
print(p)