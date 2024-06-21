import numpy as np
lx = np.arange(10)
ly = np.arange(10,20)
ones = np.ones(10)
m = (lx[:,np.newaxis]*ly[:,np.newaxis]*ones[np.newaxis, :])
print(m)
