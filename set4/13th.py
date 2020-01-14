import numpy as np

a = np.array([[8.017, 65.088, 87.134, 30.050, 58.340, 40.148],
       [67.919, 43.463, 79.004, 91.098, 22.282, 92.925],
       [35.850, 8.067, 55.315, 35.333, 84.915, 42.682],
       [90.585, 91.515, 39.380, 8.990, 58.726, 23.867],
       [56.745, 96.424, 50.007, 46.955, 72.845, 18.849],
       [16.405, 38.923, 22.694, 96.561, 32.377, 77.826],
       [42.870, 96.114, 89.887, 39.800, 68.252, 70.092],
       [52.975, 40.269, 74.661, 54.489, 5.173, 98.359],
       [75.736, 38.505, 87.102, 45.873, 38.369, 81.094],
       [22.243, 3.135, 0.230, 39.588, 28.393, 62.661]])
b = np.array([37.206, 43.282, 72.423, 85.898, 8.480, 9.290])
euc=list(np.linalg.norm(a-b,axis=1))
print('gene number',euc.index(min(euc))+1,'with euclidian distance',min(euc))