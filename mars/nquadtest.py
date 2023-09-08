from perpendicular import *
from cc_ss import *
import numpy as np
from scipy import integrate
x0 = 0
y0 = 0
z0 = 1
L = .9
x1 = [x0-L/2, x0+L/2]
x2 = [-L/2, L/2]
y1 = [y0-L/2, y0+L/2]
z1 = [z0-L/2, z0+L/2]
def func (x1, x2, y1, z1):
	return 1/np.sqrt( (x1-x2)**2 + y1**2 + z1**2 )

s = integrate.nquad(func, [x1, x2, y1, z1])[0]* k0 / (L*L)**2
print ("%e"%s)
sp =  perpendicular(L ,L, x0, y0,z0)
print ("%e"%(sp))
ss =  saeed(L ,L, x0, y0,z0)
print ("%e"%(ss))
# ~ 8.589790e+09 0 0 1
# ~ 8.996241e+08 0 0 10
# ~ 8.999962e+07 0 0 100
